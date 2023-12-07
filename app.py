from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/guest/<Mina>")
def hello_guest(guest):
  return f"<h1>Hello, {guest}</h1>"

@app.route("/page/<id>")
def display_page(id):
  return f"<h1>Hello, {id}</h1>"

@app.route("/showpage/<int:page>")
def show_page(page):
 return f"<h1>It is a page number: {page}<)h1>"

@app.route('/')
def index():
    return render_template("myhtml.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5500, debug=True)
