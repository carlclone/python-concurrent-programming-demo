import requests
import json

main_url = 'http://210.4.101.11:8081/API/'

headers = {'Authorization': 'Basic QXBpVXNlckFkbWluOnBlc29xMjAxOA==',
           "Content-Type": 'application/json'}

# num =  s1.join('%s' %id for id in [8080]*32)
# port = s1.join('%s' %id for id in list(range(1,33)) )


data = '{"event": "txsms", "userid": "0", "num": "8080", "port": "1", "encoding": "0", "smsinfo": "STATUS"}'

r = requests.post(url=main_url + "SendSMS", headers=headers, data=data)
# data=json.dumps(data)
print (data)
print (r)
