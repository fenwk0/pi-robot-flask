# Alexabot is Alexabot: Amazon Alexa Controlled Robot With the Raspberry Pi
#
# This file is the flask server that listens for commands from Alexa.
# You can see the full project here: https://www.dexterindustries.com/projects/alexabot-amazon-alexa-controlled-robot/
# In this tutorial we build Alexabot, the Amazon Alexa Controlled Robot, using the Raspberry Pi.  
# We will walk through the steps of building a voice controlled robot with the Raspberry Pi and GoPiGo.  
# With Alexabot, you can command the Raspberry Pi Robot around with commands like "Alexa Forward!" or "Alexa Coffee!".
#
# See more about Dexter Industries at http://www.dexterindustries.com
# See more about the GoPiGo at http://www.dexterindustries.com/gopigo

from flask import Flask, g
import gopigo
import time

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'


@app.route('/start')
def start():
    return 'Lets crack on'


@app.route('/stop')
def stop():
    gopigo.stop()
    return 'Stop'


@app.route('/forward/', defaults={'step': 1})
@app.route('/forward/<step>')
def forward(step):
    if int(step) <= 20:
        print("Forward: " + str(step))
        gopigo.fwd()
        time.sleep(int(step) * 0.5)  # sleep for step * 0.5 second.
        gopigo.stop()
        return 'Bot moved forward!'
    else:
        error_message = "Invalid forward command or value is > 20"
        print(error_message)
        return error_message


@app.route('/backward')
def backward():
    print("Backward!")
    gopigo.bwd()  # Send the GoPiGo Backward
    time.sleep(1)  # for 1 second
    gopigo.stop()  # and then stop the GoPiGo.
    return 'Backward!'


@app.route('/left')
def left():
    print("Left!")
    gopigo.left()
    time.sleep(1)
    gopigo.stop()
    return 'Left!'


@app.route('/right')
def right():
    print("Right!")
    gopigo.right()
    time.sleep(1)
    gopigo.stop()
    return 'Right!'


@app.route('/dance')
def dance():
    print("Dance!")
    for each in range(0, 5):
        gopigo.right()
        time.sleep(0.25)
        gopigo.left()
        time.sleep(0.25)
        gopigo.bwd()
        time.sleep(0.25)
    gopigo.stop()
    return 'Dance!'


@app.route('/coffee')
def coffee():
    print("Coffee!")
    return 'coffee!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
