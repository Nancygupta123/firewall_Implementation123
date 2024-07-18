from flask import Flask, render_template, request, redirect, url_for, session
from Firewall.strategy_factory import StrategyFactory
from Config.settings import Settings

app = Flask(__name__)
app.secret_key = 'your_secret_key'

settings = Settings()

# Dummy admin credentials
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect(url_for('home'))
        else:
            return "Invalid credentials"
    return render_template('index.html')

@app.route('/home')
def home():
    if 'admin' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/set_rules', methods=['GET', 'POST'])
def set_rules():
    if 'admin' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        ip = request.form.get('ip')
        list_type = request.form.get('list_type')
        if list_type == 'whitelist':
            settings.add_to_whitelist(ip)
        elif list_type == 'blacklist':
            settings.add_to_blacklist(ip)
    return render_template('set_rules.html')

@app.route('/display_lists')
def display_lists():
    if 'admin' not in session:
        return redirect(url_for('login'))
    whitelist = settings.get_whitelist()
    blacklist = settings.get_blacklist()
    return render_template('display_lists.html', whitelist=whitelist, blacklist=blacklist)

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
