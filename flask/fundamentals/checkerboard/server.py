from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def checkers():
    return render_template('checkers.html', col=8, row=8, color_one="red", color_two="black")


@app.route('/<int:col>')
def number(col):
    return render_template('checkers.html', row=8, col=col, color_one="red", color_two="black")


@app.route('/<int:row>/<int:col>/<color_one>/<color_two>')
def color(row, col, color_one, color_two):
    return render_template('checkers.html', row=row, col=col, color_one=color_one, color_two=color_two)

if __name__=="__main__":
    app.run(debug=True)