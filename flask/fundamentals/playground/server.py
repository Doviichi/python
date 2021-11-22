from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
def playground():
    return render_template("play.html", num=3)

@app.route('/play/<int:num>')
def play(num):
    return render_template("play.html", num= num)

@app.route('/play/<int:num>/<string:color>')
def changecolor(num, color):
    return render_template("play.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)