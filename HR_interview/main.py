import time
import mj
import cv2
import pytesseract
import PIL
from PIL import Image
import base64
import mysql.connector
import numpy as np
import speech_recognition as sr
import string
import io


i=0
def rgen():
    import secrets
    import string
    N = 10
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits)
                  for i in range(N))

    return res
def ctob(fname):
    with open(fname,'rb') as file:
        bdata = file.read()
    return bdata


def raj(p):
    import fitz
    filepath = r''+p
    text = ''
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.getText()
    ark = text.split()
    l = len(ark)
    for i in range(l):
        if(ark[i]=="ECE"):
            var = "ECE"
        elif(ark[i]=="CSE"):
            var = "CSE"
        elif(ark[i]=="MECH"):
            var = "MECH"
    return var
def ram(pr):
    mro = ctob(r''+pr)
    print(mro)
    mycursor = mydb.cursor()
    sql = '''select *from details ORDER BY id DESC LIMIT 1;'''
    mycursor.execute(sql)
    row2 = mycursor.fetchall();
    y22 = list(row2[0])
    mycursor.execute("""
       UPDATE details
       SET resume=%s
       WHERE id=%s
    """, (mro, y22[0]))
    mydb.commit()
def btof(bd,fn):
    with open(fn,'wb') as file:
        file.write(bd)

def imgr(srl):
    binary_data = base64.b64decode(srl)
    image = Image.open(io.BytesIO(binary_data))
    image.show()
def jetm(ksi):
    binary_data = base64.b64decode(ksi)
    image = Image.open(io.BytesIO(binary_data))
    image.show()



fn = ["c0.wav","c1.wav","c2.wav","c3.wav","c4.wav"]
eceq =["Why do you want to be a teacher?","What’s your teaching style or philosophy?","How would you handle a student you found difficult to teach?","How do you motivate students?","Tell me about a time when you worked with a team to solve a problem.","Tell me about a time when you faced a difficult challenge.","Tell me about a time when a situation changed or something unexpected happened at work and how you dealt with it.","During the COVID-19 pandemic, how did you ensure your class stayed on track and engaged and learned as much as possible?","How do you deal with pressure or stressful situations?","How would you encounter a situation where a student feels the risk of failing in your subject what steps will you be taking on behalf of the studemt"]
cseq = ["explain datastructures","explain recursion","explain devOps","explain high level programming","explain client server architecture"]
mechq = ["Why do you want to be a teacher?","What’s your teaching style or philosophy?","How would you handle a student you found difficult to teach?","How do you motivate students?","Tell me about a time when you worked with a team to solve a problem.","Tell me about a time when you faced a difficult challenge.","Tell me about a time when a situation changed or something unexpected happened at work and how you dealt with it.","During the COVID-19 pandemic, how did you ensure your class stayed on track and engaged and learned as much as possible?","How do you deal with pressure or stressful situations?","How would you encounter a situation where a student feels the risk of failing in your subject what steps will you be taking on behalf of the studemt"]
cans = ["object","object","object","object","object"]
mans = ["mechanics","mechanics","mechanics","mechanics","mechanics"]
eans = ["electric","electric","electric","electric","electric"]
k=0
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for, json
from flask import Flask
from flask import render_template,request
from flask import jsonify
from threading import Thread

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="yaswanth",
  database="sys"
)
app = Flask(__name__,template_folder="C:/Users/bharg/OneDrive/Desktop/bhargavi/HR_interview/templates")
app.secret_key = 'karthikkarthikkarthik'
from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
arr = np.array([0, 1, 2, 3, 4])
np.random.shuffle(arr)
@app.route('/')
def index():
    return render_template('1.html')
