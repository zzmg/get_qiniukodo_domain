# -*- coding: UTF-8 -*- 
import json
import sys
import qiniu
import requests
from hashlib import sha1
import hmac
from base64 import b64encode
import hashlib
from Crypto.Hash import SHA, HMAC

reload(sys)

sys.setdefaultencoding('utf-8')

access_key = 'RQ-0qS4uk-PuRfCiSHyDnfwbS5TPj8vp1fMej5IQ'
secret_key = 'zaYQPfYpTGklojTBzVh2Vv7S2IQvkipedQCpvGgb'

with open ('/Users/zhangmengege/Documents/python-workespace/json.txt','r') as f:
    data = json.load(f)
    print(len(data))
    for  i in data:
        print(i["tbl"])
        line = i["tbl"]
        url = 'http://api.qiniu.com/v6/domain/list?tbl='+line
        signingStr = '/v6/domain/list?tbl='+line+'\n'
        sign = hmac.new(secret_key, signingStr, digestmod=hashlib.sha1).hexdigest()
        encodedSign = qiniu.urlsafe_base64_encode(sign.decode('hex'))
        accessToken  =  access_key + ":" + encodedSign
        Authorization = 'QBox' + " " + accessToken
        headers = {"Host":"api.qiniu.com","Content-Type":"application/x-www-form-urlencoded","Authorization":Authorization}
        ret = requests.get(url,headers=headers)
        if ret is not None:
            you_list = json.loads(ret.content)
            for i in you_list:
                if 'clouddn' in i or 'qiniucdn' in i or 'qnssl' in i:
                    continue
                else:
                    print(i)
        else:
            print("error")


