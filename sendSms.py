import requests


filename = 'phones.txt'
text ='عید نوروز مبارک!'
  
def readphones(filename):
    with open(filename) as f:
        content = f.readlines()
        
    content = [x.strip() for x in content]
    return content

def sendSms(number,text):
    api_key = '#your_API_KEY'
    url = 'https://api.kavenegar.com/v1/%s/sms/send.json' %api_key
    data = {'receptor': number,'message':text}
    r = requests.post(url, data=data)
    return r.ok

phones = readphones(filename)
for phone in phones:
    if not sendSms(phone, text):
        print(phone)