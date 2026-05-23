from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# --------------------- MAIN ROUTE ---------------------
@app.route("/")
def home():
    return render_template('index.html')
# --------------------- ROUTES CAESAR ---------------------
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt(text, key)
    return f"text: {text}<br>/key: {key}<br>/encrypted text: {encrypted_text}"

@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt(text, key)
    return f"text: {text}<br>/key: {key}<br>/decrypted text: {decrypted_text}"

# --------------------- MAIN FUNCTION ---------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
