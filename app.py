# Save this as app.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def handle_submit():
    data = request.form  # This captures the form data
    return f"Form submitted! Name: {data.get('fname')} Surname: {data.get('sname')}"

if __name__ == "__main__":
    app.run(debug=True)
