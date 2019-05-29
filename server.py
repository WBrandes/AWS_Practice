from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main_page():
	return render_template("home.html")
	#return("<img src='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'/>")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
