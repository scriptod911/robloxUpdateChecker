import requests
import time

def writeVersionToFile(version):
    f = open("versions.txt", "w")
    f.write(version)

def readVersionsFile():
    f = open('versions.txt', 'r')
    return f.read()


url = 'http://setup.roblox.com/version'
res = requests.get(url)


while res.status_code == 200:
    if res.text == readVersionsFile():
        print("No updates")
        time.sleep(60)
    
    else:
        print("Update found! update: {0}".format(res.text))
        writeVersionToFile(res.text)
        time.sleep(60)
