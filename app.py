from flask import Flask,render_template, request
from datetime import datetime
app=Flask(__name__)

@app.route("/")
def index():
        
        return "welcome"

@app.route("/hello")
def hello():
	    print(request.args)
        name="nisha"
        data=[
                [ "ram",9,9],
                ["shyam",8,9],
                ["ravi",10,10]
                ]
        return render_template("test.html",name=name,now=datetime.now().strftime("%d %B, %Y %I : %M %p"))

@app.route("/form",methods=['GET','POST'])
def form():
	if request.method=='GET':
		return render_template("form.html")
	else:
		name=request.form.get('name')
		clas =request.form.get('class')
		image=request.files.get('image')
		ext=image.filename.split('.')[-1]
		image.save("static/images/{}.{}".format(name,ext))
		return "your name is {} and class is {}".format(name,clas)

if __name__=="__main__":
        app.run(use_reloader=True,debug= True)