@app.route('/up', methods=['POST','GET'])
def mest():
    i=0
    if(i==0):
        if (request.method == "POST"):
            path = request.form.get('resume')
            name1 = request.form.get('name')
            x = request.form.copy()
            mycursor = mydb.cursor()
            sql = "INSERT INTO details (name, marks,attentive,beg_pic,end_pic,voice,resume) VALUES (%s, %s,%s,%s,%s,%s,%s)"
            val = (name1, 10,"yes","null","null","null","null")
            mycursor.execute(sql,val)
            mydb.commit()
            #ram(x['resume'])
            #math1 = raj(x['resume'])
            file1 = open('b_pic.jpg', 'rb').read()
            file1 = base64.b64encode(file1)
            cursor = mydb.cursor()
            sql = '''select *from details ORDER BY id DESC LIMIT 1;'''
            cursor.execute(sql)
            row228 = cursor.fetchall()
            y899 = list(row228[0])
            cursor.execute("""
                      UPDATE details
                      SET beg_pic=%s
                      WHERE id=%s
                   """, (file1, y899[0]))
            mydb.commit()
            if (path == "PHD" or "phd"  ):
                return render_template("2.html")
            elif (path == "MBA" or "mba"):
                return render_template("2cse.html")
            elif (path == "mtech" or "MTECH"):
                return render_template("2mech.html")
        return '''<form method="post">
          <br><p1>Enter your Name and Your Resume's Path Here:</p1><br>
         <br><input type="text" name="name"><br>
         <br><input type="text" name="resume"><br>
        <br><input type="submit"><br>
         </form>
          <script> function sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
   }
   async function timer(){
      await sleep(3000);
      alert("ADD .PDF EXTENTION AT THE END");
      }
      timer();
   </script>'''
