from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/result', methods=['POST'])
def result():
   print "Submitted Info"

   session['YourName'] = request.form['YourName']
   session['DojoLocation'] = request.form['DojoLocation']
   session['FavoriteLanguage']= request.form['FavoriteLanguage']
   session['comment'] = request.form['commentbox']

   return redirect('/show')
@app.route('/show')
def show_user():
  return render_template('result.html')
app.run(debug=True) # run our server
