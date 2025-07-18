from flask import Flask, render_template, request
from servo_controller import setServoAngle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', method = ['POST'])
def move():
    servo = int(request.form['servo'])
    angle = int(request.form['angle'])

    return ('', 204)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)