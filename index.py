import os
from flask import Flask, request, render_template, send_from_directory



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./PDF"




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subir_archivos', methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['archivo']
        filename = f.filename
        f.save(os.path.join('./archivos', filename))
        return "Archivo subido"


if __name__ == '__main__':
    app.run(debug=True, port=3000)