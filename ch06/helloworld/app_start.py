from flask import Flask
app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello world"

@app.route("/led/on")
def led_on():
    return "LED ON"

@app.route("/led/off")
def led_off():
    return "LED OFF"

if __name__ == "__maiN__":
    app.run(host="0.0.0.0")