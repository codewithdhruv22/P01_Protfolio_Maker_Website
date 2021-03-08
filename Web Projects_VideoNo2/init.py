from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/design")
def design():
    return render_template("design.html")

app.run(debug= True)