import time
import requests
import json

def start_craw(url,app_Cookie,url_dianzan,dianzan_header,app_header,pushplus_token,phone,star_integralTotal):
    #回复任务
    print('开始回复任务')
    huifu_task1 = requests.post(url='https://c.cfmoto.com/jv/bbs/article/comment-v1/', headers=app_header,data='{"content":"Very good!","post_id":"106586"}')
    print(huifu_task1.text)
    time.sleep(1)
    huifu_task2 = requests.post(url='https://c.cfmoto.com/jv/bbs/article/comment-v1/', headers=app_header,data='{"content":"Very good!!","post_id":"106586"}')
    #print(huifu_task2.text)
    time.sleep(1)
    huifu_task3 = requests.post(url='https://c.cfmoto.com/jv/bbs/article/comment-v1/', headers=app_header,data='{"content":"Very good!!!","post_id":"106586"}')
    #print(huifu_task3.text)
    respon_huifu_task = huifu_task1.status_code
    if respon_huifu_task == 200:
        print('回复任务成功')
        #print(dianzan_data.text)
    else:
        print('回复任务失败')
    #发帖任务
    print('开始发帖任务')
    time.sleep(1)
    #fatie_data = '{"address":"","city_code":"0","content":"Go Out Cycling!","is_vote":false,"latitude":0.0,"longitude":0.0,"resource_list":[],"media_type":"TEXT","tags":[],"title":"","topic_list":[],"post_vote_list":[]}'
    fatie_task1 = requests.post(url='https://c.cfmoto.com/jv/bbs/post/create-v5/', headers=app_header,data='{"address":"","city_code":"0","content":"Go Out Cycling!","is_vote":false,"latitude":0.0,"longitude":0.0,"resource_list":[],"media_type":"TEXT","tags":[],"title":"","topic_list":[],"post_vote_list":[]}')
    print(fatie_task1.text)
    time.sleep(2)
    fatie_task2 = requests.post(url='https://c.cfmoto.com/jv/bbs/post/create-v5/', headers=app_header,data='{"address":"","city_code":"0","content":"Go Out Cycling!!","is_vote":false,"latitude":0.0,"longitude":0.0,"resource_list":[],"media_type":"TEXT","tags":[],"title":"","topic_list":[],"post_vote_list":[]}')
    #print(fatie_task2.text)
    time.sleep(2)
    fatie_task3 = requests.post(url='https://c.cfmoto.com/jv/bbs/post/create-v5/', headers=app_header,data='{"address":"","city_code":"0","content":"Go Out Cycling!!!","is_vote":false,"latitude":0.0,"longitude":0.0,"resource_list":[],"media_type":"TEXT","tags":[],"title":"","topic_list":[],"post_vote_list":[]}')
    #print(fatie_task3.text)
    respon_fatie_task = fatie_task1.status_code
    if respon_fatie_task == 200:
        print('发帖任务成功')
        #print(dianzan_data.text)
    else:
        print('发帖任务失败')
    #点赞任务
    print('开始点赞任务')
    time.sleep(1)
    requests.delete(url_dianzan,headers=dianzan_header)
    time.sleep(1)
    requests.post(url_dianzan,headers=dianzan_header)
    time.sleep(1)
    requests.delete(url_dianzan,headers=dianzan_header)
    time.sleep(1)
    requests.post(url_dianzan,headers=dianzan_header)
    time.sleep(1)
    requests.delete(url_dianzan,headers=dianzan_header)
    time.sleep(1)
    requests.post(url_dianzan,headers=dianzan_header)
    time.sleep(1)
    requests.delete(url_dianzan,headers=dianzan_header)
    time.sleep(1)
    requests.post(url_dianzan,headers=dianzan_header)
    time.sleep(1)
    requests.delete(url_dianzan,headers=dianzan_header)
    time.sleep(1)
    requests.post(url_dianzan,headers=dianzan_header)
    time.sleep(1)
    dianzan_data = requests.post(url_dianzan,headers=dianzan_header)
    respon_dianzan_data = dianzan_data.status_code
    if respon_dianzan_data == 200:
        print('点赞任务成功')
        print(dianzan_data.text)
    else:
        print('点赞任务失败')
    #签到任务
    print('开始签到任务')
    time.sleep(1)
    qiandao_data = '{"completeStatu" : 1,"taskDetail" : 8}'
    return_qiandao_data = requests.put(url,headers=app_header,data=qiandao_data)
    respon_return_qiandao_data = return_qiandao_data.status_code
    if respon_return_qiandao_data == 200:
        print('签到任务成功')
        #print(return_qiandao_data.text)
    else:
        print('签到任务失败')
    #每日分享
    print('开始每日分享任务')
    time.sleep(1)
    fengxiang_data = '{"completeStatu" : 1,"taskDetail" : 13}'
    return_fengxiang_data = requests.put(url,headers=app_header,data=fengxiang_data)
    time.sleep(1)
    return_fengxiang_data = requests.put(url,headers=app_header,data=fengxiang_data)
    time.sleep(1)
    return_fengxiang_data = requests.put(url,headers=app_header,data=fengxiang_data)
    time.sleep(1)
    return_fengxiang_data = requests.put(url,headers=app_header,data=fengxiang_data)
    respon_return_fengxiang_data = return_fengxiang_data.status_code
    if respon_return_fengxiang_data == 200:
        print('每日分享成功')
        #取账号信息
        #运行完
        id_information = requests.get(url='https://c.cfmoto.com/cfmotoservermall/app/user/integral/current/user/info', headers=dianzan_header).json()
        id_information = id_information['data']#运行结束提取出data字典
        integralTotal = id_information['integralTotal']#总积分
        overdueIntegral = id_information['overdueIntegralCopywriting']#剩余积分
        userId = id_information['userId']#账号id
        pushplus_title= 'CFMOTO签到' #改成你要的标题内容
        pushplus_print_content = '手机号：' + str(phone) + '\n账号ID：' + str(userId) + '\n初始积分：' + str(star_integralTotal) + '\n积分总数：' + str(integralTotal) + '\n' + str(overdueIntegral)
        pushplus_url = 'http://www.pushplus.plus/send?token='+pushplus_token+'&title='+pushplus_title+'&content='+pushplus_print_content
        requests.get(pushplus_url)
    else:
        print('签到任务失败')
    #结束
    print('账号：' + app_Cookie +'，春风摩托APP任务已完成！')