@app.route("/tpic")
def t_pc():
    import cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = videoCaptureObject.read()
        cv2.imwrite("b_pic.jpg", frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return render_template("3.html")

@app.route('/ec_ev')
def map():
    i=0
    try:
        marks = 0
        while (i < 5):
            AUDIOK = (fn[i])
            r = sr.Recognizer()

            with sr.AudioFile(AUDIOK) as source:
                kr = r.record(source)
                kr1 = r.recognize_google(kr)
                arrj = kr1.lower()
                arr1 = arrj.split()
                try:
                    for x in range(100):
                        if (arr1[x] == eans[arr[i]] or arr1[x] == eans[arr[i]]):
                            marks += 1
                            break
                except:
                    print("WRONG ANSWER")

            i += 1
    except:
        print("no answers")

    mycursor = mydb.cursor()
    sql = '''select *from details ORDER BY id DESC LIMIT 1;'''
    mycursor.execute(sql)
    row = mycursor.fetchall()
    y89 = list(row[0])
    mydb.commit()
    mycursor.execute("UPDATE details SET marks=%s WHERE id='%s'" % (str(marks),y89[0]))
    mydb.commit()
    return render_template("pwait.html")
@app.route("/cs_ev")
def cs_ev():

    i=0
    try:
        marks = 0
        while (i < 5):
            AUDIOK = (fn[i])
            r = sr.Recognizer()

            with sr.AudioFile(AUDIOK) as source:
                kr = r.record(source)
                kr1 = r.recognize_google(kr)
                arrj = kr1.lower()
                arr1 = arrj.split()
                try:
                    for x in range(100):
                        if (arr1[x] == cans[arr[i]] or arr1[x] == cans[arr[i]]):
                            marks += 1
                            break
                except:
                    print("WRONG ANSWER")

            i += 1
    except:
        print("no answers")

    mycursor = mydb.cursor()
    sql = '''select *from details ORDER BY id DESC LIMIT 1;'''
    mycursor.execute(sql)
    row = mycursor.fetchall()
    y89 = list(row[0])
    mydb.commit()
    mycursor.execute("UPDATE details SET marks=%s WHERE id='%s'" % (str(marks),y89[0]))
    mydb.commit()
    return render_template("pwait.html")
@app.route("/me_ev")
def me_ev():
    i=0
    try:
        marks = 0
        while (i < 5):
            AUDIOK = (fn[i])
            r = sr.Recognizer()

            with sr.AudioFile(AUDIOK) as source:
                kr = r.record(source)
                kr1 = r.recognize_google(kr)
                arrj = kr1.lower()
                arr1 = arrj.split()
                try:
                    for x in range(100):
                        if (arr1[x] == mans[arr[i]] or arr1[x] == mans[arr[i]]):
                            marks += 1
                            break
                except:
                    print("WRONG ANSWER")

            i += 1
    except:
        print("no answers")

    mycursor = mydb.cursor()
    sql = '''select *from details ORDER BY id DESC LIMIT 1;'''
    mycursor.execute(sql)
    row = mycursor.fetchall()
    y89 = list(row[0])
    mydb.commit()
    mycursor.execute("UPDATE details SET marks=%s WHERE id='%s'" % (str(marks),y89[0]))
    mydb.commit()
    return render_template("pwait.html")

@app.route('/take')
def t_pic():
    import take1
    return render_template("3cse.html")
@app.route("/ccam")
def c_cam():
    return render_template("3cse.html")
@app.route("/ecam")
def e_cam():
    return render_template('3.html')
@app.route("/mcam")
def m_cam():
    return render_template("3mech.html")
@app.route('/cbel')
def cb():
    return render_template("cse.html")
@app.route('/ebel')
def eb():
    return render_template("ece.html")
@app.route("/mbel")
def mb():
    return render_template("mech.html")
@app.route("/talk")
def ta_k():
    import talkk
    return render_template("talk.html")

@app.route('/last')
def lst():
    import cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = videoCaptureObject.read()
        cv2.imwrite("l_pic.jpg", frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    file = open('l_pic.jpg', 'rb').read()
    file = base64.b64encode(file)
    mycursor = mydb.cursor()
    sql = '''select *from details ORDER BY id DESC LIMIT 1;'''
    mycursor.execute(sql)
    row22 = mycursor.fetchall();
    y28 = list(row22[0])
    mycursor.execute("""
       UPDATE details
       SET end_pic=%s
       WHERE id=%s
    """, (file, y28[0]))
    mydb.commit()
    import os, os.path
    DIR = r'C:\Users\saika\PycharmProjects\jaiganesh\images'
    x = (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
    count = 0
    c = 0
    m = 0
    a1 = 0
    a2 = 0
    a3 = 0
    l = 0
    r = 0
    d = 0
    arr = []
    print(x)
    for i in range(0, x):
        import cv2
        import pytesseract
        import PIL
        from PIL import Image
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        img = 'images/result' + str(i) + '.jpg'
        imge = Image.open(img)
        data = pytesseract.image_to_string(imge)
        text = data
        arr.append(text)
        mj = arr[i]
        if (mj[:-1] == "FORWARD,"):
            count += 1
            if (count != 0):
                l = 1
                r = 0
        elif (mj[:-1] == "FORWARD."):
            c += 1
            if (c != 0):
                r = 1
                l = 0
        elif (mj[:-1] == "FORWARD"):
            if (l == 1):
                l = 0
                a1 += 1
                l = 0

            if (r == 1):
                r = 0
                a2 += 1
                r = 0
    print(a1,a2)
    if(a1==0 and a2==0):
        mycursor = mydb.cursor()
        sql = '''select *from details ORDER BY id DESC LIMIT 1;'''
        mycursor.execute(sql)
        row2 = mycursor.fetchall();
        y2 = list(row2[0])
        mycursor.execute("UPDATE details SET attentive='%s' WHERE id='%s'" % ('YES', y2[0]))
        mydb.commit()
        ffile = ctob(r'talk.wav')
        mycursor.execute("""
       UPDATE details
       SET voice=%s
       WHERE id=%s
    """,(ffile, y2[0]))
        mydb.commit()
    else:
        mycursor = mydb.cursor()
        sql = '''select *from details ORDER BY id DESC LIMIT 1;'''
        mycursor.execute(sql)
        row2 = mycursor.fetchall();
        y2 = list(row2[0])
        mycursor.execute("UPDATE details SET attentive='%s' WHERE id='%s'" % ('NO', y2[0]))
        mydb.commit()
        kkfile = ctob(r'talk.wav')
        mycursor.execute("""
               UPDATE details
               SET voice=%s
               WHERE id=%s
            """, (kkfile, y2[0]))
        mydb.commit()

    return render_template("end.html")
@app.route('/cse')
def cse_q():
    import img120
    import rks
    user = {'o': cseq[arr[0]], 't': cseq[arr[1]],"th":cseq[arr[2]],"f":cseq[arr[3]],"fi":cseq[arr[4]],"si":"cse"}
    return render_template("map.html", user=user)
@app.route('/ece')
def ece_q():
    import img120
    import rks
    user = {'o': eceq[arr[0]], 't': eceq[arr[1]],"th":eceq[arr[2]],"f":eceq[arr[3]],"fi":eceq[arr[4]],"si":"ece"}
    return render_template("map.html", user=user)
@app.route('/mech')
def mech_q():
    import img120
    import rks
    user = {'o': mechq[arr[0]], 't': mechq[arr[1]],"th":mechq[arr[2]],"f":mechq[arr[3]],"fi":mechq[arr[4]],"si":"mech"}
    return render_template("map.html", user=user)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'
users = []
users.append(User(id=1, username='hr_access', password='software'))
users.append(User(id=2, username='karthik', password='patnaik'))

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
@app.route('/hr_login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))
        return redirect(url_for('login'))
    return render_template('login.html')
cursor= mydb.cursor()

cursor.execute("SELECT * FROM details")


result = cursor.fetchall()
@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))
    else:
        return render_template('hr.html')
@app.route("/ret", methods=['POST','GET'])
def re():
    if not g.user:
        return redirect(url_for('login'))
    else:
        if (request.method == "POST"):
            path = request.form.get('index')
            xl = request.form.copy()
            kkr = int(xl['index'])
            print(result[kkr])
            return str(result[kkr])



    return '''<form method="post">
      <br><p1>Enter ID Here:</p1><br>
     <br><input type="text" name="index"><br>
    <br><input type="submit"><br>
    <script> function sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
   }
   async function timer(){
      await sleep(2000);
      alert("IN ORDER TO VIEW COMPLETE DATABASE LOGIN TO MYSQL SERVER BY USING WORKBENCH");
      }
      timer();
   </script>
     </form>'''
@app.route("/num")
def nu():
    if not g.user:
        return redirect(url_for('login'))
    else:
        cursor = mydb.cursor()

        cursor.execute("SELECT COUNT(*) FROM details;")

        r1 = cursor.fetchall()
        return str(r1[0])


@app.route('/conv',methods=['POST','GET'])
def co():
    if not g.user:
        return redirect(url_for('login'))
    else:
        if (request.method == "POST"):
            path = request.form.get('index')
            kath = request.form.get('path')
            kl = request.form.copy()
            xl = request.form.copy()
            lks = int(xl['index'])
            mkr = str(kl['path'])
            cursor = mydb.cursor()
            query = '''SELECT resume FROM details WHERE id=%s'''
            values = (lks)
            cursor.execute(query, (values,))
            data = cursor.fetchall()
            image = data[0][0]
            btof(image, r'' + mkr)
            return "completed"
        return '''<form method="post">
          <br><p1>Enter ID and Your Path Here:</p1><br>
         <br><input type="text" name="index"><br>
         <br><input type="text" name="path"><br>
        <br><input type="submit" value="Get Resume"><br>
         </form>'''

@app.route("/voice",methods=['POST','GET'])
def vo_ce():
    if not g.user:
        return redirect(url_for('login'))
    else:
        if (request.method == "POST"):
            path = request.form.get('index')
            kath = request.form.get('path')
            kl = request.form.copy()
            xl = request.form.copy()
            lks = int(xl['index'])
            mkr = str(kl['path'])
            cursor = mydb.cursor()
            query = '''SELECT voice FROM details WHERE id=%s'''
            values = (lks)
            cursor.execute(query, (values,))
            data = cursor.fetchall()
            image = data[0][0]
            btof(image, mkr)
            return "completed"
    return '''<form method="post">
    <br><p1>Enter ID and Your Path Here:</p1><br>
     <br><input type="text" name="index"><br>
     <br><input type="text" name="path"><br>
    <br><input type="submit" value="Get"><br>
     </form>'''
@app.route("/is1",methods=['POST','GET'])
def ism1():
    if not g.user:
        return redirect(url_for('login'))
    else:
        if (request.method == "POST"):
            path = request.form.get('index')
            xl = request.form.copy()
            lks = int(xl['index'])
            cursor = mydb.cursor()
            query = '''SELECT beg_pic FROM details WHERE id=%s'''
            values = (lks)
            cursor.execute(query, (values,))
            data1 = cursor.fetchall()
            image1 = data1[0][0]
            imgr(image1)
            return "completed"

        return '''<form method="post">
        <br><p1>Enter ID Here:</p1><br>
         <br><input type="text" name="index"><br>
        <br><input type="submit" value="View Beginning Picture"><br>
         </form>'''

@app.route("/im2",methods=['POST','GET'])
def ims_2():
    if not g.user:
        return redirect(url_for('login'))
    else:
        if (request.method == "POST"):
            path = request.form.get('index')
            xl = request.form.copy()
            lks = int(xl['index'])
            cursor = mydb.cursor()
            query = '''SELECT end_pic FROM details WHERE id=%s'''
            values = (lks)
            cursor.execute(query, (values,))
            data = cursor.fetchall()
            image = data[0][0]
            imgr(image)
            return "completed"

        return '''<form method="post">
        <br><p1>Enter ID Here:</p1><br>
         <br><input type="text" name="index"><br>
        <br><input type="submit" value="View Ending Picture"><br>
         </form>'''



if __name__ == '__main__':
    app.run(debug=False)