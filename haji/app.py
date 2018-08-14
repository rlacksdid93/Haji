from flask import Flask , render_template, request, redirect
from models import dbMgr

app = Flask(__name__)

# Web Page 시작부분
@app.route("/")
def index():
    return render_template('index.html')

# 회원가입 Page
@app.route("/joinform")
def joinform():
     return render_template('joinform.html')

#회원가입 정보 저장
@app.route("/join", methods=['POST'])
def join():
    print('넘어온 값들=======================',request.form)
    id = request.form['id']
    name = request.form['name']
    pwd = request.form['pwd']
    data = (id,pwd,name)
    dbMgr.join_member(data) 
    return redirect('/index')

if __name__ =='__main__':
    app.debug = True 
    app.run()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    =========================================================================================
    
    
    
    
    
    
    
    
    # app.py
from flask import Flask, render_template, request, redirect
from models import dbMgr


app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/home")


@app.route('/home')
def home():
    return render_template('home.html')


@app.route("/join")   # id, pwd, name 입력받는 페이지
def joinform():
    return render_template('joinform.html')


@app.route("/join")
def join():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    data = (id, pwd, name)
    dbMgr.join(data)
    return redirect('/home')


@app.route('/loginform')
def loginform():
    return render_template(loginform.html)


@app.route('/login')
def login():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    data = (id, pwd, name)
    dbMgr.login(data)
    return redirect('/home/logon')


    
















if __name__ == '__main__' :
    app. debug = True
    app.run()
    
    
    
    
