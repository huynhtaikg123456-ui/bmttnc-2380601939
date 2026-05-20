from string import ascii_uppercase


class PlayfairCipher:
    def __init__(self):
        self.alphabet = ascii_uppercase.replace('J', '')

    def encrypt(self, text: str, key: str) -> str:
        matrix = self._create_matrix(key)
        pairs = self._prepare_plain_text(text)
        encrypted_text = []

        for first, second in pairs:
            row1, col1 = self._find_position(matrix, first)
            row2, col2 = self._find_position(matrix, second)

            if row1 == row2:
                encrypted_text.append(matrix[row1][(col1 + 1) % 5])
                encrypted_text.append(matrix[row2][(col2 + 1) % 5])
            elif col1 == col2:
                encrypted_text.append(matrix[(row1 + 1) % 5][col1])
                encrypted_text.append(matrix[(row2 + 1) % 5][col2])
            else:
                encrypted_text.append(matrix[row1][col2])
                encrypted_text.append(matrix[row2][col1])

        return ''.join(encrypted_text)

    def decrypt(self, ciphertext: str, key: str) -> str:
        matrix = self._create_matrix(key)
        pairs = self._prepare_cipher_text(ciphertext)
        decrypted_text = []

        for first, second in pairs:
            row1, col1 = self._find_position(matrix, first)
            row2, col2 = self._find_position(matrix, second)

            if row1 == row2:
                decrypted_text.append(matrix[row1][(col1 - 1) % 5])
                decrypted_text.append(matrix[row2][(col2 - 1) % 5])
            elif col1 == col2:
                decrypted_text.append(matrix[(row1 - 1) % 5][col1])
                decrypted_text.append(matrix[(row2 - 1) % 5][col2])
            else:
                decrypted_text.append(matrix[row1][col2])
                decrypted_text.append(matrix[row2][col1])

        return ''.join(decrypted_text)

    def _create_matrix(self, key: str) -> list[list[str]]:
        clean_key = self._clean_text(key)
        seen = set()
        letters = []

        for letter in clean_key + self.alphabet:
            if letter not in seen:
                seen.add(letter)
                letters.append(letter)

        return [letters[index:index + 5] for index in range(0, 25, 5)]

    def _prepare_plain_text(self, text: str) -> list[tuple[str, str]]:
        text = self._clean_text(text)
        pairs = []
        index = 0

        while index < len(text):
            first = text[index]
            second = text[index + 1] if index + 1 < len(text) else 'X'

            if first == second:
                pairs.append((first, 'X'))
                index += 1
            else:
                pairs.append((first, second))
                index += 2

        return pairs

    def _prepare_cipher_text(self, ciphertext: str) -> list[tuple[str, str]]:
        ciphertext = self._clean_text(ciphertext)
        if len(ciphertext) % 2 != 0:
            ciphertext += 'X'
        return [(ciphertext[index], ciphertext[index + 1]) for index in range(0, len(ciphertext), 2)]

    def _clean_text(self, text: str) -> str:
        return ''.join(
            'I' if letter == 'J' else letter
            for letter in text.upper()
            if letter.isalpha()
        )

    def _find_position(self, matrix: list[list[str]], letter: str) -> tuple[int, int]:
        for row_index, row in enumerate(matrix):
            if letter in row:
                return row_index, row.index(letter)
        raise ValueError(f'{letter} is not in the Playfair matrix')
