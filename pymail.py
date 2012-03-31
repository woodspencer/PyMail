#!/usr/bin/python
###############################-PYMAIL-#################################
#Copyright (C) 2011-2012, Spencer Wood <spencer.wood25@gmail.com>      #
#This program is free software: you can redistribute it and/or modify  #
#it under the terms of the Lesser GNU General Public License as        #
#published by the Free Software Foundation, either version 3 of the    #
#License, or (at your option) any later version.                       #
#                                                                      #
#This program is distributed in the hope that it will be useful,       #
#but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#GNU General Public License for more details.                          #
#                                                                      #
#You should have received a copy of the GNU General Public License     #
#along with this program.  If not, see <http://www.gnu.org/licenses/>. #
#                                                                      #
#For your convience, the LGPL license can be found on the GNU website, #
#or read http://www.gnu.org/licenses/lgpl.txt.                         #
#                                                                      #
# This program is a part of PyImgur!                                   #
########################################################################

import smtplib, email.utils
from email.mime.text import MIMEText

def send_mail(username, password, recipient, subject, body):

    message = MIMEText(body)
    message['To'] = email.utils.formataddr((None, recipient))
    message['From'] = email.utils.formataddr((None, username))
    message['Subject'] = subject
	
    host = username.find('@')
    server = smtplib.SMTP(('smtp.{}:587').format(username[host+1:]))
    server.starttls()
    server.login(username, password)
    server.sendmail(username, recipient, message.as_string())
    server.quit()
