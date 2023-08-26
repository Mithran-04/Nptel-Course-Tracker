from flask import Flask, redirect,render_template, request,url_for
import os
import sqlite3
import json

currentlocation=os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(currentlocation, "Exdataa.db")
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    return render_template("login.html",value="")

@app.route('/RetLogin',methods=['POST','GET'])
def RetLogin():
    return render_template("login.html",value="You have selected the courses!!")

@app.route('/array2python',methods=['POST','GET'])
def array2python():
    sqlconnection=sqlite3.Connection(db_path)
    cursor=sqlconnection.cursor()
    wordlist = json.loads(request.args.get('wordlist'))
    ln=len(wordlist)
    print(ln)
    cursor1=sqlconnection.cursor()
    cursor1.execute("select * from Cs_data where RegisterNumber='{rn}'".format(rn=wordlist[0]['col1'])) 
    data1 = cursor1.fetchall() 
    if(len(data1)>0):
          return render_template("login.html",value="You have already selected the courses!!")
    else:
        for i in range(ln):
                Applieds="insert into Cs_data values('{a}','{b}','{c}','{d}','{e}','{f}','{g}','{h}')".format(a=wordlist[i]['col1'],b=wordlist[i]['col2'],c=wordlist[i]['col3'],d=wordlist[i]['col4'],e=wordlist[i]['col5'],f=wordlist[i]['col6'],g=wordlist[i]['col7'],h=wordlist[i]['col8'])
                cursor.execute(Applieds) 
    sqlconnection.commit()
    

@app.route('/login',methods=['POST','GET'])
def login():
    sqlconnection=sqlite3.Connection(db_path)
    RNo=request.form.get('RNum')    
    print(RNo)
    cursor=sqlconnection.cursor()
    cursor.execute("select * from Ex_Data where RegisterNumber='{rn}'".format(rn=RNo)) 
    data = cursor.fetchall() 
    if(RNo=="Admin3124"):
        return render_template("search.html")
    cursor1=sqlconnection.cursor()
    cursor1.execute("select * from Cs_data where RegisterNumber='{rn}'".format(rn=RNo)) 
    data1= cursor1.fetchall() 
    if(len(data1)>0):
           return render_template("login.html",value="You have already selected the courses!!")
    if(len(data)==0):
           return render_template("login.html",value="Invalid Login!!")
    return render_template("CourseSelection.html",value=data)
  
    
@app.route('/search',methods=['POST','GET'])
def search():
    sqlconnection=sqlite3.Connection(db_path)
    RNo=request.form.get('RNum')    
    cursor=sqlconnection.cursor()
    cursor.execute("select * from Cs_data where RegisterNumber='{rn}'".format(rn=RNo)) 
    data = cursor.fetchall() 
    return render_template("search.html",value=data)

if __name__=="__main__":
           app.run(debug=True)




