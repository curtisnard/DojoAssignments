from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def Counter():
    try:
        session['count'] += 1
    except KeyError:
        session['count'] = 1
@app.route('/')
def index():
    Counter()
    return render_template('index.html', count=session['count'])
@app.route('/increment', methods=['POST'])
def increment():
    Counter()
    return redirect('/')
@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')
app.run(debug=True)
