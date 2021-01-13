<!--
 * @Author: zyc
 * @LastEditors: zyc
-->
# 自动登录Nuist校园网 & 断网自动重连并发送消息至微信
# 谢谢Star
本python脚本自动登录部分借鉴了[校园网自动登录](https://blog.csdn.net/shenhuaifeng/article/details/78333851)
# 说明
1. USER_ACCOUNT内填自己账号，
2. DOMAIN_SELECTION填入网络类型。中国移动：CMCC 中国联通：Unicom 中国电信：ChinaNet 南信大：Nusit
3. USER_PASSWATD填入密码
4. 如需微信推送重连信息 则需填入sckey 此服务由[server酱提供](http://sc.ftqq.com/3.version),注册获取sckey
5. 设定定时任务 linux参考[crontab](https://www.runoob.com/linux/linux-comm-crontab.html)。可设置为每分钟运行一次ligin.py


#更新日志
2021.1.13，增加获取电脑ip功能
