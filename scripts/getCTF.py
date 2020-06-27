import requests
import time

start = time.time()
start = int(start)
finish = start + 2678400

start = str(start)
finish = str(finish)

# print("epoch current time = ", epoch)

url = "https://ctftime.org/api/v1/events/?limit=100&start={}&finish={}".format(start,finish)
print(url)


# 1 weeks in epoch = 604800
# 1 month in epoch = 2678400

def main(url):
    	
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'}

    response = requests.get(url,headers=headers)
    content = response.json()
    for i in content:
        for key,value in i.items():
            print(key ," => ", value)



main(url)