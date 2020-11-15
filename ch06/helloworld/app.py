from flask import Flask,request
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
app = Flask(__name__)

LED=8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

@app.route("/")
def helloworld():
    return "Hello world"

@app.route("/led")
def led():
    state = request.values.get("state","error")
    if state == "on":
        GPIO.output(LED,GPIO.HIGH)
    elif state == "off":
        GPIO.output(LED,GPIO.LOW)
    elif state == "error":
        return "Not Good State"
    else:
        return "Wrong Query String"
    return "LED"+state

@app.route("/led/on")
def led_on():
    GPIO.output(LED,GPIO.HIGH)
    return "LED ON"

@app.route("/led/off")
def led_off():
    GPIO.output(LED,GPIO.LOW)
    return "LED OFF"

@app.route("/gpio/cleanup")
def gpio_cleanup():
    GPIO.cleanup()
    return "GPIO CLEANUP"

if __name__ == "__maiN__":
    app.run(host="0.0.0.0")