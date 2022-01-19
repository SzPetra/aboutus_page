from flask import Flask, render_template

app=Flask(__name__)

@app.route("/aaron")
def aron_page():
	return render_template("aaron.html")

@app.route("/")
def main_page():
	return render_template("aboutus.html")
	
if __name__=="__main__":
	app.run(debug=True, port=5000)
