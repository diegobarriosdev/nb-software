#importando las funciones
from flask import Flask, render_template
from colorlabeler import ColorLabeler
from shapedetector import ShapeDetector
from random import randint
import time
import winsound
import argparse
import imutils
import cv2
import numpy
import serial
from bokeh.core.compat.mplexporter.renderers.base import Renderer


#Variables
app = Flask(__name__)
matrix=[[0,0,0],[0,0,0],[0,0,0]]
port=1
frames=0
numblocks=0
arduino=None


def sendToArduino(dat):
    arduino = serial.Serial("COM4", 9600)   
    time.sleep(2)
    arduino.write(dat)
    arduino.close()
    
#Functions
def playaudio(aud):
    winsound.PlaySound(aud,winsound.SND_FILENAME)

def imagepath(i):
    return "img/"+i+".png"

def captureimage():
    camera=cv2.VideoCapture(port)
    retval, image=camera.read()
    return image

def saveimage(name):
    for i in xrange(frames):
        temp=captureimage()
    #print("Taking image...")
    camcapture=captureimage()
    file="img/"+name+".png"
    cv2.imwrite(file,camcapture)
    #print("Imagen is saved")
       
def cutimage(player,original,edited):
    imageoriginal="img/"+original+".png"
    imageedited="img/"+edited+".png"
    img=cv2.imread(imageoriginal)
    if player=="player":
        tmp=img[50:235, 80:270]        
        cv2.imwrite(imageedited,tmp)        
    elif player=="com":
        tmp=img[30:250, 410:640]
        cv2.imwrite(imageedited,tmp)
    cv2.imshow("Cut Image", tmp)
    cv2.waitKey(0)
    
def countcotours(img):
    nc=0
    dir="img/"+img+".png"
    image = cv2.imread(dir)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image", gray)    
    cv2.waitKey(0) 
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imshow("Image", blurred)    
    cv2.waitKey(0) 
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("Image", thresh)    
    cv2.waitKey(0) 
    
            
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]      
    sd = ShapeDetector()
    
    for c in cnts:
    # compute the center of the contour
        if cv2.contourArea(c)<800:
            continue
        else:
            M = cv2.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            shape = sd.detect(c) 
            #if(shape=="square" or shape=="rectangle"):
            if 1==1:
                cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
                cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
                cv2.putText(image, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                nc=nc+1 
            cv2.imshow("Image", image)
            cv2.waitKey(0) 
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
    sd = ShapeDetector()
    
    for c in cnts:
        if cv2.contourArea(c)< 800:
            continue
        else:
            M = cv2.moments(c)
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            shape = sd.detect(c)
            color = cl.label(lab, c)
            print(shape)
            print(color)
           
            if (shape=="square" or shape=="rectangle"):
                if (color==nc):
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


@app.route("/")
def index():
    #captureimage()
    #saveimage("prueba")
    #cutimage("player","prueba","player1")
    #cutimage("com","prueba","computer")
    return render_template('inicio.html') 
 

@app.route("/stg-a1-01")
def stgAct101():
    nbCOM=getnumber()
    dat='A'+str(nbCOM)+'#'
    sendToArduino(dat)
    print("Numero Enviado: "+str(nbCOM))
    return render_template('stg-a1-01.html',nbCOM=nbCOM)

@app.route("/rvoz-a1-01")
def stgAct102():
    captureimage()
    saveimage("originala101")
    cutimage("com","originala101","a1m1com")
    nbCOM=countcotours("a1m1com")
    return render_template('rvoz-a1-01.html',nbCOM=nbCOM)

#Verificar tablero Jugador
@app.route("/rcam-a1-01")
def stgAct103():
    captureimage()
    saveimage("originala101")
    cutimage("com","originala101","a1m1com")
    cutimage("player","originala101","a1m1player")
    nbPlayer=countcotours("a1m1player")
    nbCom=countcotours("a1m1com")
    print("COM B:"+str(nbCom))
    print("PLA B:"+str(nbPlayer))
    return render_template("rcam-a1-01.html",nbCOM=nbCom,nbPlayer=nbPlayer)

@app.route("/stg-a1-02")
def stgAct104():
    return render_template('stg-a1-02.html')

@app.route("/rcam-a1-02")
def stgAct105():
    captureimage()
    saveimage("originala102")
    cutimage("player","originala102","a1m2player")
    nbPlayer=countcotours("a1m2player")
    dat='A'+str(nbPlayer)+'#'
    print(dat)
    sendToArduino(dat)
    return render_template("rcam-a1-02.html",nbPlayer=nbPlayer)
    
@app.route("/stg-a2-01")    
def stgAct201():
    n=getnumber()
    sw=False
    while(sw!=True):
        r=randint(1,3)
        g=randint(1,3)        
        b=randint(1,3)
        t=r+g+b
        if t==n:
            xy='B'+str(r)+str(g)+str(b)+'#'
            sw=True
            print("Enviar a Arduino-COM"+str(xy))
            sendToArduino(xy)
    return render_template("stg-a2-01.html",tbCom=t)

@app.route("/stg-a2-02")
def stgAct202():
    captureimage()
    saveimage("originala201")  
    cutimage("com","originala201","coma2m1")
    rc=findcolors("red",imagepath("coma2m1"))   
    return render_template("stg-a2-02.html",rc=rc)

@app.route("/stg-a2-03")
def stgAct203():
    captureimage()
    saveimage("originala201")
    cutimage("com","originala201","coma2m1")
    gc=findcolors("green",imagepath("coma2m1"))
    return render_template("stg-a2-03.html",gc=gc)

@app.route("/stg-a2-04")
def stgAct204():
    captureimage()
    saveimage("originala201")
    cutimage("com","originala201","coma2m1")
    bc=findcolors("blue",imagepath("coma2m1"))
    return render_template("stg-a2-04.html",bc=bc)

@app.route("/stg-a2-05")
def stgAct205():
    return render_template("stg-a2-05.html")

@app.route("/stg-a2-06")
def stgAct206():
    rc=0
    gc=0
    bc=0
    rp=0
    gp=0
    bp=0
    captureimage()
    saveimage("originala202")
    cutimage("com","originala202","coma2m2")
    cutimage("player","originala202","playera2m2")
    rc=findcolors("red",imagepath("coma2m2"))
    gc=findcolors("green",imagepath("coma2m2"))
    bc=findcolors("blue",imagepath("coma2m2"))
    rp=findcolors("red",imagepath("playera2m2"))
    gp=findcolors("green",imagepath("playera2m2"))
    bp=findcolors("blue",imagepath("playera2m2"))
    return render_template("stg-a2-06.html",rc=rc,gc=gc,bc=bc,rp=rp,gp=gp,bp=bp)

@app.route("/stg-a2-07")
def stgAct207():
    return render_template("stg-a2-07.html")

 
if __name__ == "__main__":
    app.run(host='172.15.34.216')