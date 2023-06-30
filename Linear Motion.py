# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 21:12:48 2023

@author: Ajax
"""

'''Calculator to calculate Linear Motion'''
from math import sqrt
def Linear_Motion():
    print("Please give answer in response to s,u,a,t,v") 
    print("s = distance")
    print("v = velocity")
    print("t = time")
    print("u = initial velocity")
    print("v = final velocity")
    First_Stage = input("What are you solving for: ").lower()
    if First_Stage == "v":
        u = float(input('Enter the initial Velocity: '))
        a = float(input('Enter the acceleration: '))
        t = float(input('Enter the time: '))
        v = u+(a*t)
        print (f'The final velocity is {v}')
   
    

    elif First_Stage == "s":
        u = float(input('Enter the initial Velocity: '))
        t = float(input('Enter the time: '))
        a = float(input('Enter the acceleration: '))
        s = (u*t) + (0.5*(a*(t*t)))
        print (f'The linear distance is {s}')
    

    elif  First_Stage == "u":
        confirm = (input("Is Final Velocity Giving: ")).lower()
        if confirm == "yes":
            v = float(input("What is the final velocity: "))
            a = float(input('Enter the acceleration: '))
            t = float(input('Enter the time: '))
            u = v - (a*t)
            print (f'The initial velocity is {u}')
        elif confirm == 'no':
            s = float(input("Enter the  distance: "))
            a = float(input('Enter the acceleration: '))
            t = float(input('Enter the time: '))
            u = (s - (0.5*(a*(t*t))))/t
            print (f'The initial velocity is {u}')
        else:
            print('Enter the right value!!')
    elif First_Stage == "t":
        confirm = input("Is Final Velocity Giving: ").lower()
        if confirm == "yes":
           v = float(input("What is your Final Velocity: ")) 
           u = float(input("What is Initial Velocity: "))
           a = float(input("What is the acceleration: "))
           t = (v-u)/a
           print (f'The time is {t}')
           
        elif confirm == 'no': 
              s = float(input("What is the distance: "))
              u = float(input("What is Initial Velocity: "))
              a = float(input("What is the acceleration: "))
              d = 4*(u**2) + (8*a*s)
              if d >= 0:
                  t1 = ( (-2*u) + sqrt(d) ) / (2*a)
                  t2 = ( (-2*u) - sqrt(d) ) / (2*a)
                  print (f"t1 is {t1} is and t2 is {t2}")
                 
              else:
                  print("You will be Getting a Complex Number!")
        else:
            print('Enter the right value!!')
            Linear_Motion()
    else:
        confirm = input("Is Final Velocity Giving: ").lower()
        if confirm == "yes":
           v = float(input("What is your Final Velocity: ")) 
           u = float(input("What is Initial Velocity: "))
           t = float(input("What is the time: "))
           a = (v-u)/t
           print (f'The acceleration is {a}')
        elif confirm == "no":
            s = float(input("What is the distance: "))
            u = float(input("What is Initial Velocity: "))
            t = float(input("What is the time: "))
            a = (s-(u*t))/(0.5*(t*t))
            print(f'The acceleration is {a}')
        else:
            print("Enter the right value!!")

def done():
    done = int(input("How many variables are you solving for: "))
    for x in range(done):
        Linear_Motion()
       
          


    
  
       
Linear_Motion()
done()
    


     

