# Paper Reference

## Original Paper
**Title:** Applying Graph Theory to Secure Data by Cryptography  

### Authors
**Dr. Gurusharan Kaur**, **Dr. Namrata Tripathi**

### Journal & Publication Details
- **Journal:** *International Journal of Linguistics and Computational Applications (IJLCA)*
- **Volume:** 8  
- **Issue:** 1  
- **Publication Period:** January – March 2021  
- **ISSN (Print):** 2394-6385  
- **ISSN (Online):** 2394-6393  
- **DOI:** 10.30726/ijlca/v8.i1.2020.81001  

---
### Key Concepts from Paper
1. **Adjacency Matrix as Key:** Using graph structure to generate cryptographic keys
2. **Column Permutation:** Reordering message columns based on graph properties
3. **Double Encryption:** Two-stage transformation for enhanced security
4. **Vertex Degree as Key:** Key2 derived from vertex degrees in the graph

### How This Implementation Enhances the Paper

The original paper presented the algorithm but had practical limitations:
- **Problem 1:** Algorithm assumed plaintext length would be divisible by number of vertices
- **Problem 2:** Prime-length plaintexts couldn't be processed correctly
- **Problem 3:** Inconsistent matrix dimensions during encryption/decryption

**Our Enhancement:**
- Implements intelligent **adaptive padding** using ceiling-based row calculation
- Handles **any plaintext length** (especially prime numbers)
- Works with **any graph structure** without limitations
- Maintains **symmetric encryption/decryption** for reliable round-trip conversion

### Mathematical Foundation

#### Key Generation from Graph
For adjacency matrix A of an n-vertex graph:
```
Key2[i] = Σ(A[j][i]) for j=0 to n-1
```
This represents the degree of each vertex.

#### Matrix Transformation
1. **Ceiling division for padding:**
   ```
   rows = ⌈plaintext_length / num_vertices⌉
   ```

2. **Column ordering by key2:**
   ```
   sorted_indices = sort(range(num_vertices) by Key2 values)
   ```

3. **Encryption steps:**
   - Caesar cipher with Key1
   - Matrix 1: arrange by rows, read by sorted columns
   - Matrix 2: arrange by rows, read by sorted columns again
   - Result: ciphertext

## References & Citations

- **Kaur, G., & Tripathi, N.** (2021). *Applying Graph Theory to Secure Data by      Cryptography*.  
  International Journal of Linguistics and Computational Applications (IJLCA), 8(1).

---

## Implementation Notes

This repository contains a faithful reproduction of the paper's algorithm with the critical enhancement of handling arbitrary plaintext lengths through adaptive padding. The implementation serves both:
- **Educational Purpose:** Understanding how graph theory can be applied to cryptography
- **Practical Purpose:** A working cryptographic tool for educational demonstrations


