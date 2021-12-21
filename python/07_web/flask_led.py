from flask import Flask
import RPi.GPIO as GPIO

RED_LED_PIN = 4
BLUE_LED_PIN = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''
    <p>Hello, Flask!</p><a href='/led/red/on'>RED LED ON</a> <a href='/led/red/off'>RED LED OFF</a>
    <a href='/led/blue/on'>BLUE LED ON</a> <a href='/led/blue/off'>BLUE LED OFF</a>
    '''

@app.route("/led/<color>/<op>")
def led_op(color, op):
    if color == 'red':
        LED_PIN = RED_LED_PIN
    else:
        LED_PIN = BLUE_LED_PIN
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return "<p>LED ON</p><a href='/'>GO HOME</a>"
    elif op == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return "<p>LED OFF</p><a href='/'>GO HOME</a>"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()