from flask import Flask, render_template
import sqlite3
import os
app = Flask(__name__)

name='Имя'
@app.route("/")
def home():
    return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)