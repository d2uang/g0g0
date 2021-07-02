from flask import Flask, redirect, request
import requests

app = Flask(__name__)
website = 'https://www.google.com'
@app.route("/")
def home():
    linkurl = request.full_path
    if linkurl.count("?&&="):
        web = linkurl.split("?&&=", 1)[1]
        return requests.get(web).content
    else:
        return redirect(f"?&&={website}", code=302)

# @app.route('/newlink')
# def redirect_to_link():
#     domain = linkurl.split("?&&=", 1)[1]
#     # return domain
#     return requests.get(f"{domain}{request.full_path}").content
# # /url?q=https://medium.com/

# print(linkurl.full_path.count("/url?q=https://"))
@app.errorhandler(404)
def page_not_found(e):
    linkurl = request.full_path
    if linkurl.count("?&&=") < 1:
        domain = request.headers.get("Referer")
        domain = domain.split("?&&=", 1)[1]
        # linkurl = linkurl.split("?&&=", 1)[1]
        return redirect(f"{request.full_path}?&&={domain}", code=302)
    elif linkurl.count("/url?q=https://"):
        linkurl = linkurl.split("/&sa=U&", 1)[0].split("url?q=", 1)[1]
        relink = f"../?&&={linkurl}"
        # return f"<meta http-equiv='refresh' content='time; URL={relink}' />"
        # return relink
        return redirect(relink, code=302)

    else:
        domain = request.headers.get("Referer")
        domain = domain.split("?&&=", 1)[1]
        # linkurl = linkurl.split("?&&=", 1)[1]
        # return domain
        return requests.get(f"{domain}{request.full_path}").content

if __name__ == "__main__":
    app.run()