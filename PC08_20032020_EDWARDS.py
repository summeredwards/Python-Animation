#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:25:24 2020

@author: summeredwards
"""
#====================

# PC08 - SOUND WAVE

# Summer Edwards

# 03/20/2020

# this code creates an animation of moving planets and stars, while also displaying fun 
# waves in the background

#====================

# import modules 
import pygame 
from random import *  
import math

pygame.init()

# set varibales 
screen = pygame.display.set_mode((800,800))

run = True 

radius1 = 300
radius2 = 100
radius3 = 150
frequency = 11
amplitude = randint(2,20) 
speed = 1
x = 200
z = 700
w = 300
v = 0
b = -50
step = 5

black = (0,0,0)
lilac = (205,153,235)
bbyPink = (245,216,245)
bbyOrange = (245,225,216)
peach = (255,204,204)
bbyBlue = (205,234,255)
teal = (204,255,255)
darkBlue = (95,165,206)
# got colors from https://www.rapidtables.com/web/color/RGB_Color.html

# define functions 
def sineWave(amp,y_pos):
    """draws sine waves on the screen"""
    for x in range (5,795):
        y = int((y_pos)+amp*math.sin(frequency*((float(x)/800)*(2*math.pi)+(speed*time.time()))))
        screen.set_at((x,y),bbyPink)
# got sine wave formula from https://ericeastwood.com/blog/7/animated-sine-wave-two-ways-with-pygame-and-tkinter

def drawStars(quantity,size):
    """draws certain number of stars randomly across screen,
    they twinkle when placed in a while loop"""
    h = randint(50,750)
    g = randint(50,750)
    for i in range(quantity):
        pygame.draw.circle(screen,bbyPink,(h,g),size)
    
# create while loop
while run:     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    # fill screen to black
    screen.fill(black)
    
    # draw waves
    sineWave(amplitude,0)
    sineWave(amplitude,60)
    sineWave(amplitude,120)
    sineWave(amplitude,180)
    sineWave(amplitude,240)
    sineWave(amplitude,300)
    sineWave(amplitude,360)
    sineWave(amplitude,420)
    sineWave(amplitude,480)
    sineWave(amplitude,540)
    sineWave(amplitude,600)
    sineWave(amplitude,660)
    sineWave(amplitude,720)
    sineWave(amplitude,780)
    
    # draw stars
    drawStars(25,5)
    
    # draw planet 1
    pygame.draw.arc(screen, bbyPink,(x,625,1000,100),0,math.pi,25)
    pygame.draw.circle(screen,lilac,(z,700),radius1)
    pygame.draw.circle(screen,bbyPink,(z,700),radius1,6)
    pygame.draw.arc(screen, bbyPink,(x,625,1000,100),math.pi,0,50)
    # draw planet 2
    pygame.draw.circle(screen,peach,(w,175),radius2)
    pygame.draw.circle(screen,bbyOrange,(w,175),radius2,6)
    # draw planet 3
    pygame.draw.circle(screen,bbyBlue,(v,450),radius3)
    pygame.draw.circle(screen,teal,(v,450),radius3,6)
    pygame.draw.circle(screen,darkBlue,(b,500),25)
    
    # make planet1 move     
    if -1100 < x <= 1900:
        x -= step
    elif x == -1100:
        x += 1900
    
    if -600 < z <= 1900:
        z -= step
    elif z == -600:
        z += 1900
    
    #make planet2 move
    if -150 < w <= 1900:
        w -= step
    elif w == -150:
        w += 1900
    
    #make planet3 move
    if -150 < v < 1900:
        v -= step
    elif v == -150:
        v += 1900
    
    if -200 < b < 1900:
        b -= step
    elif b == -200:
        b += 1900
        
    #update screen
    pygame.display.update() 