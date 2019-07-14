from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime
from pytz import timezone    

app = Flask(__name__)

def get_french_time():
    paris = timezone('Europe/Paris')
    pa_time = datetime.now(paris)
    #return pa_time.strftime('%Y-%m-%d_%H-%M-%S')
    return pa_time.strftime('%H : %M')


@app.route("/", methods=["GET"])
def home_page():
    #var1 = datetime.datetime.now()
    var1 = get_french_time()

    return render_template("frenchtime.html", dynamiccontent=var1)


if __name__ == "__main__":
    app.run(debug=True)  