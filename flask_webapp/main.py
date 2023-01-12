import os

from flask import (
    Flask, render_template, url_for, request, redirect, flash, send_file
    )

from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import FileField, SelectField
from wtforms.validators import DataRequired

import pickle
import pandas as pd

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)


class UploadForm(FlaskForm):
    file = FileField(label="Please upload your data", validators=[DataRequired()])


@app.route('/', methods=('GET', 'POST'))
def home():
    return redirect(url_for('batch'))

@app.route('/batch', methods=('GET', 'POST'))
def batch():
    uploadform = UploadForm()

    if not os.path.exists(os.getcwd() + '/uploads'):
        os.makedirs(os.getcwd() + '/uploads')
    uploads = os.listdir(os.getcwd() + '/uploads')

    class SelectForm(FlaskForm):
        select = SelectField(label="Choose File", choices=uploads, validators=[DataRequired()])

    selectform = SelectForm()

    if request.method == 'POST':
        if uploadform.file.data:
            filename = secure_filename(uploadform.file.data.filename)
            uploadform.file.data.save('uploads/' + filename)
            flash('Upload success!')

        data_file_name = selectform.data['select']
        if data_file_name:
            data_input = pd.read_csv(
                os.getcwd() + '/uploads/' + data_file_name, 
                index_col=0).squeeze().to_list()

            model = pickle.load(open('model.pkl', 'rb'))
            res = model.predict(data_input)
            df = pd.DataFrame({
                'Complaints': data_input, 
                'Monetary or not?': res})
            df.index += 1 # shift index by 1 to start index from 1 for display
            if not os.path.exists(os.getcwd() + '/results'):
                os.makedirs(os.getcwd() + '/results')
            df.to_csv(f'./results/{data_file_name.split(".")[0]}_pred_results.csv')
            flash('Results saved!')
            return render_template(
                'batch.html', 
                uploadform=uploadform, 
                selectform=selectform, 
                df=df.to_html(classes='table table-striped table-hover')
                )
    return render_template('batch.html', uploadform=uploadform, selectform=selectform)


@app.route('/single', methods=('GET', 'POST'))
def single():
    if request.method == 'POST':
        text = request.form['single_complaint']
        data_input = [text]
        model = pickle.load(open('model.pkl', 'rb'))
        res = model.predict(data_input)
        df = pd.DataFrame({
            'Complaints': data_input, 
            'Monetary or not?': res})
        df.index += 1
        return render_template('single.html', df=df.to_html(classes='table table-striped table-hover'))
    return render_template('single.html')

@app.route('/download/', methods=('GET', 'POST'))
def download():
    if not os.path.exists(os.getcwd() + '/results'):
        os.makedirs(os.getcwd() + '/results')
    results = os.listdir(os.getcwd() + '/results')
    return render_template('dowload.html', results=results)

@app.route('/download/<file>', methods=('GET', 'POST'))
def send(file):
    path='./results/' + file
    return send_file(path)

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
