# -*- coding: utf-8 -*-
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template_string("""
    <!doctype html>
    <html>
    <head>
        <title>ELVIN!</title>
        <style>
            @keyframes backgroundChange {
                0%   {background-color: blue;}
                25%  {background-color: red;}
                50%  {background-color: green;}
                75%  {background-color: yellow;}
                100% {background-color: blue;}
            }
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                animation: backgroundChange 10s infinite;
                color: white;
                font-size: 48px;
                font-weight: bold;
                font-family: 'Arial', sans-serif;
            }
        </style>
    </head>
    <body>
        Test 1
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
