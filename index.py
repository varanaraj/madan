from concurrent.futures import thread
from threading import Thread
from flask import Flask
import uploadvideo
import os

app=Flask(__name__)

@app.route("/")
def upload():
    thread_a=Thread(target=uploadvideo.Run(),args={})

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)