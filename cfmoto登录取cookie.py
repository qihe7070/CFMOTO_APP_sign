import requests
import json
Code_url = 'https://c.cfmoto.com/common/code/send_code/'
login_url = 'https://c.cfmoto.com/auth/user/login_by_verifycode/'
app_header = {
    'cookie': 'ticket=',
    'User-Agent': 'MOBILE|Android|11|KLICEN_APP|5.0.2|Dalvik/2.1.0 (Linux; U; Android 11; GM1910 Build/RKQ1.200826.002)|1440*3064|5f9aecaf81ebdd23|100',
    'interfaceversion': '1',
    'Content-Type': 'application/json; charset=UTF-8',
    'Content-Length': '50',
    'Host': 'c.cfmoto.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}
phone = input('输入手机号：')
#发送验证码数据包
Code_data = '{"msg_type":0,"phone":"' + phone + '","voice":false}'
#发送验证码数据
Code_post = requests.post(url=Code_url,headers=app_header,data=Code_data).json()
Code_msg = Code_post['msg']
if Code_msg == '发送成功':
    print(Code_msg)
    print('请输入验证码！！！')
    phone_Code = input('输入验证码：')
    login_data =' {"phone":' + phone +',"verify_code":' + phone_Code + ',"version":"v1"}'
    login_post = requests.post(url=login_url,headers=app_header,data=login_data).json()
    login_msg = login_post['msg']
    if login_msg == '登录成功':
        login_msg_data = login_post['data']
        login_ticket = login_msg_data['ticket']
        print(login_ticket)
        fp = open('cookie.txt','w',encoding='utf-8')
        json.dump(login_ticket,fp=fp,ensure_ascii=False)
        print('cookie信息以存储到程序目录下')
    else:
        print(login_msg)
        print('请重新输入验证码！！！')
else:
    print(Code_msg)
    print('请稍后再试！！！')