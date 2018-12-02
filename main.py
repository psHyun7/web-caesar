from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

index_form ="""
<!doctype html>
<html>
    <head>
        <style>
            form {
                background-color:#eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
            <label for="rotate-num">Rotate by:</label>
            <input id="rotate-num" type="text" name="rot" value="0"/>
            <textarea name="text"></textarea>
            <input type="submit" />
        </form>
    </body>
</html>
"""

form = 0

@app.route("/")
def index():
    return index_form

@app.route("/encrypt", methods=['POST'])
def encrypt():
    plain_text = request.form['text']
    encrypted = rotate_string(text)
    return encrypted


app.run()