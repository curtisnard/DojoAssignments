from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
def countLetters(word):
    count = 0
    for c in word:
        count += 1
    return count
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/result', methods=['POST'])
def result():
    print "Submitted Info"
    if request.form['YourName'] == '' and request.form['commentbox'] == '':
        flash('Name cannot be blank', 'nameError')
        flash('Comment cannot be blank', 'commentError')
        return redirect('/')
    if request.form['YourName'] == '':
        flash('Name cannot be blank', 'nameError')
        return redirect('/')
    if request.form['commentbox'] == '':
        flash('Comment cannot be blank', 'commentError')
        return redirect('/')
    session['comment'] = request.form['commentbox']
    comment = countLetters(session['comment'])
    print comment
    if comment > 120:
        flash('Comment is too long', 'commentError')
        return redirect('/')
    session['YourName'] = request.form['YourName']
    session['DojoLocation'] = request.form['DojoLocation']
    session['FavoriteLanguage']= request.form['FavoriteLanguage']
    return redirect('/show')
@app.route('/show')
def show_user():
  return render_template('result.html')
app.run(debug=True) # run our server
