from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL
import sys

app = Flask(_name_, template_folder ='../Flaskapp/templates')

global user
global userID
global password
mysql = MySQL()



app.config['MYSQL_DATABASE_USER'] = 'editor'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'lifehacks'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()



# @app.route("/home.html")
# def main():
#     return render_template('home.html')

@app.route("/", methods = ['GET'])
def main():
    return render_template('home.html')

@app.route("/search_page.html")
def show_search():
    return render_template('search_page.html')

@app.route("/hack_created.html")
def show_it():
    return render_template('hack_created.html')

@app.route('/post.html')
def showSignUp():
    return render_template('post.html')

@app.route('/post.html', methods=['POST'])
def post():

    # read the posted values from the UI
    _hackTitle = request.form['hack_title']
    _content = request.form['content']
    query = "INSERT INTO HACKS ( hackID, hack_title, content, userID) VALUES (0, %s, %s, 0)"
    cursor.execute(query, (_hackTitle, _content, userID))
    conn.commit()

    return render_template('hack_created.html')

@app.route('/loginpage.html')
def showlogin():
    return render_template('/loginpage.html')

@app.route('/loginpage.html', methods=['POST'])
def login():
        _username = request.form['user_name']
        _password = request.form['password']
        username = _username
        password = _password
        #query = "SELECT U.password FROM Users U WHERE U.email = %s"
        #cursor.execute(query, _username)
        #conn.commit()
        #cursor = conn.cursor()
        operation = "SELECT U.password, U.userID FROM Users U WHERE U.email = 'blah@example.com'"
        cursor.execute(operation)
        data = cursor.fetchall()
        userID = data[0][1]

        if data[0][0] == password:

        #if data == _password:
            return render_template('home.html')
        else:
            return render_template('/loginpage.html', methods = ['Post'])

@app.route('/signup.html')
def signup():
        _username = request.form['user_name']
        _password = request.form['password']
        query = "INSERT INTO Users VALUES _username, _password"
        cursor.execute(query)
        conn.commit()
        #cursor.close()
        #conn.close()

if _name_ == "_main_":
    app.run()