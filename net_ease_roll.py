from bs4 import BeautifulSoup
import urllib.request
import requests
import json

dir = 'Your Path'
url = 'http://news.163.com/special/0001220O/news_json.js?0.48118750578546954'
request = requests.get(url)
data = request.text[9:-1]
# print(data)
internal = json.loads(data)['news'][0]
external = json.loads(data)['news'][1]
society = json.loads(data)['news'][2]

news_list = {}
for i in internal:
    news_list[i['t']] = i['l']

for e in external:
    news_list[e['t']] = e['l']

for s in society:
    news_list[s['t']] = s['l']

# print(len(news_list))

index = 1
for key in news_list:
    url = news_list[key]
    request = urllib.request.urlopen(url)

    html = BeautifulSoup(request.read(), 'html5lib')

    content = html.find('div', {'class': 'post_body'})
    content = content.find_all('p')
    with open(dir + str(index) + '.txt', 'a', encoding='utf-8') as news_file:
        news_file.write(key + '\r\n')
        for c in content:
            text = c.text
            text = text.strip()
            if len(text) > 0 and text[0] != '#' \
                and text != '用微信扫码二维码' and text != '分享至好友和朋友圈':
                news_file.write(text + '\r\n')

    print(index)
    index += 1