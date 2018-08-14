# app.py
from flask import Flask, render_template, request, redirect, session
from models import dbMgr



app = Flask(__name__)

app.secret_key = 'fgyfgyghjhghbkjhkjhkljjklj'

@app.route('/')
def index():
    return redirect("/homeform")

'''
@app.route('/homeform')
def homeform():
    return render_template('homeform.html')
'''

@app.route('/homeform')
def homeform():
    if 'id' in session :
        id =session['id']
        return render_template('homeform.html', id=id)
    else:
        return render_template('homeform.html', id=None)

@app.route('/home',  methods=["POST"])
def home():
    id = request.form['id']
    pwd = request.form['pwd']
    data = (id, pwd)
    torf = dbMgr.login(data)
    if torf == True : # 로그인 정보 맞음
        session['id'] = id
        return render_template('homeform.html', id=id)
    else : return "<script>alert('비밀번호가 틀려서 되돌아갑니다!');history.back();</script>"


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
    return redirect('/homeform')

@app.route("/member_addi_infoform")
def member_addi_infoform():
    id=session['id']
    return render_template('member_addi_infoform.html', id=id)


@app.route("/member_addi_info" , methods=["POST"])
def member_addi_info():
    id=request.form['id']
    pwd=request.form['pwd']
    age = request.form['age']
    sex = request.form['sex']
    m_type = request.form['m_type']
    m_trouble = request.form['m_trouble']
    used_prod = request.form['used_prod']
    data = (age, sex, m_type, m_trouble, used_prod, id, pwd)
    dbMgr.member_addi_info(data)
    return redirect('/homeform')

@app.route("/logout")
def logout():
    session.clear()
    return render_template('homeform.html')


# @app.route('/loginform')
# def loginform():
#     return render_template('loginform.html')


# @app.route('/login', methods=["POST"])
# def login():
#     id = request.form['id']
#     pwd = request.form['pwd']
#     data = (id, pwd)
#     if dbMgr.login(data) == True : return redirect('/home')
#     else : return "<script>alert('비밀번호가 틀려서 되돌아갑니다!');history.back();</script>"

'''
@app.route('/login_errform')
def login_errfrom():
    return render_template(login_errfrom.html)
'''

if __name__ == '__main__' :
    app. debug = True
    app.run()