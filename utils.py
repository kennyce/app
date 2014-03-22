from flask import url_for, render_template, redirect, session, flash
from flask.ext.wtf import Form
from wtforms import TextField,BooleanField,TextAreaField
from wtforms.validators import Required,EqualTo,Length
#from collections import deque
from app import db as d
from app.models import Message as mess
from app import app


	
#IST = deque([{'sender':'','message':'','time':''},{'sender':'','message':'','time':''},{'sender':'','message':'','time':''},{'sender':'','message':'','time':''},{'sender':'','message':'','time':''},{'sender':'','message':'','time':''},{'sender':'','message':'','time':''},{'sender':'','message':'','time':''},{'sender':'','message':'','time':''},{'sender':'','message':'','time':''}])


#def rotate(l,n):
#   return l[n:] + l[:n]


class PostForm(Form):
	sender= TextField('title',validators=[Required(),Length(min=2,max=10)])
	message = TextAreaField('content',validators = [Required(),Length(min=2,max=100)])
	
	
@app.route('/')
@app.route('/create_post', methods=['GET','POST'])
def create():
	form = PostForm()
	if form.validate_on_submit():
		#MSG_LIST.rotate()		
		#MESSAGES = rotate(MESSAGES,1)
		#MSG_LIST[0]['sender'],MSG_LIST[0]['message'],MSG_LIST[0]['time'] = form.sender.data,form.message.data,datetime.utcnow()
		m = mess(form.sender.data,form.message.data)
		d.session.add(m)
		d.session.commit()
		flash('Your message is on the queue, watch the screen!')
		return redirect('/create_post')
	return render_template('create_screen.html',form=form)
	
@app.route('/create_', methods=['GET'])
def sold():
	return render_template('h.html')
	
	


	
		
	




