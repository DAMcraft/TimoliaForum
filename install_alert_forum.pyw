import PySimpleGUI as sg
import os
import urllib.request
import requests
from bs4 import BeautifulSoup


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text('Please input your credentials for timolia.de')],
    [sg.Text('Username', size =(15, 1)), sg.InputText()],
    [sg.Text('Password', size =(15, 1)), sg.InputText()],
    [sg.Button('Installieren'), sg.Cancel()],
    [sg.Text('Nachdem man das Programm installiert, scheint das Programm zu laggen. \nDies tut es aber nicht, schließen sie das Fenster deswegen Bitte nicht.\nEs tut dies von alleine')]
]
  

# Create the Window
window = sg.Window('Setup vom TimoliaForum Benachrichtigungs Bot', layout).Finalize()
event, values = window.read()

appdata = os.getenv('appdata')
retry = True
         
while retry:
    if event == "Installieren":
        get_phpssid = "https://www.timolia.de:443/login"
        with requests.Session() as s:
            r = s.get(get_phpssid, headers={})
            phpssid = requests.utils.dict_from_cookiejar(s.cookies)['PHPSESSID']

        bsdoc = BeautifulSoup(r.content, 'html.parser')
        csrf = bsdoc.find("input", {"name":"_csrf_token"})['value']
        headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "Origin": "https://www.timolia.de", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://www.timolia.de/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7"}
        login=s.post("https://www.timolia.de:443/login_check", headers=  headers,cookies = {"hl": "de","PHPSESSID": phpssid}, data = {"_username": values[0], "_password": values[1], "_target_path": "https://www.timolia.de/", "_csrf_token": csrf, "_remember_me": "on"})
        if "hey "+values[0]+"!" in login.text: 
            try:
                os.mkdir(appdata+"\\timolia_forum")
            except:
                pass
            with open(appdata+"\\timolia_forum\\login.txt", "w") as o:
                o.write(values[0]+"\n"+values[1])
            print("Installing...")
            urllib.request.urlretrieve("https://github.com/DAMcraft/TimoliaForum/blob/main/main.exe?raw=true", appdata+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\TimoliaForum.exe")
            window.close()
            retry = False
        else: # If Password or user is wrong
            window.Close()
            layout = [
                [sg.Text('Falscher Benutzername oder Falsches Passwort.')],
                [sg.Button('Erneut versuchen'), sg.Cancel()]
            ]
            
            window = sg.Window('Setup vom TimoliaForum Benachrichtigungs Bot', layout).Finalize()
            event, eggs = window.read()
            if event == "Erneut versuchen":
                layout = [
                    [sg.Text('Please input your credentials for timolia.de')],
                    [sg.Text('Username', size =(15, 1)), sg.InputText()],
                    [sg.Text('Password', size =(15, 1)), sg.InputText()],
                    [sg.Button('Installieren'), sg.Cancel()],
                    [sg.Text('Nachdem man das Programm installiert, scheint das Programm zu laggen. \nDies tut es aber nicht, schließen sie das Fenster deswegen Bitte nicht.\nEs tut dies von alleine')]
                ]
                

                # Create the Window
                window = sg.Window('Setup vom TimoliaForum Benachrichtigungs Bot', layout).Finalize()
                event, values = window.read()
                retry = True
            else:
                retry = False
         
    else: 
        window.close()
        retry = False
