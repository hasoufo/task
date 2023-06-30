import json

def find():
    name = input('输入要搜索的内容，多个关键字需使用空格！！：')

    f = open(r'./博客.json',encoding='utf-8')
    results = json.load(f)
    for result in results:
        print(result)
    if ' ' in name:
        key = name.split(' ')
        print(key)
        if 'dalle' in key:
            key[key.index('dalle')] = 'DALL•E'
        for result in results:
            for id in key:
                if id.lower() in str(result["正文"]).lower():
                    print('关键字={}已找到！'.format(id))
                    print('标题={}\n发表时间={}\n赞同数={}\n回复数={}\n正文={}'.format(result['标题'],result['发表时间'],result['赞同数'],result['回复数'],result['正文']))
    elif '&' in name:
        keys = name.split('&')
        if 'dalle' in keys:
            keys[keys.index('dalle')] = 'DALL•E'
        for result in results:
            if keys[0].lower() and keys[1].lower() in str(result["正文"]).lower():
                print('关键词:{}和{}已找到！'.format(keys[0],keys[1]))
                print('标题={}\n发表时间={}\n赞同数={}\n回复数={}\n正文={}'.format(result['标题'],result['发表时间'],result['赞同数'],result['回复数'],result['正文']))
    elif '-' in name:
        keys = name.split('-')
        if 'dalle' in keys:
            keys[keys.index('dalle')] = 'DALL•E'
        for result in results:
            if keys[0].lower() in str(result["正文"]).lower() and keys[1].lower() not in str(result["正文"]).lower():
                print('关键词:{}但是不包括{}已找到！'.format(keys[0],keys[1]))
                print('标题={}\n发表时间={}\n赞同数={}\n回复数={}\n正文={}'.format(result['标题'],result['发表时间'],result['赞同数'],result['回复数'],result['正文']))
# def find():
    # ID = ['A','B','C','D','E','F','G','H','I','J','K','L','M','I','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    # name = input('输入要搜索的内容，多个关键字需使用空格！！：')
    # key = name.split() if '' in name else '!'
    # print(key)
    # if len(key) == 2:
    #     key.append('')
    #     next = 1
    #     for i in ID:
    #         f = open(r'C:\Users\HP\PycharmProjects\pythonProject1\博客.json',encoding='utf-8')
    #         result = json.load(f)
    #         print(result)
            # read = (f.read()).split('/n')
            # print('将在',i,'子目录中搜索',name)
            # for i in read:
            #     if key != '!':

#                 if str(key[0]).title() in i and key[1] in i and key[2] in i:
#                  print ('种子编号')
#                  print(i)
#                  next +=1
#                 if name in i and key =='!':
#                     print('种子编号')
#                     print(1)
#                     print +=1
#                 if next == 10:
#                     n=input('继续搜索请输入[空格]      搜索新内容请键入[+]')
#                     if n == '+':
#                         find()
#                     if n == '':
#                         next  = 1
find()
