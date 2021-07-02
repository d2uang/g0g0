from flask import Flask, redirect, request
import requests

app = Flask(__name__)
website = 'https://www.google.com'
@app.route("/")
def home():
    return requests.get(website).content

# @app.route('/<allurl>')
# def redirect_to_link(allurl):
#     return "allurl"


@app.errorhandler(404)
def page_not_found(e):
    return requests.get(f"{website}{request.full_path}").content

if __name__ == "__main__":
    app.run()