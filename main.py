#爬取博客的页面数据 https://blog.samaltman.com/
#爬取的信息：文章标题、正文、发表时间、链接、Upvotes 数、Response 数
#保存格式 单个json file     每篇文章一个markdown
import requests
from lxml import etree
import json


conten_json = []
def download_all_htmls():
    headers = {
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58"
    }
    htmls = []
    for idx in range(12):
        url = f"https://blog.samaltman.com/?page={idx+1}"
        print("craw html:",url)
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            raise Exception("error")
        htmls.append(r.text)
    return htmls

#
def parse_linK(html):
    # print(html)
    parse = etree.HTML(html)
    link_list = parse.xpath('//*[@id="main"]/article/header/div/h2/a/@href')
    return link_list

def parse_data(link_list):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58"
    }
    for link in link_list:
        url = link
        print(url)
        r = requests.get(url, headers=headers)
        if r.status_code !=200:
            continue
        parse = etree.HTML(r.text)
        # # 解析标题
        title = parse.xpath('//*[@id="main"]/article/header/div/h2/a/text()')[0]
        # 正文 ['', '']
        content = ''.join(parse.xpath('//div[@class="posthaven-post-body"]//text()'))
        # 发表时间
        time = parse.xpath('//span[@class="posthaven-formatted-date"]/@data-unix-time')[0]
        print('time:', time)
        #Upvotes数
        Upvotes = parse.xpath('//span[@class="posthaven-upvote-number"]/text()')[0]
        print('Upvotes:', Upvotes)
        # response 数
        response = ''.join(parse.xpath('//div[@class="count"]//text()'))
        info = {
            '标题': title, '发表时间': time, '赞同数': Upvotes,
            '回复数': response.replace('\n', '').replace(' ', '').replace('responses', ''), '正文': content
        }
        print(info)
        conten_json.append(info)

for html in download_all_htmls():
    link_list = parse_linK(html)
    print(link_list)
    parse_data(link_list)

print(conten_json)
json.dump(conten_json, open('./博客.json', mode='w', encoding='utf-8'), ensure_ascii=False, indent=4)