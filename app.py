from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print('somelgthrng')
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
