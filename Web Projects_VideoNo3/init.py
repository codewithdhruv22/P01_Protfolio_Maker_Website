from flask import Flask,render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/design")
def design():
    return render_template("design.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/upload", methods = ["GET","POST"])
def upload():
    if request.method == "POST":
        name = request.form.get("firstname")
        lastname = request.form.get("lastname")
        school = request.form.get("school")
        college = request.form.get("college")
        phone = request.form.get("phone")
        email = request.form.get("email")
        skill1 = request.form.get("skill1")
        skill2 = request.form.get("skill2")
        skill3 = request.form.get("skill3")
        skill4 = request.form.get("skill4")
        about = request.form.get("about")

        print(name )
        print(lastname )
        print(school)
        print(college )
        print(phone )
        print(email )
        print(skill1 )
        print(skill2 )
        print(skill3 )
        print(skill4 )
        print(about)
    return "Uploaded"
        
app.run(debug= True)