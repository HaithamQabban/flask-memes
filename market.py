from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

def get_random_meme():
    response = requests.get('https://www.reddit.com/r/memes/random.json', headers={'User-Agent': 'Mozilla/5.0'})
    data = response.json()
    meme_url = data[0]['data']['children'][0]['data']['url']
    return meme_url

@app.route("/")
def index():
    meme_url = get_random_meme()
    return render_template("index.html", meme_url=meme_url)

@app.route("/change_meme")
def change_meme():
    meme_url = get_random_meme()
    return {"meme_url": meme_url}

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
