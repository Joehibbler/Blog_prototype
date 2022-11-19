from flask import Flask, flash, render_template, abort, session, request, redirect, url_for


# create flask Instante
app = Flask(__name__)



@app.route('/') 

def index():
     return render_template("home_page.html")


@app.route('/login_form') 

#def (login_form):
   #  return render_template("login_form.html")

@app.errorhandler(404)
def page_notfound(e):
 	 return render_template("404.html"), 404

@app.errorhandler(500)
def page_notfound(e):
 	 return render_template("500.html"), 500