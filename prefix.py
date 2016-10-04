import requests
import json

def initialPost():
    url = 'http://challenge.code2040.org/api/prefix'
    payload = {'token':'f13b411e75521c7338e9e553d0c197e9'}
    original = requests.post(url, params=payload)
    return original.json()

def finalPost(array):
    url = 'http://challenge.code2040.org/api/prefix/validate'
    payload = {'token':'f13b411e75521c7338e9e553d0c197e9', 'array':array}
    original = requests.post(url, json=payload)

def hasPrefix(array, prefix):
    prefixLength = len(prefix)
    arrayLength = len(array)
    newArray = []
    count = 0

    for ix in range(0, arrayLength):
        curItem = array[ix]
        if(prefix != curItem[0:prefixLength]):
            newArray.append(curItem)
        count += 1
    return newArray

############################ Main ############################

prefixAndArray = initialPost()

prefix = prefixAndArray['prefix']
originalArray = prefixAndArray['array']

prefixArray = hasPrefix(originalArray, prefix)

print(prefix)
print(originalArray)
print(prefixArray)

finalPost(prefixArray)
