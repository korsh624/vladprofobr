from flask import Flask, render_template
app = Flask(__name__)
import json
def readData():
    data = ''
    with open("data_file.json", "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
    return data




@app.route("/")
def home():
    return render_template('index.html')


@app.route("/colledg")
def colledg():
    array=readData()
    return render_template('colledg.html',array=array)

if __name__=="__main__":
    app.run(debug=True)