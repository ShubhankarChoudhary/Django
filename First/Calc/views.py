from django.shortcuts import render

from django.http import HttpResponse

import mysql.connector 





def home(request):
    db = mysql.connector.connect(host = '127.0.0.1', user = 'root', passwd = 'Shubhankar@1', database = 'python')
    mycursor = db.cursor()
    query = ('select * from login where Name = %s')
    Name = ('Shubhankar',)
    mycursor.execute(query,Name)
    mycursor.execute('show databases')
    return HttpResponse(input('Enter you name : '))