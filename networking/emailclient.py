#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:39:45 2019

@author: giudittaparolini
"""

import smtplib

from email.mime.text import MIMEText

body = "This is a test email. How are you?"

msg = MIMEText(body)
msg['From'] = "XXX"
msg['To'] = "XXX"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login("XXX", "YYY")

server.send_message(msg)

print("Mail sent")

server.quit()