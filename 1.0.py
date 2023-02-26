import requests
import json
b='449513162266419200'#初始化消息id（填需要发送频道的最后一条消息链接的最后一串数字,必须设置）
okkey=0
while True:
    import time
    time.sleep(1)
    url='https://a1.fanbook.mobi/api/bot/b27c98a520500c7c0b5f37ee75cb575b97228baacac1e55cf5c4b5/message/getList'#注意令牌
    headers = {'content-type':"application/json;charset=utf-8"}
    jsonfile=json.dumps({'channel_id':'39900596224','message_id':b,'behavior':'after'})#channel_id填频道id
    postreturn=requests.post(url,data=jsonfile,headers=headers)
    a=str(postreturn.text)
    okkey+=1
    if len(a)>150:
                desc_data = json.loads(postreturn.text)["data"]
                desc_data = json.loads(desc_data[0]['content'])
                desc_data = desc_data['text']
                print(desc_data)
                url='https://a1.fanbook.mobi/api/bot/b27c98a520500c7c0b5f37ee75cb62460d447b0fd575b97228baacac1e55cf5c4b5/sendMessage'#注意令牌
                headers = {'content-type':"application/json;charset=utf-8"}
                jsonfile=json.dumps({"chat_id":399900596224,"text":'你说了：'+desc_data})#指定回复内容，可以使用in判断并回复更多内容
                postreturn=requests.post(url,data=jsonfile,headers=headers)
                c=postreturn.text
                b=c[34:52]
