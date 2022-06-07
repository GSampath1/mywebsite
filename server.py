import os 
from flask import Flask, redirect, url_for, render_template, request,make_response
from threading import Thread
import requests
import json

app = Flask(__name__,
template_folder="template")
app.static_folder = 'static'

@app.errorhandler(404)
async def page_not_found(error):
    return redirect("/404")

@app.route("/404")
async def error404():
    return render_template('404.html'), 404

@app.route("/support")
async def support(): 
        return redirect('https://discord.gg/rcYh8zfTz4')

@app.route("/")
async def home():
    return render_template('index.html')

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)    