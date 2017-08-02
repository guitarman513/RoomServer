from flask import Flask, render_template

app = Flask(__name__)

#CONSTANTS FOR TAB AND URL NAMES
tab1 = 'Lights'
tab2 = 'VLC'
tab3 = 'Door Lock'



@app.route('/')
def index():
    return render_template('main.html')

#lights
@app.route('/Lights/')
@app.route('/lights/')
def firstTab():
    return render_template('lights.html')

#Door Lock
@app.route('/VLC/')
@app.route('/vlc/')
def secondTab():
    return render_template('vlc.html')

#T.V.
@app.route('/doorlock/')
@app.route('/DoorLock/')
def thirdTab():
    return render_template('doorLocks.html')



############### 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('notFound.html'), 404















if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
