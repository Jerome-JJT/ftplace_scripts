
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
host = "https://ftplace.42lausanne.ch/"

domain = "c1r14s2.local"
domain = "ftplace.42lwatch.ch"
domain = "ftplace.42lausanne.ch"

cookie_file = '.custom_cookie_jar' + (sys.argv[5] if len(sys.argv) >= 6 else '')
print(cookie_file)
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
#         s += str(board[j][i]["c"])

    # print(s)

# 42lwatch
# destx = 149
# desty = 53

# Wiiu
# destx = 97
# desty = 104

# qr
# destx = 229
# desty = 0

# orange
# destx = 131
# desty = 104

# blue
# destx = 61
# desty = 122

# blue new
# destx = 68
# desty = 122

# threads new
# destx = 91
# desty = 26

# majora ABORT
# destx = 180
# desty = 180

# tardis combo
# destx = -8
# desty = 19

# destx = 126
# desty = 59

# smash
# destx = 200
# desty = 80

# luma
# destx = 133
# desty = 55
# destx = 192
# desty = 14

#pochita test
# destx = 190
# desty = 10

# Sword
# destx = 50
# desty = 139

# # luma up gauche
# destx = 15
# desty = 36


# # # pochita middle
# destx = 116
# desty = 16



# python script.py 3 converted_pyra3.txt 007 007 jja
# python script.py 3 converted_Vincent_bg.txt 007 007 firsto
# python script.py 3 converted_kngiht.txt 007 007 seco
# python script.py 3 converted_dofus.txt 007 007 thir
# python script.py 3 converted_pixel_zss2.txt 007 007 quact

# python script.py 3 converted_link.txt 007 007 servfir
# python script.py 3 converted_mona.txt 007 007 servdos
# python script.py 3 converted_charmender.txt 007 007 serthir






# chomo
if "pyra" in sys.argv[2]:
    destx = 126
    desty = 232
elif "Vinc" in sys.argv[2]:
    destx = 300
    desty = 10
elif "kng" in sys.argv[2]:
    destx = 100
    desty = 350
elif "dofu" in sys.argv[2]:
    destx = 250
    desty = 100
elif "zss" in sys.argv[2]:
    destx = 300
    desty = 50
elif "link" in sys.argv[2]:
    destx = -15
    desty = 232
elif "mona" in sys.argv[2]:
    destx = 500
    desty = 250
elif "char" in sys.argv[2]:
    destx = 250
    desty = 300
elif "sans2" in sys.argv[2]:
    destx = 335
    desty = 80
elif "cutheart" in sys.argv[2]:
    destx = 20
    desty = 266
else:
    destx = 0
    desty = 0





order = False


if (__name__ == "__main__"):
    if (len(sys.argv) > 1):
        if (sys.argv[1] == "1"):

            while (True):

                # print('deb', session.cookies)
                response = make_get(f"{host}api/profile")
                print('profile', response.status_code, response.json())
                time.sleep(30)
                
        elif (sys.argv[1] == "2" and len(sys.argv) > 2):
            
            startx = 91
            starty = 26
            sizex = 32
            sizey = 32
            
            with open(sys.argv[2], "w", encoding="utf8") as f:
                for i in range(starty, starty + sizey):
                    s = ""
                    for j in range(startx, startx + sizex):
                        s += chr(board[j][i]["c"] + ord('A'))
                        
                    print(f"{s}")
                    f.write(f"{s}\n")
                    
        
        elif (sys.argv[1] == "3" and len(sys.argv) > 2):

            changes = []
            with open(sys.argv[2], "r", encoding="utf8") as f:
                changes = f.readlines()

            nbchange = 0
            proof = []
            
            for n, i in enumerate(board):
                proof.append("")
                for m, j in enumerate(i):
                    proof[-1] += chr(board[m][n]['c'] + ord('A'))
                    
            
                    
            for n, i in enumerate(changes):
                for m, j in enumerate(i.strip()):
                    
                    idtodo = ord(changes[n][m]) - ord('A')
                    
                    if (idtodo != 0 and (n + desty) >= 0 and (m + destx) >= 0 and chr(idtodo + ord('A')) != proof[n + desty][m + destx]):
                        # proof[n + desty][m + destx] = changes[n][m]

                        if changes[n][m] == 'Z':
                            continue
                        nbchange += 1
                        proof[n + desty] = proof[n + desty][:m + destx] + changes[n][m] + proof[n + desty][m + destx + 1:]
            
            create_image(proof, 1, f'proof_{sys.argv[2][:sys.argv[2].find(".")]}.png')
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
                        proof[-1] += chr(board[m][n]['c'] + ord('A'))

                orders = []

                for n, i in enumerate(changes):
                    for m, j in enumerate(i.strip()):
                        
                        if changes[n][m] == 'Z':
                            continue
                        idtodo = ord(changes[n][m]) - ord('A')
                        
                        if (idtodo != 0 and n + desty > 0 and m + destx > 0 and chr(idtodo + ord('A')) != proof[n + desty][m + destx]):
                            # proof[n + desty][m + destx] = changes[n][m]
                            
                            nbchange += 1
                            orders.append({"x": m + destx, "y": n + desty, "color": idtodo})
                
                print(nbchange, " TO CHANGE")
                
                while True:
                    
                    if (len(orders) <= 0):
                        break
                    
                    r = random.randrange(len(orders))
                    if order == True:
                        r = 0
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

    
