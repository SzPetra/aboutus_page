from flask import Flask, render_template

app=Flask(__name__)

@app.route("/aaron")
def aron_page():
	return render_template("aaron.html")

@app.route("/balazs")
def balazs_page():
	return render_template("balazs.html")

@app.route("/imi")
def imi_page():
	return render_template("imi.html")

@app.route("/jeno")
def jeno_page():
	return render_template("jeno.html")

@app.route("/lorand")
def lorand_page():
	return render_template("lorand.html")

@app.route("/miki")
def miki_page():
	return render_template("miki.html")

@app.route("/petra")
def petra_page():
	return render_template("petra.html")

@app.route("/appoint")
def appointment_page():
	return render_template("appoint.html")

@app.route("/rebi")
def rebi_page():
	return render_template("rebi.html")

@app.route("/topic")
def topic_page():
	return render_template("topic.html")

@app.route("/")
def main_page():
	return render_template("aboutus.html")
	
if __name__=="__main__":
	app.run(debug=True, port=8000)
