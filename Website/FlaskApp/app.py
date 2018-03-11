from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL
app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'editor'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'lifehacks'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()



@app.route("/")
def main():
    return render_template('home.html')

@app.route('/post.html')
def showSignUp():
    return render_template('post.html')
@app.route('/

@app.route('/signUp',methods=['POST'])
def signUp():
 
    # read the posted values from the UI
    _hackid = request.form['inputName']
    _content = request.form['inputEmail']
    _userID = request.form['inputPassword']
    
    query = "INSERT INTO HACKS (hackid, content, userID) VALUES (%s, %s, %s)" % (1, _content, _userID)
    cursor.execute(query)
    
    
    return json.dumps({'html':'<span>That\'s a great hack!</span>'})

if __name__ == "__main__":
    app.run()
    
