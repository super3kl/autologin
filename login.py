'''
Author: zyc
Date: 2021-01-12 09:32:14
LastEditTime: 2021-01-12 21:27:18
LastEditors: zyc
Description: log in INuist and send message to wechat
FilePath: login.py
'''
import base64
import requests
import re
import time
   
USER_ACCOUNT='xxxxx'

## choose DOMAIN_SELECTION
## Unicom
## CMCC
## ChinaNet
## Nuist
DOMAIN_SELECTION='xxxx'
USER_PASSWATD='xxxxx'
sckey = ''

class logInNuist:
    def __init__(self):
        self.post_addr = "http://a.nuist.edu.cn/index.php/index/login"
        self.post_header = {   'Host': 'a.nuist.edu.cn',
                                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0',
                                'Accept': 'application/json, text/javascript, */*; q=0.01',
                                'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                                'Accept-Encoding': 'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-Requested-With':'XMLHttpRequest',
                                'Referer':'http://a.nuist.edu.cn/index.php?url=aHR0cDovL2RldGVjdHBvcnRhbC5maXJlZm94LmNvbS9zdWNjZXNzLnR4dA==',
                                'Content-Length': '68',
                                'Cookie':'_gscu_1147341576=059821653286gq10; sunriseUsername='+USER_ACCOUNT+';\
                                sunriseDomain='+DOMAIN_SELECTION+';sunriseRememberPassword=true; sunrisePassword='+USER_PASSWATD+';\
                                PHPSESSID=hb0o9bkct2f6ge164oj3vj0me5;think_language=zh-CN',
                                'Connection':'keep-alive'
                                }
        self.post_data = {'domain':DOMAIN_SELECTION,
            'enablemacauth':'0',
            'password':base64.b64encode(USER_PASSWATD.encode()),
            'username':USER_ACCOUNT
            }

    def post(self):
        z = requests.post(self.post_addr,
                        data = self.post_data,
                        headers = self.post_header)
        response = requests.get('http://a.nuist.edu.cn/index.php/index/login')
        print(response.json())

    def test_connect(self):
        try:
            q = requests.get("http://www.baidu.com",timeout=5)
            m = re.search(r'STATUS OK',q.text)
            if m:
               return True
            else:
               return False
        except:
            print ('error')
            return False

    def send_message(self,text='test',desp='test'):
        url = 'https://sc.ftqq.com/%s.send?'
        content = (url + 'text=' + text  + '&desp=' + desp)%sckey
        requests.get(content)
        print('sending message is done')
        


if  __name__ == '__main__':


    login_nuist = logInNuist()
    if login_nuist.test_connect():
        pass
    else:
        login_nuist.post()
        print('network reconnected success')
        if len(sckey) > 0:
            login_nuist.send_message(text = 'network reconnected',
                                    desp = 'done')
