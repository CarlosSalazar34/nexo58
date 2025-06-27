from flask import Flask, render_template, request, redirect, url_for
from scripts import enviar_gmail
import os

folder = os.getcwd()

def index():
    if request.method == "POST":
        return redirect(url_for("message-client"))
    return render_template("index.html")


def info():
    if request.method == "GET":
        title = request.args.get("title")
        image = request.args.get("image")
        return render_template("info_product.html", title=title, image = image)

def message_send():
    return render_template("message_send.html")

def message_client():
    if request.method == "POST":
        name = request.form.get("client-name")
        email = request.form.get("client-mail")
        message = request.form.get("message")
        print(name, email, message)
        enviar_gmail(name, message)
        return redirect(url_for("message-send"))

app = Flask(__name__, static_folder=folder, template_folder=folder)


app.add_url_rule("/", "index", index, methods = ["GET", "POST"])
app.add_url_rule("/message-send", "message-send", message_send, methods = {"GET", "POST"})
app.add_url_rule("/infoproduct", "info", info, methods = ["GET", "POST"])
app.add_url_rule("/message-client", "message-client", message_client, methods = ["GET", "POST"])

if __name__ == "__main__":
    # app.run(debug=True, host="192.168.4.134")
    app.run(debug=True)