# Knuth-Morris-Pratt (KMP) Algorithm
## Linear-Time Substring Search Without Backtracking
**Presented by:** Rob Gravelle

# Substring Search Algorithms

Welcome to the Substring Search section of my Algorithms Portfolio. This repository contains clean, modular Python implementations of classic pattern-matching algorithms, accompanied by multi-tiered documentation designed for different audiences.

---

## Repository Structure & Documentation Strategy

Every algorithm directory in this repository follows a standardized four-file structure:

substring_search/
├── Knuth_Morris_Pratt/
│   ├── KMP.py                   # Production-ready Python implementation
│   ├── RECRUITER_SUMMARY.txt    # Non-technical / Business overview
│   ├── TECHNICAL_SPEC.txt       # Engineering / CS deep-dive
│   └── KMP_PRESENTATION.txt     # Pitch deck / Slide presentation
├── Boyer_Moore/
│   └── ...
└── Rabin_Karp/
    └── ...

### Why Dual-Audience Documentation?

To effectively bridge the gap between technical execution and business communication, each algorithm includes two distinct markdown/text specifications:

* RECRUITER_SUMMARY (Executive / Non-Technical)
  - Target Audience: Hiring managers, recruiters, project managers, and non-technical stakeholders.
  - Focus: High-level executive summaries, real-world analogies, business value, predictability, and practical applications without unnecessary mathematical overhead.

* TECHNICAL_SPEC (Engineering / CS Deep-Dive)
  - Target Audience: Software engineers, technical interviewers, and computer scientists.
  - Focus: Rigorous asymptotic analysis (O(N) time/space bounds), theoretical foundation, state machine mechanics, edge cases, and algorithmic trade-offs.

* [ALGORITHM]_PRESENTATION (Slide Deck Format)
  - Target Audience: Technical leads, team presentations, or visual learners.
  - Focus: A slide-by-slide presentation (compatible with Marp and GitHub rendering) summarizing the core problem, walkthroughs, visual tables, and applications.

---

## Substring Search Overview & Comparison

Substring search algorithms aim to find occurrences of a pattern string P (length m) within a body of text T (length n).

| Algorithm | Preprocessing Time | Search Time (Worst) | Search Time (Average) | Key Advantage |
| :--- | :---: | :---: | :---: | :--- |
| Knuth-Morris-Pratt (KMP) | O(m) | O(n) | O(n) | Zero text backtracking; ideal for unseekable streaming data. |
| Boyer-Moore | O(m + |Sigma|) | O(n * m) | O(n / m) | Sub-linear average speed; skips large sections of text right-to-left. |
| Rabin-Karp | O(m) | O(n * m) | O(n + m) | Rolling hash mechanism; highly efficient for multi-pattern matching. |

---

## Getting Started

To run any implementation, navigate to the algorithm directory and run the script with Python 3:

cd Knuth_Morris_Pratt
python KMP.py

#  Questions & Discussion

**Created by:** Rob Gravelle
**GitHub:** github.com/Rob-Gravelle