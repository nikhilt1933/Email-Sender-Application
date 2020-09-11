# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 22:41:08 2019

@author: Nikhil
"""

import smtplib

# Send mail function
def send_mail(gmail, to, password, message):
    
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(gmail,password)
    s.sendmail(gmail,to,message)
    
    s.quit()
    
#send_mail('soni7.nikhil@gmail.com','nikhilthadeshwar2@gmail.com','aksharnikhil','Hello')
