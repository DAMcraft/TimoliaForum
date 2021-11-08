timoliauser = "timoliauser"
timoliapwd = "timoliapass"

import os

appdata = os.getenv('appdata')
if timoliauser == "timoliauser" and timoliapwd == "timoliapass" and os.path.isfile(appdata+"\\timolia_forum\\login.txt"):
    with open(appdata+"\\timolia_forum\\login.txt", "r") as o:
      lines = o.read().splitlines()
      timoliauser = lines[0]
      timoliapwd = lines[1]
         


import webbrowser
import requests 
from bs4 import BeautifulSoup
import json
import time
from win10toast_click  import ToastNotifier
import urllib.request
import random
from PIL import Image

class Error(Exception):
    pass

def open_url():
    try: 
        webbrowser.open_new("https://forum.timolia.de/account/alerts")
        print('Opening URL...')  
    except: 
        print('Failed to open URL. Unsupported variable type.')
class timolia:

  def __init__(self, user, pwd):
    self.username = user
    self.password = pwd
    self.subrefferer = ""

    get_phpssid = "https://www.timolia.de:443/login"
    with requests.Session() as s:
        r = s.get(get_phpssid, headers={})
        phpssid = requests.utils.dict_from_cookiejar(s.cookies)['PHPSESSID']
        self.phpssid = phpssid
    bsdoc = BeautifulSoup(r.content, 'html.parser')
    csrf = bsdoc.find("input", {"name":"_csrf_token"})['value']
    self.csrf = csrf
    headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "Origin": "https://www.timolia.de", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://www.timolia.de/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"}
    login=s.post("https://www.timolia.de:443/login_check", headers=  headers,cookies = {"hl": "de","PHPSESSID": phpssid}, data = {"_username": user, "_password": pwd, "_target_path": "https://www.timolia.de/", "_csrf_token": csrf, "_remember_me": "on"})
    if "hey "+user+"!" in login.text: 
      print("successfully logged into timolia!")
      remember_me = requests.utils.dict_from_cookiejar(s.cookies)['remember_me']
    else:
      raise Error("Couldn't log into timolia as "+timoliauser)
    headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.timolia.de/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"}
    get_xfuser_token = requests.get("https://www.timolia.de:443/api/forum_login", cookies={"PHPSSID":phpssid, "remember_me":remember_me}, headers=headers)
    if "success" in get_xfuser_token.text:
        print("successfully got token 1")
        uid = json.loads(get_xfuser_token.text)["id"]
        token1 = json.loads(get_xfuser_token.text)["token"]
    else:
      raise Error("Couldnt get token 1")
    headers = {"GET /symfonysso.php?userid=55795&token=93239604461880816c132b2.59941620&noredirect=1&host=http": "/www.timolia.de HTTP/2", "Sec-Ch-Ua": "\"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"", "Accept": "*/*", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://www.timolia.de", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.timolia.de/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"}
    session2 = requests.Session()

    get_xfuser = session2.get("https://forum.timolia.de:443/symfonysso.php?userid="+str(uid)+"&token="+token1+"&noredirect=1&host=http://www.timolia.de", headers=headers)
    if "success" in get_xfuser.text:
      xf_user = session2.cookies.get_dict()["xf_user"]
      print("Logged into TIMOLIA FORUM, xf_user = "+xf_user)
    else:
          raise Error("Couldn't log into Forum")
    session3 = requests.session()
    #Xf Token is no longer used. I will still leave this here just in case
    headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://forum.timolia.de/account/alerts", "Accept-Encoding": "gzip, deflate", "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7", "If-Modified-Since": "Sun, 07 Nov 2021 18:38:08 GMT"}
    get_xf_token = session3.get("https://forum.timolia.de:443/account/", headers=headers, cookies = {"xf_user": "55795%2C3a038a07a26d3f519e49a481b4b1c9c515c84d4e"})
    bsdoc2 = BeautifulSoup(get_xf_token.text, 'html.parser')
    xf_token = bsdoc2.find("a", {"class":"LogOut primaryContent"})["href"].split('xfToken=')[1]
    get_notifs(xf_user, xf_token)


def get_notifs(xf_user, xf_token):
    # I use another request now, xf_token is useless and the format is better
    # headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"", "Accept": "application/json, text/javascript, */*; q=0.01", "X-Ajax-Referer": "https://forum.timolia.de/account/alerts", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://forum.timolia.de/account/alerts", "Accept-Encoding": "gzip, deflate", "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"}
    # get_notifs = requests.get("https://forum.timolia.de:443/account/alerts-popup?&_xfRequestUri=%2Faccount%2Falerts&_xfNoRedirect=1&_xfToken="+xf_token+"&_xfResponseType=json", headers=headers,cookies = {"xf_user": xf_user})
    # print(get_notifs.text)
    while True:
          headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://forum.timolia.de/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7", "If-Modified-Since": "Mon, 08 Nov 2021 13:10:01 GMT"}
          get_new_notif = requests.get("https://forum.timolia.de:443/account/alerts", cookies={"xf_user": xf_user}, headers=headers)
          bsdoc3 = BeautifulSoup(get_new_notif.text, 'html.parser')
          notif = bsdoc3.find("li", class_="primaryContent new")
          if not notif == None:
              notif_id = notif["id"]
              notif_img = notif.a.img["src"]
              tempdir = os.getenv('temp')
              if not os.path.isfile(tempdir+"\\timolia_already_alertet.txt"):
                    with open(tempdir+"\\timolia_already_alertet.txt", "w") as z:
                      z.write("")
              with open(tempdir+"\\timolia_already_alertet.txt", "r") as f:
                if notif_id not in f.read():
                  notif_text = notif.div.h3.text.strip()
                  with open(tempdir+"\\timolia_already_alertet.txt", "a") as a:
                    a.write(notif_id+"\n")
                  print(notif_text)
                  n = str(random.randint(0,100000000000))
                  urllib.request.urlretrieve(notif_img, tempdir+"\\"+n+".png")
                  filename = r''+tempdir+"\\"+n
                  img = Image.open(filename+".png")
                  img.save(filename+".ico")
                  ToastNotifier().show_toast("New Alert on the Timolia Forum!",notif_text,duration=20,icon_path=tempdir+"\\"+n+".ico", callback_on_click=open_url)


          time.sleep(10)

login=timolia(timoliauser,timoliapwd)
# print(login.phpssid)