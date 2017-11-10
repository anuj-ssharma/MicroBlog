from flask import render_template
from app import app
from .forms import LoginForm
from flask import flash,redirect

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'AJ'} #fake user
    posts = [ #fake array of posts
        {
            'author' : {'nickname':'John'},
            'body' : 'Beautiful day in Portland'
        },
        {
            'author': {'nickname':'Susan'},
            'body':'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title="Namaste",
                           user=user,
                           posts=posts)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)