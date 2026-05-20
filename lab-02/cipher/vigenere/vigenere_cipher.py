from string import ascii_uppercase


class VigenereCipher:
    def __init__(self):
        self.alphabet = list(ascii_uppercase)

    def _clean_key(self, key: str) -> str:
        key = ''.join(letter for letter in key.upper() if letter in self.alphabet)
        if not key:
            raise ValueError('Key must contain at least one letter')
        return key

    def encrypt(self, text: str, key: str) -> str:
        key = self._clean_key(key)
        encrypted_text = []
        key_index = 0

        for letter in text.upper():
            if letter not in self.alphabet:
                encrypted_text.append(letter)
                continue

            text_index = self.alphabet.index(letter)
            shift = self.alphabet.index(key[key_index % len(key)])
            encrypted_text.append(self.alphabet[(text_index + shift) % len(self.alphabet)])
            key_index += 1

        return ''.join(encrypted_text)

    def decrypt(self, ciphertext: str, key: str) -> str:
        key = self._clean_key(key)
        decrypted_text = []
        key_index = 0

        for letter in ciphertext.upper():
            if letter not in self.alphabet:
                decrypted_text.append(letter)
                continue

            text_index = self.alphabet.index(letter)
            shift = self.alphabet.index(key[key_index % len(key)])
            decrypted_text.append(self.alphabet[(text_index - shift) % len(self.alphabet)])
            key_index += 1

        return ''.join(decrypted_text)
