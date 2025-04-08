from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def truly_yours(page_name):
    return render_template(page_name)

if __name__ == '__main__':
    app.run(host='10.27.27.43',port='8554',debug=True)