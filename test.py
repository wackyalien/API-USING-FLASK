import requests
Base = "http://127.0.0.1:5000/"

data = [{"Likes":56,"Name":"kunal","Views":5210},
    {"Likes":56230,"Name":"cool","Views":21440},
    {"Likes":0,"Name":"Woow","Views":10}]



for i in range(len(data)):
    response = requests.put(Base+"video/" +str(i),data[i])
    print (response.json())

input()
response = requests.get(Base+"video/6")
print (response.json())
