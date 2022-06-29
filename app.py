from flask import Flask, render_template, request, redirect, url_for
from transaction import Transaction

app = Flask(__name__)

transaction_log = []

def get_max_transaction_id():
    try:
        transaction_ids = [t['id'] for t in transaction_log]
        max_id = transaction_ids[-1]
    except IndexError:
        max_id = 0
    return max_id

def get_transaction_details(id):
    try:
        transaction_details = [t for t in transaction_log if t.id == id][0]
    except:
        transaction_details = None
    return transaction_details

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/submit-transaction', methods = ['GET', 'POST'])
def submit_transaction():
    if request.method == 'POST':
        transaction_id = get_max_transaction_id() + 1
        transaction = Transaction(transaction_id, 
                                  request.form['desc'],
                                  request.form['amount'],
                                  request.form['location'])
        transaction_log.append(transaction)
        return redirect(url_for('submit_success', id=transaction_id))
    return render_template('transaction.html')

@app.route('/submit-success/<int:id>')
def submit_success(id):
    transaction = get_transaction_details(id=id)
    return render_template('success.html', transaction=transaction)

@app.route('/view-all-transactions')
def view_all_transactions():
    return "All transactions"

if __name__ == '__main__':
    pass
