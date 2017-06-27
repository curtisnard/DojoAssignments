from flask import Flask, render_template, request, redirect, session, flash, url_for
from datetime import datetime
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriendsdb')
app.secret_key = 'ThisIsSecret'
@app.route('/', methods=['GET'])
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', friends=friends)
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {'first_name': request.form['first_name'],'last_name': request.form['last_name'],'email': request.form['email']}
    mysql.query_db(query, data)
    return redirect('/')
@app.route('/friends/<id>/edit')
def edit(id):
    data = {"specific_id": id}
    query = "SELECT * FROM friends WHERE id = :specific_id LIMIT 1"
    friend = mysql.query_db(query, data)
    return render_template("editpage.html", person=friend)
@app.route('/friends/<id>', methods=['POST'])
def update(id):
    info = {'specific_id': id,'first_name': request.form['first_name'],'last_name':  request.form['last_name'],'email': request.form['email']}
    query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email, updated_at=NOW() WHERE id=:specific_id LIMIT 1"
    mysql.query_db(query, info)
    return redirect('/')
@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    datum = {"specific_id": id}
    query = "DELETE FROM friends WHERE id = :specific_id"
    mysql.query_db(query, datum)
    return redirect('/')
app.run(debug=True)
