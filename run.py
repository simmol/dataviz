from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from app import default_page

app = Flask(__name__, template_folder="templates")

app.debug = True
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = '8)^@%4$x$goajwz)gg-w79f*38u=tfl$4#p8q8#61u_8)n5-k#'
toolbar = DebugToolbarExtension(app)

# Register Blueprints
app.register_blueprint(default_page)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8088, debug=True)
