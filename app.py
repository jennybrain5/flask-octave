#!/usr/bin/python
from flask import Flask, request
import subprocess, requests

app = Flask(__name__)
# INICIO codigo comentado 1

@app.route('/')
def default():
	
	#file = requests.get(url, stream=True)
	#dump = file.raw
    return 'Octave+Flask Web Service<BR><BR>To generate PNG figure add this to the current URL:<BR>/genfig?script=<b>URL_TO_SCRIPT</b>&id=<b>FIGUIRE_PARAMETER</b>&name=<b>FIGURE_NAME</b><BR>Example:http://192.168.99.100:5000/genfig?url=https://goo.gl/QQhXZi&id=10&name=oct_fig.png'
	
@app.route('/genfig')
def gen_figure():
   path_script=request.args.get('url')
   task_id=request.args.get('id')
   figure_name=request.args.get('name')
   file = requests.get(path_script, allow_redirects=True)
   open('script.octave', 'wb').write(file.content)
   cmd=['octave','-q','script.octave',task_id,figure_name]
   p=subprocess.Popen(cmd, stdout = subprocess.PIPE)
   out, err = p.communicate()
   #return out
   return 'File generated Successfully'
   

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')