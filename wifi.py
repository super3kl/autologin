
import base64
import requests
import re
import time
#
USER_ACCOUNT='11111111'
DOMAIN_SELECTION='Unicom'#这是中国联通
USER_PASSWATD='1111111'

#登录地址
post_addr="http://a.nuist.edu.cn/index.php/index/login"

def post_():

   #构造头部信息
   post_header={
   'Host': 'a.nuist.edu.cn',
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
   'Connection':'keep-alive',
   }

   post_data={'domain':DOMAIN_SELECTION,
      'enablemacauth':'0',
      'password':base64.b64encode(USER_PASSWATD.encode()),
      'username':USER_ACCOUNT
      }
   #发送post请求登录网页
   z=requests.post(post_addr,data=post_data,headers=post_header)
   response = requests.get('http://a.nuist.edu.cn/index.php/index/login')
   print(response.json())

def testconnect():
        try:
            q = requests.get("http://www.baidu.com",timeout=5)
            m = re.search(r'STATUS OK',q.text)
            print(q)
            if m:
               return True
            else:
               return False
        except:
            print ('error')
            return False

if __name__ == '__main__':
   while(True):
      if testconnect():
         time.sleep(1)
      else:
         post_()
