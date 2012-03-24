import os
import featuredProj
from flask import Flask
from flask import render_template
app = Flask(__name__)
id = 774437
@app.route("/")
def hello():
    url = featuredProj.parse(id)
    return render_template('temp.html', title="Default title!", imageURL=url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
