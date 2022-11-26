from flask import Flask, render_template, request
from pkgs import scraper

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def test():

    if request.method == 'GET':
        return render_template('index.html')
    
    content = scraper.fetch_content(request.form['url'])

    if content:
        return render_template('content/content.html',content=content)
    
    return render_template('index.html')