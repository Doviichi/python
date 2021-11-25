from flask import Flask, render_template, request, redirect, session
app = Flask('__name__')

app.secret_key = 'ber'


@app.route('/')
def index():
    if 'count' not in session: 
        session['count'] = 0 
    else:
        session['count'] += 1
    print (request.form)
    return render_template('index.html')


@app.route('/count', methods=['POST'])
def count():
    session['count']+=int(request.form['add_count'])
    session['count'] += int(request.form['number'])
    print('number added. total count', session['count'])
    return redirect('/')



@app.route('/clear', methods=['post'])
def clear():
    if 'count' in session:
        session['count'] = 0
        print ('cleared', session['count'])
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)