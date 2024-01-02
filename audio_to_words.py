from flask import Flask,request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        file_contents = uploaded_file.read()
        return render_template('index.html', file_contents=file_contents)
    else:
        return render_template('index.html')

@app.route('/process_convert_form',methods=['GET','POST'])
def process_convert_form():
    if request.method == 'POST':
        ##call conversion api
        with open('request_info/info.txt', 'r') as f:
            content = f.read()
            return content
        #return "Convert Successfully!"
    else:
        return render_template('index.html')
    

