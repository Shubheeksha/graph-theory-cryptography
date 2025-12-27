# Graph Theory Cryptography - Paper Reproduction

A Python implementation of the cryptographic algorithm described in the paper:
**"Applying Graph Theory to Secure Data by Cryptography"**

## Overview
This project reproduces and enhances the graph-theory-based encryption algorithm that combines:
- **Caesar Cipher** - Shift-based character encryption (key1)
- **Graph Key Generation** - Derives permutation key from adjacency matrix (key2)
- **Column Permutation** - Uses graph structure to permute plaintext columns
- **Double Matrix Transformation** - Two-stage encryption for enhanced security

## Key Features
✓ Handles prime-length plaintexts correctly
✓ Detailed step-by-step encryption/decryption visualization
✓ Matrix transformations at each stage
✓ Configurable padding and Caesar shift
✓ Comprehensive test coverage

## Installation
```bash
git clone https://github.com/yourusername/graph-theory-cryptography.git
cd graph-theory-cryptography
pip install -r requirements.txt
