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


@app.route("/joinform")   # id, pwd, name 입력받는 페이지
def joinform():
    return render_template('joinform.html')


@app.route("/join", methods=["POST"])
def join():
    id = request.form['id']
    pwd = request.form['pwd']
    name = request.form['name']
    data = (id, pwd, name)
    dbMgr.join(data)
    return redirect('/home')


@app.route('/loginform')
def loginform():
    return render_template('loginform.html')


@app.route('/login', methods=["POST"])
def login():
    id = request.form['id']
    pwd = request.form['pwd']
    data = (id, pwd)
    if dbMgr.login(data) == True : return redirect('/home')
    else : return "<script>alert('비밀번호가 틀려서 되돌아갑니다!');history.back();</script>"


@app.route('/login_errform')
def login_errfrom():
    return render_template(login_errfrom.html)

    


    
















if __name__ == '__main__' :
    app. debug = True
    app.run()
