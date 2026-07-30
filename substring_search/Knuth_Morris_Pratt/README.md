# Substring Search Algorithms
**Author:** Rob Gravelle  
**Portfolio Module:** `Algorithms/substring_search`

---

Welcome to the Substring Search module. This repository contains well-documented reference implementations of classic pattern-matching algorithms, backed by unit test suites, executive overviews, and deep-dive technical specifications.

---

## Algorithm Performance Comparison

Substring search algorithms find occurrences of a pattern string $P$ (length $m$) within a body of target text $T$ (length $n$).

| Algorithm | Preprocessing Time | Search Time (Worst) | Search Time (Average) | Auxiliary Space | Key Advantage |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Knuth–Morris–Pratt (KMP)** | $O(m)$ | $O(n)$ | $O(n)$ | $O(m)$ | Zero text backtracking; ideal for unseekable streaming data. |
| **Boyer–Moore** | $O(m + \vert{}\Sigma\vert{})$ | $O(n \times m)$ | $O(n / m)$ | $O(m + \vert{}\Sigma\vert{})$ | Sub-linear average speed; skips large text blocks right-to-left. |
| **Rabin–Karp** | $O(m)$ | $O(n \times m)$ | $O(n + m)$ | $O(1)$ | Rolling hash mechanism; highly efficient for multi-pattern matching. |

---

## Directory Navigation

Every algorithm in this module is structured as a self-contained package:

```text
substring_search/
├── README.md                     # Module overview & comparison table
├── Knuth_Morris_Pratt/           # KMP Search Module
│   ├── KMP.py                    # Algorithm implementation & demo
│   ├── test_kmp.py               # Automated pytest suite (10 tests)
│   ├── README.md                 # Navigation hub & quickstart
│   ├── RECRUITER_SUMMARY.md      # Non-technical / Executive summary
│   ├── TECHNICAL_SPEC.md         # Engineering spec & DFA analysis
│   ├── KMP_PRESENTATION.md       # Slide deck (Marp / GitHub compatible)
│   └── Images/                   # Visual failure link diagrams
├── Boyer_Moore/                  # (In Development)
└── Rabin_Karp/                   # (In Development)