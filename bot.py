import pywhatkit as pk
import pyautogui as pg
import time

with open('F:/MeuLabs/CODES/Whatsapp/royal.txt', 'r', encoding='utf-8') as file:
    message = file.read()

with open('F:/MeuLabs/CODES/Whatsapp/numbers_royal.csv', 'r') as file:
    numbers = file.readlines()

hrs = 14
mins = 5

for i, number in enumerate(numbers):
    phone = number.replace('\n', '')
    print(i, phone,"  ", end='')  

    if mins<60:
        mins = mins+1
    else:
        hrs = hrs+1
        mins = 1

    pk.sendwhatmsg(f"+{phone}","Howdy Little  Engineers🤩,\n\nHope you have revisited the lecture materials and made some circuits with TinkerCAD.\nYou can obtain the slides, code & recording of the sission from the following link:\nSession recording:\nhttps://us02web.zoom.us/rec/share/I637zKgHoGh8uDdsTed9Rf12BpwTjshR487MWXIWvlpjebiFKnfHo8aA0Kv95wwY.4Kn7p8hwea4BC6a2\nPasscode: aYUC6#q.\nSlides: https://www.canva.com/design/DAFjG-twn8o/41jtVovSL4wrBIhSm5zsTw/edit?utm_content=DAFjG-twn8o&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton\n\nWe at Meu Labs conduct project-based programs not only covering  Robotics but also Analytics, Software engineering, Creative Arts & many more.\n👨‍🔬🧑‍🎨🧑‍🔧👨‍💻\nYou can explore more on our courses from our site: https://meulabs.org/\n\nIn addition to that we have created many robust free/paid online courses, so you can gain valuable knowledge from the comfort of your home.\nLink: https://www.udemy.com/user/meulabs/\n\nKeep on exploring, keep on discovering but more importantly, keep on trying.\nHoping to meet you very soon.🤓\n\nFor More information or questions, please contact/message : +94719613500\n\n\n_This is an automated message, please reply to the given contact number above for any queries. Thanks_", hrs,mins,25,True,3)
    print("---> Success !")
    #time.sleep(3)
    #pg.hotkey('ctrl','w')
