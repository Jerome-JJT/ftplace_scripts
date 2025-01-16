
import sys
import time
import http.cookiejar
from http.cookiejar import Cookie
import requests, pickle
import random

from show import create_image
# cookie_jar = http.cookiejar.LWPCookieJar(".cookie_jar")
# host = "http://c1r14s2:6666/"
host = "http://c1r14s2:7979/"
host = "https://ftplace.42lwatch.ch/"

domain = "c1r14s2.local"
domain = "ftplace.42lwatch.ch"

cookie_file = '.custom_cookie_jar'

# cookie_jar = http.cookiejar.LWPCookieJar(".cookie_jar")
# try:
#     cookie_jar.load(ignore_discard=True)
# except FileNotFoundError:
#     print("No existing cookie file found. Creating a new one.")
    
session = requests.Session()
# session.cookies = cookie_jar

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
        
    session.cookies.set("token", token, path="/", domain=domain)
    session.cookies.set("refresh", refresh, path="/", domain=domain)
        

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


def make_get(url):
    global session
    
    response = session.get(url)
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
        
        response = session.get(url)
        return response

    elif (response.status_code == 401):
        print("401 Expired")
        ask_token()
        
        response = session.get(url)
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
    
    elif (response.status_code == 401):
        print("401 Expired")
        ask_token()
        
        response = session.post(url, json=data)
        return response
    else:
        return response
    

# token = input("Token: ")
# refresh = input("Refresh: ")

# c = Cookie(0, 'token', token, '', '', 'c1r14s2.local', 
#        None, None, '/', None, False, False, 'TestCookie', None, None, None)
# cookie_jar.set_cookie(c)
# cookie_jar.save(ignore_discard=True)

session.cookies.set("token", token, path="/", domain=domain)
session.cookies.set("refresh", refresh, path="/", domain=domain)

board = ''

def update_board():
    global board
    
    response = make_get(f"{host}api/get?type=board")


    # if (response.ok):

    print('basic', response.status_code)
    board = response.json()["board"]
    # print(response.json()["colors"])

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = {**board[i][j], "x": j, "y": i}

update_board()
# for i in range(40, 50):
#     s = ""
#     for j in range(40, 50):
#         s += str(board[j][i]["color_id"])

    # print(s)

# 42lwatch
destx = 149
desty = 53

# Wiiu
destx = 97
desty = 104

if (__name__ == "__main__"):
    if (len(sys.argv) > 1):
        if (sys.argv[1] == "1"):

            while (True):

                # print('deb', session.cookies)
                response = make_get(f"{host}api/profile")
                print('profile', response.status_code, response.json())
                time.sleep(30)
                
        elif (sys.argv[1] == "2" and len(sys.argv) > 2):
            
            startx = 29
            starty = 18
            sizex = 20
            sizey = 20
            
            with open(sys.argv[2], "w") as f:
                for i in range(starty, starty + sizey):
                    s = ""
                    for j in range(startx, startx + sizex):
                        s += chr(board[j][i]["color_id"] + ord('A'))
                        
                    print(f"{s}")
                    f.write(f"{s}\n")
                    
        
        elif (sys.argv[1] == "3" and len(sys.argv) > 2):

            changes = []
            with open(sys.argv[2], "r") as f:
                changes = f.readlines()

            nbchange = 0
            proof = []
            
            for n, i in enumerate(board):
                proof.append("")
                for m, j in enumerate(i):
                    proof[-1] += chr(board[m][n]['color_id'] + ord('A'))
                    
            
                    
            for n, i in enumerate(changes):
                for m, j in enumerate(i.strip()):
                    
                    idtodo = ord(changes[n][m]) - ord('A')
                    
                    if (idtodo != 0 and (n + desty) > 0 and (m + destx) > 0 and idtodo != proof[n + desty][m + destx]):
                        # proof[n + desty][m + destx] = changes[n][m]
                        nbchange += 1
                        proof[n + desty] = proof[n + desty][:m + destx] + changes[n][m] + proof[n + desty][m + destx + 1:]
            
            create_image(proof, 1, 'proof.png')
            print(nbchange, " TO CHANGE")
            
            

        elif (sys.argv[1] == "4" and len(sys.argv) > 2):

            changes = []
            with open(sys.argv[2], "r") as f:
                changes = f.readlines()

            while True:

                update_board()

                nbchange = 0
                proof = []
                
                for n, i in enumerate(board):
                    proof.append("")
                    for m, j in enumerate(i):
                        proof[-1] += chr(board[m][n]['color_id'] + ord('A'))

                orders = []

                for n, i in enumerate(changes):
                    for m, j in enumerate(i.strip()):
                        
                        idtodo = ord(changes[n][m]) - ord('A')
                        
                        if (idtodo != 0 and n + desty > 0 and m + destx > 0 and idtodo != proof[n + desty][m + destx]):
                            # proof[n + desty][m + destx] = changes[n][m]
                            
                            orders.append({"x": m + destx, "y": n + desty, "color": idtodo})
                
                print(nbchange, " TO CHANGE")
                
                while True:
                    
                    if (len(orders) <= 0):
                        break
                    
                    r = random.randrange(len(orders))
                    
                    print("DRAW", orders[r], 'rest', len(orders))
                    res = make_post(f"{host}api/set", orders[r])
                    
                    
                    print(res.status_code)
                    if (res.status_code == 425):
                        break
                    if (res.status_code == 201):
                        orders.pop(r)
                    
                    time.sleep(1)
                    
                print("Wait 300 seconds")
                time.sleep(300)

    
