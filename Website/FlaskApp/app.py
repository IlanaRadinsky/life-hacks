from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'uradinsk'
app.config['MYSQL_DATABASE_PASSWORD'] = 'p2253'
app.config['MYSQL_DATABASE_DB'] = 'diradinsk'
app.config['MYSQL_DATABASE_HOST'] = 'mysql://iradinsky:poodleblue96!@ada.sterncs.net:3306'

"""
app.config['MYSQL_DATABASE_USER'] = 'editor'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'lifehacks'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)"""

conn = mysql.connect()
cursor = conn.cursor()



@app.route("/")
def main():
    return render_template('home.html')


@app.route('/post.html')
def showSignUp():
    return render_template('post.html')

@app.route('/post.html', methods=['POST'])
def post():

    # read the posted values from the UI
    _hackid = request.form['hack_title']
    _content = request.form['textarea1']
    hi_ilana = "hi ilana!!"
    query = "INSERT INTO TAGS VALUES (hi_ilana)"
    #query = "INSERT INTO TAGS VALUES ({_hackid})"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


    return json.dumps({'html':'<span>That\'s a great hack!</span>'})

if __name__ == "__main__":
    app.run()
