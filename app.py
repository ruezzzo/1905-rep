"""
Админ-панель аналитики колледжа в Instagram и 2GIS.
Колледж: Инновационный Технический колледж (ИТК)
"""
from flask import Flask, render_template, jsonify
from data import get_dashboard_data, get_recommendations

app = Flask(__name__)


@app.route("/")
def index():
    data = get_dashboard_data()
    recs = get_recommendations(data)
    return render_template("index.html", data=data, recommendations=recs)


@app.route("/api/data")
def api_data():
    return jsonify(get_dashboard_data())


@app.route("/api/recommendations")
def api_recs():
    return jsonify(get_recommendations(get_dashboard_data()))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
