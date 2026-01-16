import math
import numpy as np

class GraphCryptography:
    def __init__(self, adjacency_matrix, key1, padding_char='X', space_char='_'):
        self.adj_matrix = np.array(adjacency_matrix)
        self.key1 = key1
        self.key2 = self._generate_key2_from_graph()
        self.padding_char = padding_char
        self.space_char = space_char  # Character to represent spaces
        self.adjacency_matrix = adjacency_matrix  # Store for printing

    def _generate_key2_from_graph(self):
        key2 = []
        for col_idx in range(self.adj_matrix.shape[1]):
            key2.append(int(np.sum(self.adj_matrix[:, col_idx])))
        return key2

    def _shift_ascii_values(self, text):
        """Shift ASCII values of all characters by key1 amount."""
        result = ""
        for char in text:
            ascii_val = ord(char)
            # Shift ASCII value and keep it in printable range (32-126)
            shifted = ((ascii_val - 32 + self.key1) % 95) + 32
            result += chr(shifted)
        return result

    def _unshift_ascii_values(self, text):
        """Reverse the ASCII value shift."""
        result = ""
        for char in text:
            ascii_val = ord(char)
            # Reverse shift ASCII value
            unshifted = ((ascii_val - 32 - self.key1) % 95) + 32
            result += chr(unshifted)
        return result

    def _create_matrix(self, text, cols):
        # Create matrix with the encrypted/shifted text
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
        """Unified encryption for both simple and alphanumeric text."""
        original_length = len(plaintext)
        
        print(f"Step 0 - Original plaintext: {plaintext}")
        print(f"Original length: {original_length}")
        print(f"\nAdjacency Matrix:")
        print(np.array(self.adjacency_matrix))
        print(f"Generated Key2 from graph: {self.key2}\n")

        # Convert to uppercase for consistency
        plaintext = plaintext.upper()
        
        # Step 1: Shift ASCII values of all characters
        ascii_shifted = self._shift_ascii_values(plaintext)
        print(f"Step 1 - After ASCII shift (+{self.key1}): {ascii_shifted}\n")

        # Step 2: Create matrix and apply first permutation
        cols = len(self.key2)
        matrix1 = self._create_matrix(ascii_shifted, cols)
        print(f"Step 2 - Matrix 1 (shifted text arranged with {cols} columns):")
        print(f"Key2 order: {self.key2}")
        self._print_matrix(matrix1, self.key2)
        
        step1 = self._read_by_column_order(matrix1, self.key2)
        print(f"\nStep 3 - After reading columns by key2 order: {step1}\n")

        # Step 3: Create second matrix and apply final permutation
        matrix2 = self._create_matrix(step1, cols)
        print(f"Step 4 - Matrix 2 (permuted text arranged with {cols} columns):")
        self._print_matrix(matrix2, self.key2)
        
        ciphertext = self._read_by_column_order(matrix2, self.key2)
        print(f"\nStep 5 - Final ciphertext: {ciphertext}\n")

        return ciphertext, original_length

    def decrypt(self, ciphertext, original_length):
        """Unified decryption for both simple and alphanumeric text."""
        cols = len(self.key2)
        
        print(f"\n{'='*60}")
        print("DECRYPTION PROCESS")
        print(f"{'='*60}")
        print(f"\nStep 0 - Ciphertext to decrypt: {ciphertext}\n")

        # Step 1: Arrange ciphertext by columns
        matrix1 = self._arrange_by_columns(ciphertext, self.key2)
        print(f"Step 1 - Matrix 1 (ciphertext arranged by columns):")
        print(f"Key2 order: {self.key2}")
        self._print_matrix(matrix1, self.key2)
        
        step1 = self._read_by_row(matrix1)
        print(f"\nStep 2 - After reading row by row: {step1}\n")

        # Step 2: Arrange by columns again
        matrix2 = self._arrange_by_columns(step1, self.key2)
        print(f"Step 3 - Matrix 2 (permuted text arranged by columns):")
        self._print_matrix(matrix2, self.key2)
        
        ascii_shifted = self._read_by_row(matrix2)
        print(f"\nStep 4 - Before ASCII unshift: {ascii_shifted}\n")

        # Step 3: Unshift ASCII values
        plaintext = self._unshift_ascii_values(ascii_shifted)
        plaintext = plaintext[:original_length]
        print(f"Step 5 - After ASCII unshift (-{self.key1}): {plaintext}\n")
        
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

    # Test 1: Simple text
    print(f"\n{'='*60}")
    print("TEST 1: Simple Text Encryption")
    print("="*60)
    
    plaintext1 = "THIS IS AN EN"
    print(f"\n{'='*60}")
    print("ENCRYPTION")
    print("="*60)
   
    ciphertext1, orig_len1 = crypto.encrypt(plaintext1)
    print('Ciphertext:', ciphertext1)

    decrypted1 = crypto.decrypt(ciphertext1, orig_len1)

    print(f"\n{'='*60}")
    print("VERIFICATION")
    print("="*60)
    print(f"Original:  {plaintext1}")
    print(f"Decrypted: {decrypted1}")
    print(f"Match: {plaintext1.upper() == decrypted1}")

    # Test 2: Alphanumeric text
    print(f"\n\n{'='*60}")
    print("TEST 2: Alphanumeric Text Encryption")
    print("="*60)
    
    plaintext2 = "Hello123"
    print(f"\n{'='*60}")
    print("ENCRYPTION")
    print("="*60)
    
    ciphertext2, orig_len2 = crypto.encrypt(plaintext2)
    print('Ciphertext:', ciphertext2)
    
    decrypted2 = crypto.decrypt(ciphertext2, orig_len2)
    
    print(f"\n{'='*60}")
    print("VERIFICATION")
    print("="*60)
    print(f"Original:  {plaintext2}")
    print(f"Decrypted: {decrypted2}")
    print(f"Match: {plaintext2.upper() == decrypted2}")

    # Test 3: Special characters
    print(f"\n\n{'='*60}")
    print("TEST 3: Special Characters")
    print("="*60)
    
    plaintext3 = "Test@2025!"
    print(f"\n{'='*60}")
    print("ENCRYPTION")
    print("="*60)
    
    ciphertext3, orig_len3 = crypto.encrypt(plaintext3)
    print('Ciphertext:', ciphertext3)
    
    decrypted3 = crypto.decrypt(ciphertext3, orig_len3)
    
    print(f"\n{'='*60}")
    print("VERIFICATION")
    print("="*60)
    print(f"Original:  {plaintext3}")
    print(f"Decrypted: {decrypted3}")
    print(f"Match: {plaintext3.upper() == decrypted3}")

