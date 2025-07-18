from flask import Flask, render_template, request
from servo_controller import setServoAngle

app = Flask(__name__)

currentAngles = {0: 95, 1: 90}

@app.route('/')
def index():
    return render_template('index.html', angles = currentAngles)

@app.route('/move', methods = ['POST'])
def move():
    servo = int(request.form['servo'])
    angle = int(request.form['angle'])
    setServoAngle(servo, angle)
    currentAngles[servo] = angle
    return render_template('index.html', angles = currentAngles)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)
