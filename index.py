from flask import Flask
import os
import bs4
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = requests.get("https://en.m.wikipedia.org/wiki/List_of_authors_of_names_published_under_the_ICZN#I")
    soup = bs4.BeautifulSoup(url.content,"html5lib")
    resu = soup.findAll("b")
    return str(resu)+"\n"

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port,debug=True)


