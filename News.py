import urllib.request
import re
import os


class news:

    def print_news(self):
        site = urllib.request.urlopen('https://news.yandex.ru/')
        html = site.read().decode('utf8')
        header_tags = re.findall(r'<h[1-2][^>]*><a[^>]*>(.*?)</a></h[1-2]>', str(html))
        os.system('cls')
        print(str('\n'.join(header_tags)))
        return
