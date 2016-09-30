import requests
import json

def initialPost():
    url = 'http://challenge.code2040.org/api/haystack'
    payload = {'token':'f13b411e75521c7338e9e553d0c197e9'}
    original = requests.post(url, params=payload)
    return original.json()

def finalPost(idx):
    url = 'http://challenge.code2040.org/api/haystack/validate'
    payload = {'token':'f13b411e75521c7338e9e553d0c197e9', 'needle':idx}
    original = requests.post(url, params=payload)

def findNeedle(target, collection):
    count = 0
    for k in haystack:
        if (target == k):
            return count
        count = count + 1
    return count

############################ Main ############################

needleHaystack = initialPost()

needle = needleHaystack['needle']
haystack = needleHaystack['haystack']

needleIdx = findNeedle(needle, haystack)

finalPost(needleIdx)
