from flask import Flask, render_template, request
import requests

app=Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/weather',methods=['POST','GET'])
def get_weatherdata():
    apikey='1dc16a3869dcfbcd6d2bab589e28f09f'
    url='https://api.openweathermap.org/data/2.5/weather'
    param={
        'q':request.form.get('city'),
        'appid':apikey,
        'units':request.form.get('units'),
        
    }
    responce=requests.get(url,param)
    data=responce.json()
    return f'Data: {data}'

if __name__ == '__main__':
    app.run('0.0.0.0',port=8000)
