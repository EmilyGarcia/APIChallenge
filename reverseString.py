import requests

def reverseString(original):
    reversed = "";
    for ix in range(len(original)):
        reversed = original[ix] + reversed
    return reversed

url = 'http://challenge.code2040.org/api/reverse'
payload = {'token':'f13b411e75521c7338e9e553d0c197e9'}
original = requests.post(url, params=payload) #stores original string

reversed = reverseString(original.text) #stores reversed string
url = 'http://challenge.code2040.org/api/reverse/validate'
payload = {'token':'f13b411e75521c7338e9e553d0c197e9', 'string':reversed}
requests.post('http://challenge.code2040.org/api/reverse/validate', params=payload)
