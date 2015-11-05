from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def main():
return render_template("main.html")

@app.route('/aboutme')
def aboutme():
return render_template("aboutme.html")

@app.route('/contactme')
def contactme():
return render_template("contactme.html")


if __name__ == "__main__":
	app.run()
