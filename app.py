from flask import Flask, render_template, request
import requests, validators

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        if validators.url(long_url):
            shortened_url = shorten(long_url)
            return render_template('index.html', url = shortened_url)
        else:
            return render_template('index.html',  invalid_url = "Invalid URL")
    else:
        return render_template('index.html')

def shorten(long_url):
    key = '65ed6d05dfa9df611ae9e3d42e74c7722932e'
    name  = ''
    r = requests.get('http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key, long_url, name))

    y = r.json()
    shortened_url = y["url"]["shortLink"]

    return shortened_url


    
    
    
