import os
import threeProjs
import kitty

from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)
id = 774437

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/googlef34ca2b18ef9d5d0.html")
def googleVerificationPage():
    return render_template('googlef34ca2b18ef9d5d0.html')

@app.route("/")
def hello():
    l = threeProjs.parse()
    img0 = l[0]['imageURL']
    img1 = l[1]['imageURL']
    img2 = l[2]['imageURL']
    url0 = l[0]['proposalURL']
    url1 = l[1]['proposalURL']
    url2 = l[2]['proposalURL']
    title0 = l[0]['title']
    title1 = l[1]['title']
    title2 = l[2]['title']

    kittyurl =  kitty.getRandom()
    return render_template('index.html', title="Kitties for Kiddies!", img0=img0, img1=img1, img2=img2,
                           url0=url0, url1=url1, url2=url2,
                           title0=title0, title1=title1, title2=title2,
                           desc0 = l[0]['shortDescription'], desc1=l[1]['shortDescription'],
                           desc2 = l[2]['shortDescription'],
                           kittyURL = kittyurl)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
