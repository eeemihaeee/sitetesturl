from app import app
from flask import render_template
@app.route('/')
@app.route('/index/?')
def index():
		user = {'nickname':'Mihael'}
		posts = [{
		 'author': {'nickname':'John'},
		'body':'Это сообщение прекрасно!'
		},
			{
				'author': {'nickname': 'Anton'},
				'body': 'Автор зрит в корень!'
			}
		]
		return render_template(
			'index.html', title='Home', user=user,posts=posts)
from app.forms import LoginForm
@app.route('/login')
def login():
	form =LoginForm()
	return render_template('login.html',
						   title='Sign In',form=form)
