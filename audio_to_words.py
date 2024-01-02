from flask import Flask,request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        file_contents = uploaded_file.read()
        with open("wav2word/data/input.wav","wb") as f:
            f.write(file_contents)
        return render_template('index.html', file_contents=file_contents)
    else:
        return render_template('index.html')

@app.route('/process_convert_form',methods=['GET','POST'])
def process_convert_form():
    if request.method == 'POST':
        ##call conversion api
        import wav2word.scripts.process as process
        txt,pinyin=process.process("../data/input.wav")
        # with open('request_info/info.txt', 'r') as f:
        #     content = f.read()
        return txt
        #return "Convert Successfully!"
    else:
        return render_template('index.html')
    

