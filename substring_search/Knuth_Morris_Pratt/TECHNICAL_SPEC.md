# Technical Specification: Knuth-Morris-Pratt (KMP) Search
**Author:** Rob Gravelle | **Complexity:** Time O(n + m) | Space O(m)
**Target Text Length:** n | **Pattern Length:** m

---

### 1. Historical & Theoretical Context
Developed independently by Donald Knuth and Vaughan Pratt (1970) and James H. Morris (1970), and published jointly in 1977, KMP was designed to address the catastrophic O(n * m) worst-case theoretical complexity of standard brute-force search. Prior to KMP, string matching on repetitive alphabets (such as binary text or genomic sequences) caused heavy pointer backtracking. KMP introduced the concept of deterministic finite state automata (DFA) constructed from pattern self-similarity, laying the groundwork for modern linear-time sequence alignment in computer science.

---

### 2. Theoretical Foundation & Mechanics
The naive string-matching paradigm suffers from an O(n * m) worst-case time complexity due to redundant re-evaluations of text characters upon encountering a mismatch. KMP eliminates text backtracking by leveraging the structural properties of the pattern string.

#### The Longest Prefix Suffix (LPS) Array
The backbone of KMP is the auxiliary **LPS Table** (also known as the Partial Match Table or pi function).

For a pattern P of length m, LPS[i] stores the length of the longest proper prefix of P[0..i] that is also a suffix of P[0..i].
* **Proper Prefix:** A prefix that is not equal to the full string itself.
* **Suffix:** A trailing substring ending at position i.

---

---

### 3. Failure Transitions & Execution Walkthrough

The core innovation of KMP is its preprocessing phase, which constructs the Longest Prefix Suffix (LPS) table. This table acts as a deterministic finite automaton (DFA) that directs state fallbacks without rewinding the text pointer $i$.

<div align="center">
  <img src="./Images/kmp_failure_links.png" width="700" alt="KMP State Machine and Failure Links">
  <p><em>Figure 1: State transition graph illustrating match advances and failure fallback links for pattern ABABAC.</em></p>
</div>

#### Preprocessing Phase ($O(m)$ Time, $O(m)$ Auxiliary Space)
We construct LPS iteratively using a two-pointer invariant:
1. `length` tracks the current matching prefix length.
2. `i` iterates through the pattern string from index 1 to $m-1$.

* If $P[i] == P[length]$: Increment `length`, store $LPS[i] = length$, and advance `i`.  
* If $P[i] \neq P[length]$ and $length > 0$: Fallback $length = LPS[length - 1]$ **without** advancing `i` (amortized $O(m)$ overall).

#### Matching Phase ($O(n)$ Time)
Using pointer $i$ for text $T$ and pointer $j$ for pattern $P$:
* **On Match ($T[i] == P[j]$):** Increment both $i$ and $j$.
* **On Full Match ($j == m$):** Record match index at $i - j$. Set $j = LPS[j - 1]$ to detect overlapping occurrences.
* **On Mismatch ($T[i] \neq P[j]$):**
  * If $j \neq 0$: Update $j = LPS[j - 1]$ (text pointer $i$ stays invariant).
  * If $j == 0$: Increment $i$.

---

### 4. Asymptotic Analysis & Edge Cases

| Metric | Complexity | Notes |
| :--- | :--- | :--- |
| **Preprocessing Time** | O(m) | Single pass over pattern P |
| **Search Time** | O(n) | Text pointer i strictly increments up to n times |
| **Total Worst-Case Time** | O(n + m) | Deterministic upper bound |
| **Space Complexity** | O(m) | Required for the LPS storage array |

#### Key Advantages & Trade-offs
* **Zero Text Backtracking:** Ideal for unseekable data streams, large network packets, and disk/memory buffers.
* **Worst-Case Determinism:** Unlike Boyer-Moore (which relies on large alphabets for optimal performance) or Rabin-Karp (susceptible to hash collision degradation), KMP guarantees linear time across all alphabet sizes—including binary text (0s and 1s).