import os
import sys
import time
import http.cookiejar
from http.cookiejar import Cookie
import requests, pickle
import random
from functools import *
import shutil
import datetime
import imageio
import glob

from show import create_image
# host = "http://c1r14s2:6666/"
host = "http://c1r14s2:7979/"
# host = "https://ftplace.42lwatch.ch/"

domain = "c1r14s2.local"
# domain = "ftplace.42lwatch.ch"

cookie_file = '.custom_cookie_jar'
    
session = requests.Session()

token = ''
refresh = ''

def ask_token():
    global token
    global refresh
    
    token = input("Token: ")
    refresh = input("Refresh: ")
    
    with open(cookie_file, "w") as custom_cookie_jar:
        custom_cookie_jar.write(f"{token}\n")
        custom_cookie_jar.write(f"{refresh}\n")
        

try:
    with open(cookie_file, "r") as custom_cookie_jar:
        lines = custom_cookie_jar.readlines()
        
        if (len(lines) != 2):
            print("Cookie file len ", len(lines))
            ask_token()
        else:
            token = lines[0].strip()
            refresh = lines[1].strip()

except FileNotFoundError:
    print("File not found")
    ask_token()


def make_get(url, stream=False):
    global session
    
    print("REQ", url)
    response = session.get(url, stream=stream)
    if (response.status_code == 426):
        print('refresh 426')
        
        token = response.cookies["token"]
        refresh = response.cookies["refresh"]
        
        with open(cookie_file, "w") as custom_cookie_jar:
            custom_cookie_jar.write(f"{token}\n")
            custom_cookie_jar.write(f"{refresh}\n")
            
        session.cookies.set("token", token, path="/", domain=domain)
        session.cookies.set("refresh", refresh, path="/", domain=domain)
        
        response = session.get(url, stream=stream)
        return response
    
    else:
        return response
    
    
def make_post(url, data):
    global session
    
    response = session.post(url, json=data)
    if (response.status_code == 426):
        print('refresh 426')
        
        # print(session.cookies["token"], response.cookies["token"])
        
        token = response.cookies["token"]
        refresh = response.cookies["refresh"]
        
        with open(cookie_file, "w") as custom_cookie_jar:
            custom_cookie_jar.write(f"{token}\n")
            custom_cookie_jar.write(f"{refresh}\n")
            
        session.cookies.set("token", token, path="/", domain=domain)
        session.cookies.set("refresh", refresh, path="/", domain=domain)
        
        response = session.post(url, json=data)
        return response
    
    else:
        return response


session.cookies.set("token", token, path="/", domain=domain)
session.cookies.set("refresh", refresh, path="/", domain=domain)

board = ''

def get_board(time):
    global board
    
    response = make_get(f"{host}api/getimage?time={time}", stream=True)
    filename = time.replace("-", "_").replace(":", "_").replace(".", "_")

    os.makedirs("imgs", exist_ok=True)
    
    print(response.status_code)
    if (response.ok):
        with open(f'imgs/{filename}.png', 'wb') as out_file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, out_file)
            


    
destx = 149
desty = 53

if (__name__ == "__main__"):
    if (len(sys.argv) > 1):
        if (sys.argv[1] == "1"):

            while (True):

                # print('deb', session.cookies)
                response = make_get(f"{host}api/profile", stream=True)
                print('profile', response.status_code, response.json())
                time.sleep(30)
                
        elif (sys.argv[1] == "2"):
            starttime = datetime.datetime.fromisoformat('2025-01-15T16:00:00.000000')
            endtime = datetime.datetime.fromisoformat('2025-01-16T13:41:17.356715')

            while starttime < endtime:
                print("GET ", starttime.isoformat())
                get_board(starttime.isoformat())
                
                starttime += datetime.timedelta(hours=1)
                
                time.sleep(1)

        elif (sys.argv[1] == "3"):
            images = []
            for filename in glob.glob('imgs/*.png'):
                images.append(imageio.imread(filename))
            imageio.mimsave('res.gif', images)

    
