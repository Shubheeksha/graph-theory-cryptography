import math
import numpy as np

class GraphCryptography:
    def __init__(self, adjacency_matrix, key1, padding_char='X'):
        self.adj_matrix = np.array(adjacency_matrix)
        self.key1 = key1
        self.key2 = self._generate_key2_from_graph()
        self.padding_char = padding_char

    def _generate_key2_from_graph(self):
        key2 = []
        for col_idx in range(self.adj_matrix.shape[1]):
            key2.append(int(np.sum(self.adj_matrix[:, col_idx])))
        return key2

    def _caesar_encrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + self.key1) % 26 + base)
            else:
                result += char
        return result

    def _caesar_decrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base - self.key1) % 26 + base)
            else:
                result += char
        return result

    def _create_matrix(self, text, cols):
        text = text.replace(' ', '')
        rows = (len(text) + cols - 1) // cols
        padded_text = text.ljust(rows * cols, self.padding_char)
        matrix = []
        for i in range(rows):
            matrix.append(list(padded_text[i*cols:(i+1)*cols]))
        return matrix

    def _read_by_column_order(self, matrix, key_order):
        result = ""
        sorted_indices = sorted(range(len(key_order)), key=lambda k: key_order[k])
        for col_idx in sorted_indices:
            for row in matrix:
                if col_idx < len(row):
                    result += row[col_idx]
        return result

    def _read_by_row(self, matrix):
        return ''.join(''.join(row) for row in matrix)

    def _print_matrix(self, matrix, key_header=None):
        """Print matrix in a formatted way."""
        if key_header:
            print("   " + "  ".join(map(str, key_header)))
        for row in matrix:
            print("   " + "  ".join(row))

    def _arrange_by_columns(self, text, key_order):
        """
        Robust arrange: compute rows with ceiling and fill missing cells
        with padding so columns always have uniform height.
        This fixes issues when len(text) is not divisible by cols (e.g., primes).
        """
        cols = len(key_order)
        rows = (len(text) + cols - 1) // cols  # ceiling

        # Initialize matrix filled with padding_char
        matrix = [[self.padding_char for _ in range(cols)] for _ in range(rows)]

        # Determine the order of columns according to key_order
        sorted_indices = sorted(range(len(key_order)), key=lambda k: key_order[k])

        text_idx = 0
        for col_idx in sorted_indices:
            for row_idx in range(rows):
                if text_idx < len(text):
                    matrix[row_idx][col_idx] = text[text_idx]
                    text_idx += 1
                else:
                    # leave padding
                    matrix[row_idx][col_idx] = self.padding_char
        return matrix

    def encrypt(self, plaintext):
        plaintext = plaintext.replace(' ', '').upper()
        original_length = len(plaintext)
        
        print(f"Step 0 - Original plaintext: {plaintext}")
        print(f"Original length: {original_length}\n")

        caesar = self._caesar_encrypt(plaintext)
        print(f"Step 1 - After Caesar cipher (+{self.key1}): {caesar}\n")

        cols = len(self.key2)
        matrix1 = self._create_matrix(caesar, cols)
        print(f"Step 2 - Matrix 1 (Caesar text arranged with {cols} columns):")
        print(f"Key2 order: {self.key2}")
        self._print_matrix(matrix1, self.key2)
        
        step1 = self._read_by_column_order(matrix1, self.key2)
        print(f"\nStep 3 - After reading columns by key2 order: {step1}\n")

        matrix2 = self._create_matrix(step1, cols)
        print(f"Step 4 - Matrix 2 (permuted text arranged with {cols} columns):")
        self._print_matrix(matrix2, self.key2)
        
        ciphertext = self._read_by_column_order(matrix2, self.key2)
        print(f"\nStep 5 - Final ciphertext: {ciphertext}\n")

        return ciphertext, original_length

    def decrypt(self, ciphertext, original_length):
        cols = len(self.key2)
        
        print(f"\n{'='*60}")
        print("DECRYPTION PROCESS")
        print(f"{'='*60}")
        print(f"\nStep 0 - Ciphertext to decrypt: {ciphertext}\n")

        matrix1 = self._arrange_by_columns(ciphertext, self.key2)
        print(f"Step 1 - Matrix 1 (ciphertext arranged by columns):")
        print(f"Key2 order: {self.key2}")
        self._print_matrix(matrix1, self.key2)
        
        step1 = self._read_by_row(matrix1)
        print(f"\nStep 2 - After reading row by row: {step1}\n")

        matrix2 = self._arrange_by_columns(step1, self.key2)
        print(f"Step 3 - Matrix 2 (permuted text arranged by columns):")
        self._print_matrix(matrix2, self.key2)
        
        caesar_text = self._read_by_row(matrix2)
        print(f"\nStep 4 - Before Caesar decryption: {caesar_text}\n")

        plaintext = self._caesar_decrypt(caesar_text)
        plaintext = plaintext[:original_length]
        print(f"Step 5 - After Caesar decryption (-{self.key1}): {plaintext}\n")
        
        return plaintext


if __name__ == '__main__':
    adjacency_matrix = [
        [1,1,1,1],
        [1,0,0,1],
        [1,0,0,0],
        [1,1,0,1]
    ]
    key1 = 4
    crypto = GraphCryptography(adjacency_matrix, key1)

    # prime-length plaintext (13)
    plaintext = 'THISISANEXAMO'  # length 13
    print('Plaintext :', plaintext)

    ciphertext, orig_len = crypto.encrypt(plaintext)
    print('Ciphertext:', ciphertext)

    decrypted = crypto.decrypt(ciphertext, orig_len)
    print('Decrypted :', decrypted)
    print('Match     :', decrypted == plaintext.upper())
