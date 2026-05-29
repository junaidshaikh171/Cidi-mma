from flask import Flask, render_template

app = Flask(__name__)

fighters = [
    {
        "name": "Junaid Shaikh",
        "wins": 21,
        "losses": 6,
        "weight": "Lightweight"
    },
    {
        "name": "Mohammad Ali",
        "wins": 29,
        "losses": 0,
        "weight": "Lightweight"
    },
    {
        "name": "Mike tyson",
        "wins": 27,
        "losses": 1,
        "weight": "Heavyweight"
    }
]

@app.route('/')
def home():
    return render_template("index.html", fighters=fighters)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
