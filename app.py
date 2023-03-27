from flask import *
import time
import os

app = Flask(__name__,static_url_path='', static_folder='frontend/static',template_folder='frontend/templates')
port = int(os.environ.get("PORT", 5454))
# os.system('npx tailwindcss -i ./frontend/static/css/src/input.css -o ./frontend/static/css/dist/output.css')

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)