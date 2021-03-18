#Download All other project files from here  - https://drive.google.com/drive/folders/1attt_nMSNHVO-KDT9Bf75UaltYv7_JWY?usp=sharing

from flask import Flask,render_template, request
import uuid
import os
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

        key = uuid.uuid1()
        #Image Uploading Method
        img = request.files["dp"]
        img.save(f"static/images/{img.filename}")
        img_new_name = f"{key}{img.filename}"
        os.rename(f"static/images/{img.filename}",f"static/images/{img_new_name}")
    return render_template("Design1.html",dname = name,dlname = lastname,dsch = school,img = img_new_name, dcol = college,dph = phone,demail = email,ds1 = skill1,ds2 = skill2,ds3 =skill3,ds4 = skill4,dabout = about)

        
if __name__ == "__main__":
    app.run(debug=True)

