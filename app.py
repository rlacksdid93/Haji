# app.py
from flask import Flask, render_template, request, redirect
from models import dbMgr

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/writeform")
def writeform():
	return render_template('writeform.html')

@app.route("/write", methods=['POST'])
def write():
	print('넘어온 값들====', request.form)
	names = request.form['names']
	age = request.form['age']
	pwd = request.form['pwd']
	data = (names,pwd,age)
	dbMgr.board_write(data)
	return redirect('/')

@app.route("/list")
def list():
	rows = dbMgr.board_list()
	return render_template('list.html', rows=rows)

# @app.route("/read/<num>")
# def read(num):
# 	dbMgr.board_hit_up(num)
# 	row = dbMgr.board_read(num)
# 	return render_template('read.html', row=row)

# @app.route("/updateform/<num>")
# def updateform(num):
# 	row = dbMgr.board_read(num)
# 	return render_template('updateform.html', row=row)
 
# @app.route("/update", methods=['POST'])
# def update():
# 		print('넘어온값들',request.form) 	
# 		num = request.form['num']
# 		name=request.form['name']
# 		title=request.form['title']
# 		content=request.form['content']
# 		pwd=request.form['pwd']
# 		data=(name,title,content,num,pwd)
# 		result=dbMgr.board_update(data)
# 		if result==0:
#     			return "<script>alert('비밀번호가 틀려서 되돌아갑니다.');history.back();</script>"
# 		else:
#     			return redirect('list')
# 		print(result)
		

		# <!-- 다 보이지 넘어오게 request.form 하면-->
    	
# @app.route("/deleteform/<num>")
# def deleteform(num):
    	# 
    	# return render_template('deleteform.html',num=num)

# @app.route("/delete", method=['POST'])
# def delete():
# 	print('delete request.form=====',request.form)
# 	num = request.form['num']
# 	pwd=request.form['pwd']
# 	data=(num,pwd)
# 	result=dbMgr.board_update(data)
# 	if result == 0:
#     		return '''<script> alert('비밀번호가 틀려서 되돌아갑니다!');
# 			history.back(); </script>'''
# 	else :
# 			return redirect('/list')
	



if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)



'''
CREATE TABLE board (
	num     INT           NOT NULL AUTO_INCREMENT , 
	name    VARCHAR(10)   NOT NULL , 
	title   VARCHAR(50)   NOT NULL , 
	content VARCHAR(3000) NOT NULL , 
	pwd     VARCHAR(20)   NOT NULL , 
	hit     INT           NOT NULL DEFAULT 0 , 
	regdate DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP ,
	CONSTRAINT PK_board   PRIMARY KEY ( num )
);
CREATE TABLE comments (
	c_no      INT          NOT NULL AUTO_INCREMENT , 
	c_name    VARCHAR(10)  NOT NULL , 
	c_content VARCHAR(500) NOT NULL , 
	c_date    DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP , 
	num       INT          NULL ,
	CONSTRAINT PK_comments PRIMARY KEY ( c_no ) ,
	CONSTRAINT FK_board_TO_comments FOREIGN KEY ( num ) REFERENCES board ( num )
);

update board 
set name='이름 변경', title='제복 변경', 
	content='내용 변경', 	 regdate=now() 
	where num=1 and pwd='123'
'''
