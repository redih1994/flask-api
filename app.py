from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():

    data = pd.read_csv("data_small/stations.txt", skiprows=17)

    return render_template("home.html", data=data.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == f"{date}"]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}

@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")
    return result

@app.route("/api/v1/annual/<station>/<year>")
def year_data(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df["    DATE"] = df["    DATE"].astype(str).str[:4].astype(int)
    df = df.loc[df["    DATE"] == int(year)]
    result = df.to_dict(orient="records")
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5011)