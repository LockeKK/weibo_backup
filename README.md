# weibo_backup
Backup your weibo post

Check your environment, make sure you get

request module AND Python 3.5+

You need to get your weibo post URL and specify them in weibo_saver.py

#YOU HAVE TO SPECIFY THE WEIBO POST COUNT AND YOUR ID

POST_COUNT = 708

#do it like this:

#with Chrome, login to your mobile weibo web: https://m.weibo.cn/u/1820518xxx

#Click F12, see the souce code, select "Network", search "getIndex"

#Check the item, right click, choose "copy link address", you will get the the URL like below

#You might need to scroll down your weibo page to get this string.

#THE KEY INFORMATION IS THE containerid, YOU COULD JUST REPLACE MY ONE

url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=XXXX&containerid=10760318205xxxxx&page='

You can refer the details from below authors:

不知名网友：

https://dlyang.me/weibo-export/

知乎网友梁爱丽

https://www.zhihu.com/question/20339936/answer/195823664

Acknowledge to their efforts.