if __name__=="__main__":
    url = 'http://c.cfmoto.com/cfmotoservermall/app/integral/task/complete'
    url_dianzan = 'https://c.cfmoto.com/jv/bbs/post/thumbs_up/106392'
    #从列表取数据循环执行
    app_Cookie_list = [
        #app抓包 支持多账号！
        'ticket=TK-******-****;vehicle_id=-1',#132****5062
        'ticket=TK-******-****;vehicle_id=-1',#198****5206
        'ticket=TK-******-****;vehicle_id=-1',#189****0832
        'ticket=TK-******-****;vehicle_id=-1',#132****6562
    ]
    ret = []
    for i in range(0,len(app_Cookie_list), 1):
        ret.append(app_Cookie_list[i:i+1])
        time.sleep(3)
        app_Cookie = ''.join(app_Cookie_list[i:i+1])
        print(app_Cookie)
        #header
        app_header = {
            'Host': 'c.cfmoto.com',
            'interfaceversion': '1',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Cookie': app_Cookie,
            'User-Agent': 'MOBILE|iOS|15.4|KLICEN_APP|5.0.1|iPhone|iPhone|1170*2532|13C74FB1-4F8C-42FD-BCB7-836DB6AF2FB3',
            'Accept-Language': 'zh-Hans-CN;q=1',
            'Content-Length': '45',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        #点赞header
        dianzan_header = {
            'cookie': app_Cookie,
            'User-Agent': 'MOBILE|Android|10|KLICEN_APP|5.0.1|Dalvik/2.1.0 (Linux; U; Android 10; GM1910 Build/QKQ1.190716.003)|1440*3064|5c297b2b2656c79d|100',
            'interfaceversion': '1',
            'Content-Length': '0',
            'Host': 'c.cfmoto.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
        }
        pushplus_token = '你的pushplus token' #在pushpush网站中可以找到  http://pushplus.plus/push1.html
        star_id_information = requests.get(url='https://c.cfmoto.com/cfmotoservermall/app/user/integral/current/user/info', headers=dianzan_header).json()
        star_code = star_id_information['code']
        #print(star_code)
        if star_code == 0:
            print('code=0正常运行')
            #取手机号json
            id_phone= requests.get(url='https://c.cfmoto.com/cfmotoserverim/app/service/rongcloud/token', headers=dianzan_header).json()
            star_code = id_phone['data']
            phone = star_code['phone']#手机号=phone
            star_id_information_data = star_id_information['data']#运行前初始积分data
            star_integralTotal = star_id_information_data['integralTotal']#运行前初始积分
            #调出函数
            start_craw(url,app_Cookie,url_dianzan,dianzan_header,app_header,pushplus_token,phone,star_integralTotal)
        else:
            print('code=401,运行错误,Cookie失效!')
            pushplus_title= 'CFMOTO签到错误' #改成你要的标题内容
            pushplus_print_content = 'Cookie失效，请重新抓取填写！\n' + '失效Cookie：'+ app_Cookie
            pushplus_url = 'http://www.pushplus.plus/send?token='+pushplus_token+'&title='+pushplus_title+'&content='+pushplus_print_content
            pushplus_requests = requests.get(pushplus_url)
            print(pushplus_requests.text)
    else:
        print('全部Cookie账号任务执行结束！')
