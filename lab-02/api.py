from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
app = Flask(__name__)

#CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})
@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    ciphertext = data['ciphertext']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt(ciphertext, key)
    return jsonify({'decrypted_text': decrypted_text})

#VIGENERE CIPHER ALGORITHM
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    ciphertext = data['ciphertext']
    key = data['key']
    decrypted_text = vigenere_cipher.decrypt(ciphertext, key)
    return jsonify({'decrypted_text': decrypted_text})

#RAIL FENCE CIPHER ALGORITHM
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    ciphertext = data['ciphertext']
    key = int(data['key'])
    decrypted_text = railfence_cipher.decrypt(ciphertext, key)
    return jsonify({'decrypted_text': decrypted_text})

#PLAYFAIR CIPHER ALGORITHM
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = playfair_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    ciphertext = data['ciphertext']
    key = data['key']
    decrypted_text = playfair_cipher.decrypt(ciphertext, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
