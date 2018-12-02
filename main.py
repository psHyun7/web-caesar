from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form ="""
<!doctype html>
<html>
    <head>
        <style>
            form {{
                background-color:#eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
            <label for="rotate-num">Rotate by:</label>
            <input id="rotate-num" type="text" name="rot" value="0"/>
            <textarea name="text">{0}</textarea>
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/encrypt", methods=['POST'])
def encrypt():
    plain_text = request.form['text']
    rotation = int(request.form['rot'])
    encrypted = rotate_string(plain_text, rotation)
    return_value = "<h1>" + encrypted + "</h1>"
    return form.format(encrypted)


app.run()