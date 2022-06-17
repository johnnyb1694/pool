from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/submit-transaction', methods = ['GET', 'POST'])
def submit_transaction():
    if request.method == 'POST':
        print('Posting transaction...')
        desc = request.form['desc']
        print(desc)
    else:
        print('Getting transaction page...')
    return render_template('transaction.html')