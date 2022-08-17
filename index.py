from flask import Flask, render_template, request, Response, redirect, send_file
import os
from os import remove
import pafy

app = Flask(__name__)
path=os.getcwd() + '/static/'

@app.route('/')
def route():
    return render_template('index.html')

@app.route('/downloadMP4', methods=['GET', 'POST'])
def downloadMP4():
    if request.method == 'POST':
        url = request.form.get("url")
        video = pafy.new(url)
        best = video.getbest(preftype="mp4")
        best.download(path)
        p = path + video.title + '.mp4'

    return send_file(p, as_attachment=True)

@app.route('/downloadMP3', methods=['GET', 'POST'])
def downloadMP3():
    if request.method == 'POST':
        url = request.form.get("url")
        video = pafy.new(url)
        best = video.getbestaudio()
        best.download(path)
        p = path + video.title + '.webm'

    return send_file(p, as_attachment=True)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)




