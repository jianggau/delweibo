import requests
from bs4 import BeautifulSoup

user = ''
passwords = ''
def get_info(a, b, c):
    info = soup.find(attrs={a:b})[c]
    return info


UA = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.76 Safari/537.36'
headers = {
         'User-Agent': UA,
         'Host': 'login.weibo.cn',
         'Origin': 'https://login.weibo.cn',
         'Referer': 'https://login.weibo.cn/login/?'
         }

s = requests.Session()
url = 'https://login.weibo.cn/login/?'
text = s.get(url, headers=headers, verify = False).text
soup = BeautifulSoup(text)
pwd = get_info('type', 'password', 'name')
vk = soup.find(attrs={'name':'vk'})['value']
print vk
print pwd

payoff = {
        'mobile' : user,
        pwd : passwords,
        'remember' : 'on',
        'backURL' : 'http%3A%2F%2Fweibo.cn',
        'vk' : vk,
        'tryCount': '',
        'backTitle': '%E6%89%8B%E6%9C%BA%E6%96%B0%E6%B5%AA%E7%BD%91',
        'submit': '%E7%99%BB%E5%BD%95'
        }
r = s.post(url, data=payoff, headers=headers, verify=False)
plink = s.get('http://weibo.cn')
soup3 = BeautifulSoup(plink.text)
tag3 = soup3.find(attrs={'class':'tip2'})
plink3 = 'http://weibo.cn' + tag3.find('a').get('href')
print plink3

while True:
    rssd = s.get(plink3)
    soup2 = BeautifulSoup(rssd.text)
    
    tag = soup2.find(attrs={'class':'ct'})
    print tag, type(tag)
    
    dict = []
    for link in soup2.find_all('a'):
        if link.string == u'\u5220\u9664':
            #print(link.get('href'))
            dict.append(link.get('href'))
            #print dict
    
    for link2 in dict:
        link3 = link2 + '&act=del'
        s.get(link3)
