from flask import Flask
app = Flask(__name__)

@app.route('/')
def helloworld():
    return 'Hello world!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def sayhi(name):
    return f"Hi {name}"

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f"{word} " * num

if __name__=="__main__":
    app.run(debug=True)