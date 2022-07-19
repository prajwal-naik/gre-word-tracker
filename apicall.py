import requests


def checkResult(res):
    return type(res) == list

def makeGetRequest(url, word):
    return requests.get(url + word).json()
