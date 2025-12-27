"""
Demo script showing how to use the GraphCryptography class
Demonstrates encryption and decryption with different plaintext lengths
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.graph_cryptography import GraphCryptography


def demo_basic_usage():
    """Demonstrate basic encryption and decryption"""
    print("\n" + "="*70)
    print("GRAPH THEORY CRYPTOGRAPHY - BASIC DEMO")
    print("="*70)
    
    # Define adjacency matrix
    adjacency_matrix = [
        [1, 1, 1, 1],  # V1: connected to V1, V2, V3, V4
        [1, 0, 0, 1],  # V2: connected to V1, V4
        [1, 0, 0, 0],  # V3: connected to V1
        [1, 1, 0, 1]   # V4: connected to V1, V2, V4
    ]
    
    key1 = 4
    
    # Initialize cryptography system
    crypto = GraphCryptography(adjacency_matrix, key1)
    
    print(f"\nAdjacency Matrix:")
    print(f"{adjacency_matrix}")
    print(f"\nGenerated Key2 (from graph): {crypto.key2}")
    print(f"Key1 (Caesar shift): +{key1}")
    
    # Test with prime-length plaintext
    plaintext = "THISISANEXAMO"  # 13 characters (prime)
    print(f"\n{'='*70}")
    print(f"TEST: Prime-length plaintext ({len(plaintext)} characters)")
    print(f"{'='*70}")
    print(f"\nOriginal plaintext: {plaintext}\n")
    
    # Encrypt
    print("ENCRYPTION PROCESS:")
    print("-"*70)
    ciphertext, length = crypto.encrypt(plaintext)
    
    # Decrypt
    print("\nDECRYPTION PROCESS:")
    print("-"*70)
    decrypted = crypto.decrypt(ciphertext, length)
    
    # Verification
    print("\n" + "="*70)
    print("VERIFICATION RESULTS")
    print("="*70)
    print(f"Original:  {plaintext}")
    print(f"Encrypted: {ciphertext}")
    print(f"Decrypted: {decrypted}")
    print(f"Match: {'✓ YES' if decrypted == plaintext else '✗ NO'}")
    print("="*70 + "\n")


def demo_various_lengths():
    """Demonstrate with various plaintext lengths"""
    print("\n" + "="*70)
    print("TESTING VARIOUS PLAINTEXT LENGTHS")
    print("="*70)
    
    adjacency_matrix = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 0],
        [1, 1, 0, 1]
    ]
    
    crypto = GraphCryptography(adjacency_matrix, key1=3)
    
    test_cases = [
        ("HELLO", 5, "prime"),
        ("ENCRYPT", 7, "prime"),
        ("GRAPHTHEORY", 11, "prime"),
        ("THISISANEXAMO", 13, "prime"),
        ("HELLOWORLD12", 12, "composite"),
        ("CRYPTOGRAPHY", 12, "composite"),
    ]
    
    for plaintext, length, desc in test_cases:
        print(f"\nPlaintext: '{plaintext}' ({length} chars - {desc})")
        ciphertext, _ = crypto.encrypt(plaintext)
        decrypted = crypto.decrypt(ciphertext, length)
        match = "✓" if decrypted == plaintext else "✗"
        print(f"Status: {match} {'PASS' if decrypted == plaintext else 'FAIL'}")
        print(f"  Encrypted: {ciphertext}")
        print(f"  Decrypted: {decrypted}")


def demo_different_graph():
    """Demonstrate with a different graph structure"""
    print("\n" + "="*70)
    print("TESTING WITH DIFFERENT GRAPH STRUCTURE")
    print("="*70)
    
    # 7-vertex graph
    adjacency_matrix = [
        [1, 1, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1],
        [0, 1, 1, 1, 1, 1, 0]
    ]
    
    crypto = GraphCryptography(adjacency_matrix, key1=5)
    
    print(f"\n7-Vertex Graph - Key2: {crypto.key2}")
    
    plaintext = "GRAPHCRYPTO"  # 11 characters (prime)
    print(f"\nPlaintext: {plaintext} ({len(plaintext)} chars - prime)")
    
    ciphertext, length = crypto.encrypt(plaintext)
    decrypted = crypto.decrypt(ciphertext, length)
    
    print(f"\nMatch: {'✓ YES' if decrypted == plaintext else '✗ NO'}")
    print(f"  Encrypted: {ciphertext}")
    print(f"  Decrypted: {decrypted}")


if __name__ == '__main__':
    demo_basic_usage()
    demo_various_lengths()
    demo_different_graph()
    
    print("\n" + "="*70)
    print("All demos completed successfully!")
    print("="*70 + "\n")
