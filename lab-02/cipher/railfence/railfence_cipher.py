class RailFenceCipher:
    def encrypt(self, text: str, key: int) -> str:
        if key <= 1 or key >= len(text):
            return text

        rails = ['' for _ in range(key)]
        rail = 0
        direction = 1

        for char in text:
            rails[rail] += char
            rail += direction

            if rail == 0 or rail == key - 1:
                direction *= -1

        return ''.join(rails)

    def decrypt(self, ciphertext: str, key: int) -> str:
        if key <= 1 or key >= len(ciphertext):
            return ciphertext

        pattern = self._build_pattern(len(ciphertext), key)
        rail_lengths = [pattern.count(rail) for rail in range(key)]

        rails = []
        index = 0
        for length in rail_lengths:
            rails.append(list(ciphertext[index:index + length]))
            index += length

        rail_positions = [0 for _ in range(key)]
        decrypted_text = []

        for rail in pattern:
            decrypted_text.append(rails[rail][rail_positions[rail]])
            rail_positions[rail] += 1

        return ''.join(decrypted_text)

    def _build_pattern(self, text_length: int, key: int) -> list[int]:
        pattern = []
        rail = 0
        direction = 1

        for _ in range(text_length):
            pattern.append(rail)
            rail += direction

            if rail == 0 or rail == key - 1:
                direction *= -1

        return pattern
