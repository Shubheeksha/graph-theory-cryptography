# Graph Theory Cryptography - Paper Reproduction

A Python implementation of the cryptographic algorithm described in the paper:
**"Applying Graph Theory to Secure Data Encryption"**

## Overview
This project reproduces and enhances the graph-theory-based encryption algorithm that combines:
- **Caesar Cipher** - Shift-based character encryption (key1)
- **Graph Key Generation** - Derives permutation key from adjacency matrix (key2)
- **Column Permutation** - Uses graph structure to permute plaintext columns
- **Double Matrix Transformation** - Two-stage encryption for enhanced security

## Key Features
✅ **Flexible Plaintext Length** - Handles any length plaintext including prime numbers through intelligent padding

✅ **Adaptive Graph Support** - Works with any graph structure (4-vertex, 7-vertex, etc.) via adjacency matrix

✅ **Robust Padding Strategy** - Automatic padding ensures uniform matrix dimensions during transformations

✅ Detailed step-by-step encryption/decryption visualization

✅ Matrix transformations displayed at each cryptographic stage

✅ Configurable padding character and Caesar shift value

✅ Comprehensive test coverage for edge cases

## Enhancement Over Original Paper
The original algorithm had limitations with:
- Plaintext lengths not divisible by the number of graph vertices (especially problematic for prime-length inputs)
- Inconsistent matrix dimensions during column arrangement operations

**Our Solution:** Implements ceiling-based row calculation and adaptive padding that:
1. Ensures uniform column heights regardless of plaintext length
2. Correctly handles any graph structure without modification
3. Preserves original plaintext length for accurate decryption

## Installation
```bash
git clone https://github.com/yourusername/graph-theory-cryptography.git
cd graph-theory-cryptography
pip install -r requirements.txt
