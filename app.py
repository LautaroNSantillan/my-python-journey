from flask import Flask,render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def hello_world():
    req_method = request.method
    if req_method == 'POST':
        first_name = request.form['first_name']
        return redirect(url_for("name", first_name=first_name))
    return render_template('req.html', request_method=req_method)


@app.route('/name/<string:first_name>')
def name(first_name):
    return f'{first_name}'


if __name__ == '__main__':
    app.run(debug=True)  # production : false
