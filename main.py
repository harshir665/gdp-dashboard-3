from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url).json()
    return response['bitcoin']['usd']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/btc-price')
def btc_price():
    price = get_btc_price()
    return jsonify({"price": price})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)