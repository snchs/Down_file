from flask import Flask, render_template ,request

app = Flask(__name__)

file_dir = 'static/img/img_1.png'
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    global file_dir
    if request.method == 'GET':
        return render_template('base.html', dir_img=file_dir)
    elif request.method == 'POST':
        dir_img = request.files['file']
        dir_img.save('static/img/' + dir_img.filename)
        return render_template('base.html', dir_img=('static/img/' + dir_img.filename))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
