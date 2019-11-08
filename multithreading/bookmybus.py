#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:09:38 2019

@author: giudittaparolini
"""

from threading import *

class BookMyBus:
    def buy(self):
        print("Confirming a seat")
        print("Processing the payment")
        print("Printing the Ticket")

obj = BookMyBus()

t1 = Thread(target = obj.buy() )
t2 = Thread(target = obj.buy() )
t3 = Thread(target = obj.buy() )

t1.start()
t2.start()
t3.start()

print ("-------")

class BookMyBus():
    
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        
    def buy(self, seatsRequested):
        print("Total seats available:", self.availableSeats)
        if (self.availableSeats>=seatsRequested):
            print("Confirming a seat")
            print("Processing the payment")
            print("Printing the Ticket")
            self.availableSeats-=seatsRequested
        else:
            print("Sorry. There are no seats available")
            
obj = BookMyBus(10)

t1 = Thread(target=obj.buy,args=(3,))
t2 = Thread(target=obj.buy,args=(4,))
t3 = Thread(target=obj.buy,args=(4,))



t1.start()
t1.join() #if you do not join the threads the code is executed randomly and you only get the correct result once in a while
t2.start()
t2.join()
t3.start()

print ("-------")

#code synchronization with a Lock
class BookMyBus():
    
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.l = Lock()
        
    def buy(self, seatsRequested):
        self.l.acquire()
        print("Total seats available:", self.availableSeats)
        if (self.availableSeats>=seatsRequested):
            print("Confirming a seat")
            print("Processing the payment")
            print("Printing the Ticket")
            self.availableSeats-=seatsRequested
        else:
            print("Sorry. There are no seats available")
        self.l.release()
            
obj = BookMyBus(10)

t1 = Thread(target=obj.buy,args=(3,))
t2 = Thread(target=obj.buy,args=(4,))
t3 = Thread(target=obj.buy,args=(4,))



t1.start()
t2.start()
t3.start()

#code synchronization with a Semaphore
class BookMyBus():
    
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.l = Semaphore()
        
    def buy(self, seatsRequested):
        self.l.acquire()
        print("Total seats available:", self.availableSeats)
        if (self.availableSeats>=seatsRequested):
            print("Confirming a seat")
            print("Processing the payment")
            print("Printing the Ticket")
            self.availableSeats-=seatsRequested
        else:
            print("Sorry. There are no seats available")
        self.l.release()
            
obj = BookMyBus(10)

t1 = Thread(target=obj.buy,args=(3,))
t2 = Thread(target=obj.buy,args=(4,))
t3 = Thread(target=obj.buy,args=(4,))



t1.start()
t2.start()
t3.start()