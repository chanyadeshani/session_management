from flask import Flask, render_template, request
from flask import session


app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'  # It's important to ensure that the secret key remains a secret that cannot be easily guessed.


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            print(f'{key}: {value}')

        # Can get name of the user from database here
        user_name = request.form['user_name']
        password = request.form['password']
        confirm_password = request.form['confirm_password']


        return render_template('login.html')
    else:
        return render_template("register.html")


# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            print(f'{key}: {value}')

            # Can get name of the user from database here
        session['user_id'] = request.form['user_id'],

        return render_template('dashboard.html')

    return render_template("login.html")


@app.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        # Print the form data to the console
        for key, value in request.form.items():
            print(f'{key}: {value}')

            # Save the form data to the session object
            session['stock_symbol'] = request.form['stock_symbol']
            session['number_of_shares'] = request.form['number_of_shares']
            session['purchase_price'] = request.form['purchase_price']


    return render_template('add_stocks.html')


@app.route('/stocks/')
def list_stocks():
    return render_template('stocks.html')


@app.get('/about')
def about():
    return '<h2>About this application...</h2>'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
