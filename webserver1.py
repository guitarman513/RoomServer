from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'localhost'  # use the free broker from HIVEMQ
app.config['MQTT_BROKER_PORT'] = 1883  # default port for non-tls connection
#app.config['MQTT_USERNAME'] = ''  # set the username here if you need authentication for the broker
#app.config['MQTT_PASSWORD'] = ''  # set the password here if the broker demands authentication
app.config['MQTT_KEEPALIVE'] = 5  # set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_TLS_ENABLED'] = False  # set TLS to disabled for testing purposes

mqtt = Mqtt(app)
socketio = SocketIO(app)




@app.route('/')
def main():
    return render_template('html/main.html')

#VLC
@app.route('/VLC/')
@app.route('/vlc/')
def firstTab():
    return render_template('html/VLC.html')


############### 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('html/notFound.html'), 404

##################################################################################
@app.route("/LED/color/<color>")
def action(color):

    message = color
    mqtt.publish("LED/color",message)

    return render_template('html/main.html')

##################################################################################

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
