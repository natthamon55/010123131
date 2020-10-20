import cv2
import numpy as np
import PySimpleGUI as sg 
from ball_pysim import *
from time import time
  
#color in hex
bt1 = {'size':(13,4), 'font':('Franklin Gothic Book', 20), 'button_color':("white",'#df6b77')}
bt2 = {'size':(13,2), 'font':('Franklin Gothic Book', 20), 'button_color':("white",'#df6b77')}

White = '#F8F8FF'
Black = '#000000'

sg.theme('DarkBlack')



def login():
    layout = [
            [sg.Text('ONE-TOUCH LOGIN', size=(40,3), justification='center', text_color='White', font=('Franklin Gothic Book', 50, 'bold'))],
            [sg.Text('--------', size=(35, 1), font=('Segoe UI', 14), text_color='Black'),sg.Text('PASSWORD :', size=(12, 1), font=('Segoe UI', 30), text_color='White'),sg.Input(key='-password-')],
            [sg.Text('--------', size=(22, 8), font=('Segoe UI', 14), text_color='Black')],
            [sg.Text('--------', size=(55, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('SUBMIT',**bt1)]
                
            ]

    window = sg.Window('OneTouch', layout ,auto_size_buttons=False, resizable=False).Finalize()
    window.Maximize()

    while True:
        button , value = window.read()
        password = value['-password-']

        if button == 'SUBMIT' :
            if password == '1234':
                sg.popup("Login SUCCESSFUL")
                main_menu()
                window.Close()
            else:
                sg.popup("Login FAILED!!")

        if button == sg.WIN_CLOSED:
            break

    window.Close()



def main_menu() :

    layout =[ 
            
            [sg.Text('ONE-TOUCH', size=(30,1), justification='center', text_color='White', font=('Franklin Gothic Book', 80, 'bold'))],
            [sg.Text('--------', size=(22, 8), font=('Segoe UI', 14), text_color='Black')],
            [sg.Text('--------', size=(45, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('START',**bt1),sg.Text('--------', size=(12, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('HOW TO PLAY ?',**bt1)] ,  
            [sg.Text('--------', size=(22, 2), font=('Segoe UI', 14), text_color='Black')]

            ]

    window = sg.Window('OneTouch', layout ,auto_size_buttons=False, resizable=False).Finalize()
    window.Maximize()

    while True:
        button , values = window.read()
        if button == "START" :
            game()
            window.Close()

        if button == "HOW TO PLAY ?" :
            sg.popup('Touch/Click the ball through the camera , When you tap it there will show your score with coundown timer :P')

        if button == sg.WIN_CLOSED :
            break

    window.close()


def game():

    global count_score

    #----------------open cv------------------#
    cap = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier(r'C:\software\haarcascade_frontalface_default.xml')
    cap.set(3, 1280)
    cap.set(4, 720)
    #-----------------------------------------#

    sg.theme('Black')

    # define the window layout
    layout = [
            [sg.Text('TIME : ', size=(10, 1), font=('Segoe UI', 20), text_color='White'),sg.Text('', size=(10, 1), font=('Helvetica', 22),text_color = 'White',key='timer'),
            sg.Button('Ball', size=(10, 1), font='Helvetica 14'),
            sg.Button('Exit', size=(10, 1), font='Helvetica 14') ],
            [sg.Text('SCORE : ', size=(10, 1), font=('Segoe UI', 20), text_color='White'),sg.Text('', size=(10, 1), font=('Helvetica', 22), text_color='White', key='score1')] ,
            [sg.T('                       ') , sg.Graph(canvas_size=(1280,720), graph_bottom_left=(0,0), graph_top_right=(400,400),key="canvas")]
            ]

    # create the window and show it without the plot
    window = sg.Window('OneTouch', layout, auto_size_buttons=False, resizable=False).Finalize() 
    window.maximize()  

    canvas = window['canvas']

    ball = ball_pysim(canvas)

    #-------score-------#
    count_score = 0

    #-----timer--------#
    timer_running = True  
    seconds = 64
    start = time()
    current = time()

    face_x , face_y = 0,0

    while True:

        #------------------- part openCV ----------------#
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)              # แปลงสีจากโหมด BGR เป็น GRAY เพื่อนำภาพไปใช้สำหรับ face detection

        faces = face_detector.detectMultiScale(gray, 1.1, 4)        # ทำการ dectect หน้าโดยจะให้ ตำแหน่ง x y ความยาว ความสูง

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            face_x , face_y = x, y
            print((x,y))

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        if  ball.is_collided(face_x, face_y) :
            canvas.DeleteFigure(circle)
            ball = ball_pysim(canvas)
            count_score += 1
            window['score1'].update(count_score)


        imgbytes = cv2.imencode('.png', frame)[1].tobytes()
        
        #------------------------------------------------#    
       
        canvas.DrawImage(data=imgbytes, location=(0, 400))

        circle = canvas.DrawCircle((ball.x, ball.y), ball.r, fill_color=ball.color, line_color='black')

        button, values = window.read(timeout=60)

         
        if button == 'Exit' :
            score()
        
        if  button == sg.WIN_CLOSED :
            break

        if button == 'Ball':
            canvas.DeleteFigure(circle)
            ball = ball_pysim(canvas)
            count_score += 1
            window['score1'].update(count_score)


        if timer_running: 
            current = time()
            timeleft = int(seconds - (current - start))
            window['timer'].update(timeleft)
            window.refresh()

            if timeleft == 0:
                sg.popup("TIME UP")
                score()
                window.Close() 
            
    window.close()
        

def score() :

    layout =[

                [sg.Text('ONE-TOUCH', size=(30,2), justification='center', text_color='White', font=('Franklin Gothic Book', 80, 'bold'))],
                [sg.Text('--------', size=(40, 3), font=('Segoe UI', 14), text_color='Black'),sg.Text('SCORE : ', size=(10, 2), font=('Segoe UI', 40), text_color='White'),sg.Text('', size=(12, 2), font=('Segoe UI', 40), text_color='White', key='score2')],   
                [sg.Text('--------', size=(60, 1), font=('Segoe UI', 14), text_color='Black'),sg.Button('RESTART',**bt2),sg.Text('--------', size=(5, 1), font=('Segoe UI', 14), text_color='Black')]

            ]

    window = sg.Window('OneTouch', layout ,auto_size_buttons=False, resizable=False).Finalize()
    window.Maximize()

    while True : 
        button , values = window.read(timeout=60)
           
        window['score2'].update(count_score)
                
        if button == "RESTART" :
            main_menu()
            window.Close()
            

        if button == sg.WIN_CLOSED :
            break

    window.close()
            
    
login()