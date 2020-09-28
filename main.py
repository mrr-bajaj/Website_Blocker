import  time
from datetime import datetime as dt


import os
from elevate import elevate

elevate()

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect ="127.0.0.1"

website_lists = ["www.facebook.com","facebook.com","www.instagram.com"]

flag= True

while flag:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours..")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_lists:
                if website in content:
                    flag=False
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_lists):
                    file.write(line)
            file.truncate()
            print("Fun Hours..")
            flag = False

    time.sleep(5)