# Knuth-Morris-Pratt (KMP) Algorithm
## Linear-Time Substring Search Without Backtracking
**Presented by:** Rob Gravelle

---

## Agenda

1. **The Core Problem**: Why Naive Search Fails
2. **Historical Background**: Origins & Milestones
3. **The Core Intuition**: Avoiding Redundant Checks
4. **The Secret Weapon**: Longest Prefix Suffix (LPS) Table
5. **Algorithm Walkthrough**: Step-by-Step Execution
6. **Complexity & Benchmarks**: O(N+M) vs O(N * M)
7. **Real-World Applications**: Where KMP Shines
8. **Summary & Takeaways**

---

## 1. The Core Problem

### The Naive Substring Search Bottleneck

When searching for a pattern in text:
* Compare character by character.
* On mismatch: **Shift pattern by 1** and start over from scratch.

Text:    A B A B C A B A B C
Pattern: A B A B X
          x (Mismatch at index 4)
Shift:     A B A B X  <-- Backtracks text pointer!

* **Worst-Case Complexity**: O(N * M)
* **Issue**: Discards valuable information about characters already matched.

---


## 2. Historical Background

### The Pioneers Behind the Algorithm

<div align="center">
  <img src="./Images/KMP.png" width="600" alt="KMP Algorithm Inventors: Knuth, Pratt, Morris">
</div>

### A Breakthrough in String Processing (1970–1977)

* **Co-Inventors**: 
  * Donald Knuth & Vaughan Pratt (Stanford, 1970)
  * James H. Morris (UC Berkeley, 1970)
* **Published**: Joint paper in 1977 (*Fast Pattern Matching in Strings*, SIAM Journal on Computing).
* **Historical Significance**:
  * First deterministic linear-time algorithm for string matching.
  * Solved severe performance penalties on repetitive text (e.g., DNA strings, binary signals).

> "KMP proved that we never need to move backward in the target text."
## 3. The Core Intuition

### The "Smart Reader" Paradigm

Imagine searching for **ONION** in a document:

1. You match **O - N - I - O**, then encounter a mismatch on the 5th character.
2. Naive approach: Backtrack to character #2 and start reading again.
3. **KMP approach**:
   * You already know you read **O - N - I - O**.
   * Notice that **O - N** at the end matches **O - N** at the start.
   * Keep your finger on the main text, align the prefix O - N, and keep moving forward!

---

## 4. The Secret Weapon: LPS Table

### Longest Proper Prefix which is also a Suffix

The **LPS array** stores precomputed shift distances for every prefix of the pattern.

For Pattern `ABABC`:

| Index | Substring | Proper Prefixes | Suffixes | LPS Value |
| :---: | :---: | :---: | :---: | :---: |
| **0** | `A` | None | None | **0** |
| **1** | `AB` | `A` | `B` | **0** |
| **2** | `ABA` | `A`, `AB` | `A`, `BA` | **1** (`A`) |
| **3** | `ABAB` | `A`, `AB`, `ABA` | `B`, `AB`, `BAB` | **2** (`AB`) |
| **4** | `ABABC` | ... | ... | **0** |

---

## 5. Algorithm Walkthrough

### Matching Phase Mechanics

Text:    A B A B D A B A C D A B A B C A B A B
Pattern: A B A B C
Match:   A B A B x  (Mismatch: 'D' vs 'C' at Pattern index 4)

1. Look up LPS[4 - 1] -> LPS[3] = **2** (`AB`).
2. Do **NOT** move the text pointer backward.
3. Jump pattern index from 4 to 2.

Text:    A B A B D A B A C D A B A B C A B A B
Pattern:     A B A B C
             x  (Immediate mismatch 'D' vs 'A'; advance text pointer)

---

## 6. Complexity Analysis

| Metric | Naive Algorithm | KMP Algorithm |
| :--- | :---: | :---: |
| **Preprocessing Time** | O(1) | O(M) |
| **Matching Time** | O(N * M) | O(N) |
| **Total Worst-Case Time** | O(N * M) | **O(N + M)** |
| **Auxiliary Space** | O(1) | O(M) |

### Why O(N) Matching Time?
* The text index i **never decrements**.
* The pattern index j drops at most N times overall.
* Amortized work per character is constant O(1).

---

## 7. Real-World Applications

* **Streaming Data Processing**: Ideal for non-seekable inputs (network sockets, live telemetry) where backtracking is impossible.
* **Bioinformatics**: Fast matching on small, highly repetitive alphabets (DNA sequences: {A, C, G, T}).
* **Log Analysis**: Efficient single-pass scanning of massive server log files.
* **Intrusion Detection Systems (IDS)**: Matching packet signatures in live network traffic.

---

## 8. Summary & Takeaways

1. **Zero Text Backtracking**: Processes input text strictly left-to-right.
2. **Preprocessing Power**: Invests O(M) upfront to guarantee O(N) runtime later.
3. **Deterministic**: No probabilistic risks or hash collisions (unlike Rabin-Karp).
4. **Portfolio Ready**: Clean Python implementation available in `KMP.py`.

#  Questions & Discussion

**Created by:** Rob Gravelle
**GitHub:** github.com/Rob-Gravelle
---
