from flask import Flask, render_template, send_file
import csv
import pandas as pd
import os

app = Flask(__name__)

df = pd.read_csv('cleaned_table.csv')
data = df.values.tolist()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/IN')
def IN():
    return render_template('home.html')


@app.route('/DataA')
def DAA():
    df1 = pd.read_csv('datasample.csv')
    data1 = df1.iloc[[173, 249], 0:7].values.tolist()
    columns1 = list(df1.columns)[0:7]
    data1.insert(0, columns1)
    return render_template('DataA.html', data=data1)

@app.route('/DataM')
def DAM():
    return render_template('DataM.html')


@app.route('/Fin')
def FIN():
    df = pd.read_csv('cleaned_table.csv', header=0)

    data = df.values.tolist()[:50]
    columns = list(df.columns)
    data.insert(0, columns)
    return render_template('Fin.html', data=data)

@app.route('/Eva')
def EVA():
    return render_template('Eva.html')

@app.route('/Conclu')
def CON():
    return render_template('Conclu.html')

@app.route('/csv')
def csv():
    return send_file('cleaned_table.csv', as_attachment=True)


if __name__ == '__main__':
    app.run(port=5000)


