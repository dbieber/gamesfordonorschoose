import os
import featuredProj
import kitty
from flask import Flask
from flask import render_template
app = Flask(__name__)
id = 774437

@app.route("/googlef34ca2b18ef9d5d0.html")
def googleVerificationPage():
    return render_template('googlef34ca2b18ef9d5d0.html')

@app.route("/")
def hello():
    url = featuredProj.parse(id)
    kittyurl =  kitty.getRandom()
    return render_template('index.html', title="Kitties for Kiddies!", imageURL=url, kittyURL = kittyurl)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
