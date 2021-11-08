import PySimpleGUI as sg
import os
import urllib.request

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

         

if event == "Installieren":
    try:
        os.mkdir(appdata+"\\timolia_forum")
    except:
        pass
    with open(appdata+"\\timolia_forum\\login.txt", "w") as o:
        o.write(values[0]+"\n"+values[1])
    print("Installing...")
    urllib.request.urlretrieve("https://github.com/DAMcraft/TimoliaForum/blob/main/main.exe?raw=true", appdata+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\TimoliaForum.exe")
    window.close()
else: 
    window.close()