#!/usr/bin/python
# coding=utf-8
#Check your environment, make sure you get
#request module AND Python 3.5+
import requests
import time
import random
import json

#YOU HAVE TO SPECIFY THE WEIBO POST COUNT AND YOUR ID
POST_COUNT = 708
#do it like this:
#with Chrome, login to your mobile weibo web: https://m.weibo.cn/u/1820518xxx
#Click F12, see the souce code, select "Network", search "getIndex"
#Check the item, right click, choose "copy link address", you will get the the URL like below
#You might need to scroll down your weibo page to get this string.
#THE KEY INFORMATION IS THE containerid, YOU COULD JUST REPLACE MY ONE
url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=XXXX&containerid=10760318205xxxxx&page='

json_file = []
total_count = int((POST_COUNT+5)/10)
for i in range(total_count):
    data = requests.get(url+str(i))
    print(data.content)
    print("[%d out of %d]" % (i, total_count))
    json_file.append((data.content.decode('utf-8')))
    time.sleep(random.uniform(1, 5))

print("Retrieve from weibo done. Now convert it into html")
with open('weibo.html', 'wb') as f_html:
    f_html.write('<html><head><title>Somebody\'s Weibo Archive</title></head><body>'
                 '<div">\n'
                 '<link type="text/css" rel="stylesheet" charset="utf-8" href="default.css" />'.encode('utf-8'))
    f_html.write('<h1>微博存档</h1><hr>'.encode('utf-8'))

    for i in range(len(json_file)):
        content = json_file[i]
        items = json.loads(content).get('data')
        write_msg = '\n<!-- json #' + str(i) +'-->\n'
        if 'cards' not in items:
            break

        for card in items['cards']:
            if 'mblog' not in card:
                continue

            name = json.dumps(card['mblog']['user']['screen_name'], ensure_ascii=False)  # 因为都是重复的同样的ID，所以没有写进文件里。
            time = json.dumps(card['mblog']['created_at'], ensure_ascii=False)
            mfrom = json.dumps(card['mblog']['source'], ensure_ascii=False)
            text = json.dumps(card['mblog']['text'], ensure_ascii=False)
            text = str(text)
            text = text.replace('\\', '')  # escape字符也是很恶心的东西，删掉。
            text = text.replace('//h5.sinaimg', '\"https://h5.sinaimg')  # 处理某些图片的URL问题
            print(text)
            f_html.write('<div>'.encode('utf-8'))

            write_msg += '<p>Date: ' + time + '</p>\n' + '<p>Source: ' + mfrom + '</p>\n' + '<p>' + text + '</p>\n'

            if 'original_pic' in card['mblog']:  # 这两行建议一开始别加进去，文本调试OK以后再加，不然HTML页面会加载很久，尤其是图多or网速不好的时候。
                write_msg += '<img class="orig" src=' + json.dumps(card['mblog']['original_pic'], ensure_ascii=False) + '>\n'
            write_msg += '</div><hr>\n\n'
            f_html.write(write_msg.encode('utf-8'))
            f_html.flush()
            write_msg = ''
    f_html.write('</div></body></html>'.encode('utf-8'))
    f_html.flush()
    print('Task finished.')
    f_html.close()

