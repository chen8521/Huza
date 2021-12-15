# coding=utf-8
#翻译图标

def tran(q):
    import http.client
    import hashlib
    import urllib
    import random
    import json

    appid = '20200427000431745'  # 填写你的appid
    secretKey = 'CSAEdcf1tOTVH2LefCMi'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'zh'   #原文语种
    toLang = 'en'   #译文语种
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        print (result)
        return result

    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()

if __name__ == '__main__':
    import os
    import time
    all = []
    p = r'C:\Users\hufei\Desktop\db'
    for i in os.listdir(p):
        time.sleep(1)
        r = tran(i)
        all.append(r)
