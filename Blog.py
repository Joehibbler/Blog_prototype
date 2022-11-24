from flask import Flask, flash, render_template, abort, session, request, url_for,flash
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired,  DataRequired

# create flask Instant
app = Flask(__name__)
app.config['SECRET_KEY'] = "ZoraZora1!"

 # Create form-Class and secret-key
class LoginForm(Form):
      username = StringField('username', validators=[InputRequired()])
      password = PasswordField('password', validators=[InputRequired()])

@app.route('/name', methods=['GET','POST']) 
def name():
      form = LoginForm()
      if request.method=='POST':
             return 'Form Successfully Submitted!'
      return render_template('name.html', form=form)
 


 
@app.route('/') 
def index():
             return render_template("home_page.html")

@app.route('/login_form', methods=['GET','POST']) 
def login_form():
      form = LoginForm()
      if  request.method=='POST':
             return render_template("home_page.html")
      return render_template("login_form.html", form=form)
 
@app.route('/staff_dashboard') 
def staff_dashboard():
             return render_template("staff_dashboard.html")

@app.route('/register_for_camp') 
def register_form():
    
             return render_template("register_for_camp.html")
    


@app.route('/about_us') 
def about_us():
             return render_template("about_us.html")



@app.route('/event_schedule') 
def event_schedule ():
             return render_template("event_schedule.html")

@app.route('/legal_notice') 
def legal_notice ():
             return render_template("legal_notice.html")

@app.route('/logout_page') 
def logout_page():
             return render_template("logout_page.html")

@app.errorhandler(404)
def page_notfound(e):
 	          return render_template("404.html"), 404

@app.errorhandler(500)
def page_notfound(e):
 	          return render_template("500.html"), 500

if __name__ == '__main__':
   app.run(debug=True)
    # Create form-Class and secret-key