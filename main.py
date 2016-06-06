#importando las funciones
from flask import Flask, render_template
from colorlabeler import ColorLabeler
from random import randint
import time
import winsound
import argparse
import imutils
import cv2
import numpy
import serial
from bokeh.core.compat.mplexporter.renderers.base import Renderer
from pycparser.c_ast import Switch
from nose import case

#Variables
app = Flask(__name__)
matrix=[[0,0,0],[0,0,0],[0,0,0]]
port=1
frames=0
numblocks=0

#Functions
def getrow():
    return randint(0,2)

def getcol():
    return randint(0,2)
   
def fillmatrix(n):
    i=1
    while i<=n: 
        r=getrow()
        f=getcol()
        if matrix[r][f]!=1:
            matrix[r][f]=1
            i=i+1

def matrixcolor(r,g,b):
    i=1
    for i in range(0,3):
        for j in range(0,3):
            aleatory=randint(0,3)
            matrix[i][j]=1
        
        
def resetmatrix():
        for i in range(0,3):
            for j in range(0,3):
                matrix[i][j]=0

def buildstring():
    allcoordinates=""
    for i in range(0,3):
        for j in range(0,3):
            if(matrix[i][j])==1:
                allcoordinates+="f"+str(i)+"c"+str(j)+"_"
    return allcoordinates
        
def printmatrix():
    for i in range(0,3):
        for j in range(0,3):
            print("Matriz["+str(i)+"]["+str(j)+"]="+str(matrix[i][j]))

def playaudio(aud):
    winsound.PlaySound(aud,winsound.SND_FILENAME)

def captureimage():
    camera=cv2.VideoCapture(port)
    retval, image=camera.read()
    return image

def saveimage(name):
    for i in xrange(frames):
        temp=captureimage()
    print ("Taking image...")
    camcapture=captureimage()
    file="img/"+name+".png"
    cv2.imwrite(file,camcapture)
    print ("Imagen is saved")
       
def cutimage(player,original,edited):
    imageoriginal="img/"+original+".png"
    imageedited="img/"+edited+".png"
    img=cv2.imread(imageoriginal)
    if player=="com":
        tmp=img[150:340, 35:225]        
        cv2.imwrite(imageedited,tmp)        
    elif player=="player":
        tmp=img[150:340, 400:600]
        cv2.imwrite(imageedited,tmp)
    cv2.imshow("Cut Image", tmp)
    cv2.waitKey(0)
    
def countcotours(img):
    nc=0
    dir="img/"+img+".png"
    image = cv2.imread(dir)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
 
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]      
    
    for c in cnts:
    # compute the center of the contour
        if cv2.contourArea(c)<100:
            continue
        else:
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"]) 
            cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
            cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(image, "center", (cX - 20, cY - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            nc=nc+1 
            #cv2.imshow("Image", image)
            #cv2.waitKey(0) 
    return nc

def findcolors(nc,im):
    cont=0
    image = cv2.imread(im)
   
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
    thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]
 
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    
    cl = ColorLabeler()
    
    for c in cnts:
        if cv2.contourArea(c)> 150:
            M = cv2.moments(c)
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
     
            #shape = sd.detect(c)
            color = cl.label(lab, c)
            if color==nc:
                text = "{}".format(color)
                cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
                cv2.putText(image, text, (cX, cY),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                cont=cont+1
                cv2.imshow("Image", image)
                cv2.waitKey(0)
    return cont

def getnumber():
    return randint(1,9)

#Views

@app.route("/")
def index():
    return render_template('inicio.html')

@app.route("/act01m1")
def iniciar():
    #resetmatrix()
    #numblocks=getnumber()
    numblocks=9
    #fillmatrix(numblocks)
    #printmatrix()
    #cad=buildstring()
    #print(cad)
    #printmatrix()
    #Enviar Cadena a Arduino
    return render_template('act01m1.html',timetoway=numblocks)

@app.route('/rvoz1')
def rvoz1():
    #captureimage()
    #saveimage("com","a1m1com")
    cutimage("com","a1m101","a1m1com01")
    numblockscom=countcotours("a1m1com01")
    #print("Numero de Bloques COM:"+str(numblockscom))
    return render_template('rvoz1.html',numblockscom=numblockscom)

#Verificar tablero Jugador
@app.route('/rcam1')
def rcam1():
    #captureimage()
    #saveimage("a1m1player1")
    cutimage("com","a1m101","a1m1com01")
    cutimage("player","a1m101","a1m1player01")
    playernumblocks=countcotours("a1m1player01")
    comnumblocks=countcotours("a1m1com01")
    #print("Numero de Bloques PLAYER:"+str(playernumblocks))
    #print("Numero de Bloques COM   :"+str(comnumblocks))
    if(playernumblocks!=0):
        if(playernumblocks!=comnumblocks):
            useractivity="failure"
        else:
            if (playernumblocks==comnumblocks):
                useractivity="success"
            else:
                useractivity="error"
    else:
        useractivity="empty"      
    return render_template("rcam1.html",useractivity=useractivity,nblockstoput=comnumblocks)

@app.route("/act01m2")
def act01m2():
    return render_template('act01m2.html')

@app.route("/rcam2")
def rcam2():
    #captureimage()
    #saveimage("a1m2player")
    cutimage("player","a1m201","a1m2player")
    nblocks=countcotours("a1m2player")
    #resetmatrix();
    #fillmatrix(nblocks)
    #printmatrix()
    #cad=buildstring()
    #Pasar a Arduino
    #print("Numero de Bloques Player01: "+str(nblocks))
    return render_template("rcam2.html",a1m2nbplayer=nblocks)
    
@app.route("/act02m1")    
def act02m1():
    n=getnumber()
    #print("Number: "+str(n))
    sw=False
    #print(sw)
    while(sw!=True):
        #print(sw)
        r=randint(1,3)
        g=randint(1,3)        
        b=randint(1,3)
        total=r+g+b
        if total==n:
            xy=str("B_")+str(r)+str(g)+str(b)+"#"
            sw=True
            print("Enviar a Arduino-COM"+str(xy))
            #print(sw)
            #print("Green: "+str(green))
            #print("Red  : "+str(red))    
    return render_template("act02m1.html",nbrCOM=r,nbgCOM=g,nbbCOM=b)

#@app.route("/on")
#def on():
    #ser = serial.Serial('COM6')
    #time.sleep(1.8) 
    #print(ser.name)
    #ser.write('1')
    #ser.close()
    #return "Led encendido"
    
#@app.route("/off")
#def off():
    #ser = serial.Serial('COM6')
    #print(ser.name)
    #ser.write('2'.encode())
    #ser.close()
    #return "Led apagado"

if __name__ == "__main__":
    app.run(host='192.168.1.3')


