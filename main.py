#爬取博客的页面数据 https://blog.samaltman.com/
#爬取的信息：文章标题、正文、发表时间、链接、Upvotes 数、Response 数
#保存格式 单个json file     每篇文章一个markdown
import requests
# from bs4 import BeautifulSoup
from lxml import etree
import json
import pprint
conten_json = []
def download_all_htmls():
    htmls = []
    for idx in range(12):
        url = f"https://blog.samaltman.com/?page={idx+1}"
        print("craw html:",url)
        r = requests.get(url)
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
    for link in link_list:
        url = link
        print(url)
        r = requests.get(url)
        if r.status_code !=200:
            continue
        parse = etree.HTML(html)
        # # 解析标题
        title = parse.xpath('//*[@id="main"]/article/header/div/h2/a/text()')[0]
        # 链接
        link = url
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
            '标题': title, '发表时间': time, '赞同数': Upvotes, '回复数': Upvotes
        }
        print(info)
        conten_json.append(info)

for html in download_all_htmls():
    link_list = parse_linK(html)
    print(link_list)
    parse_data(link_list)

print(conten_json)
json.dump(conten_json, open('./博客.json', mode='w', encoding='utf-8'), ensure_ascii=False, indent=4)