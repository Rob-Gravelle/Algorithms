================================================================================
                    KNUTH-MORRIS-PRATT (KMP) ALGORITHM
           Linear-Time Substring Search Without Backtracking
                        Presented by: Rob Gravelle
================================================================================

--------------------------------------------------------------------------------
AGENDA
--------------------------------------------------------------------------------
1. The Core Problem: Why Naive Search Fails
2. Historical Background: Origins & Milestones
3. The Core Intuition: Avoiding Redundant Checks
4. The Secret Weapon: Longest Prefix Suffix (LPS) Table
5. State Machine Mechanics & Failure Links Diagram
6. Algorithm Walkthrough: Step-by-Step Execution
7. Complexity Analysis: O(N+M) vs O(N * M)
8. Real-World Applications: Where KMP Shines
9. Summary & Takeaways

--------------------------------------------------------------------------------
SLIDE 1: THE CORE PROBLEM
--------------------------------------------------------------------------------
The Naive Substring Search Bottleneck:

When searching for a pattern in text using standard methods:
  • Compare character by character.
  • On mismatch: Shift pattern forward by 1 position and start over.

Example:
  Text:    A B A B C A B A B C
  Pattern: A B A B X
            x (Mismatch at index 4)
  Shift:     A B A B X  <-- Backtracks the text pointer!

  • Worst-Case Time Complexity: O(N * M)
  • Primary Flaw: Discards valuable structural information about characters 
    that were already successfully matched.

--------------------------------------------------------------------------------
SLIDE 2: HISTORICAL ORIGINS & PIONEERS
--------------------------------------------------------------------------------
+-----------------------+ +-----------------------+ +-----------------------+
|     Donald Knuth      | |     Vaughan Pratt     | |    James H. Morris    |
|  Stanford University  | |  Stanford University  | | Cal Berkeley / CMU    |
+-----------------------+ +-----------------------+ +-----------------------+

A Breakthrough in String Processing (1970–1977):

  • 1970: Knuth & Pratt and Morris independently discover zero-backtrack search.
  • 1970: Morris independently invents the technique while developing a text
          editor buffer at UC Berkeley.
  • 1977: The three researchers unite to publish the definitive joint paper:
          "Fast Pattern Matching in Strings" (SIAM Journal on Computing).

Historical Significance:
  • First deterministic linear-time algorithm for string matching.
  • Solved severe performance penalties on repetitive text (e.g., DNA strings,
    binary signals).

> "KMP proved that we never need to move backward in the target text."

--------------------------------------------------------------------------------
SLIDE 3: THE CORE INTUITION
--------------------------------------------------------------------------------
The "Smart Reader" Paradigm:

Imagine searching for the pattern ABABAC inside a long document:

  1. You match A - B - A - B - A, but then hit a mismatch on the 6th character (C).
  2. Naive approach: Backtrack to the 2nd character in the text and start re-reading.
  3. KMP approach:
     • You already know you read A - B - A - B - A.
     • Notice that A - B - A appears at both the START (prefix) and END (suffix)
       of the matched text.
     • Keep your finger on the main text, align the prefix ABA, and keep moving 
       forward without re-reading a single character!

--------------------------------------------------------------------------------
SLIDE 4: THE SECRET WEAPON (LPS TABLE)
--------------------------------------------------------------------------------
Longest Proper Prefix which is also a Suffix:

The LPS array precomputes shift distances for every prefix of the pattern.

For Pattern "ABABC":

+-------+-----------+--------------------+---------------------+-----------+
| Index | Substring | Proper Prefixes    | Suffixes            | LPS Value |
+-------+-----------+--------------------+---------------------+-----------+
|   0   | A         | None               | None                |     0     |
|   1   | AB        | A                  | B                   |     0     |
|   2   | ABA       | A, AB              | A, BA               |   1 (A)   |
|   3   | ABAB      | A, AB, ABA         | B, AB, BAB          |   2 (AB)  |
|   4   | ABABC     | A, AB, ABA, ABAB   | C, BC, ABC, BABC    |     0     |
+-------+-----------+--------------------+---------------------+-----------+

--------------------------------------------------------------------------------
SLIDE 5: STATE MACHINE MECHANICS & FAILURE LINKS
--------------------------------------------------------------------------------
Pattern: A B A B A C

State Table / LPS Array:
 +-----+---+---+---+---+---+---+
 |  i  | 0 | 1 | 2 | 3 | 4 | 5 |
 +-----+---+---+---+---+---+---+
 |  P  | A | B | A | B | A | C |
 | LPS | 0 | 0 | 1 | 2 | 3 | 0 |
 +-----+---+---+---+---+---+---+

State Transition & Fallback Structure (Failure Link Diagram):

   (Match A)    (Match B)    (Match A)    (Match B)    (Match A)    (Match C)
 [0] --------> [1] --------> [2] --------> [3] --------> [4] --------> [5] --------> ((MATCH))
  ^             |             |            |            |            |
  |  (Fail A)   |  (Fail B)   |  (Fail A)  |  (Fail B)  |  (Fail A)  |  (Fail C)
  +-------------+-------------+            |            |            |
  |                                        v            v            v
  +----------------------------------------+------------+------------+
                                         Fallback to State 3 (LPS[4] = 3)

Key Mechanics:
  • Green Transitions: Advance state index upon matching input characters.
  • Fallback Links: Instantly shift pattern pointer j to LPS[j - 1] on mismatch.
  • Result: Guarantees zero text pointer rewinds (O(N) total comparisons).

--------------------------------------------------------------------------------
SLIDE 6: ALGORITHM WALKTHROUGH
--------------------------------------------------------------------------------
Matching Phase Mechanics:

  Text:    A B A B D A B A C D A B A B C A B A B
  Pattern: A B A B C
  Match:   A B A B x  (Mismatch: 'D' vs 'C' at Pattern index 4)

Steps Taken:
  1. Look up LPS[4 - 1] -> LPS[3] = 2 ("AB").
  2. Do NOT move the text pointer backward.
  3. Jump pattern index from 4 to 2.

Next Comparison:
  Text:    A B A B D A B A C D A B A B C A B A B
  Pattern:     A B A B C
               x  (Immediate mismatch 'D' vs 'A'; advance text pointer)

--------------------------------------------------------------------------------
SLIDE 7: COMPLEXITY ANALYSIS
--------------------------------------------------------------------------------
Metric Comparison:

+--------------------------+-----------------+-----------------+
| Metric                   | Naive Algorithm | KMP Algorithm   |
+--------------------------+-----------------+-----------------+
| Preprocessing Time       | O(1)            | O(M)            |
| Matching Time            | O(N * M)        | O(N)            |
| Total Worst-Case Time    | O(N * M)        | O(N + M)        |
| Auxiliary Space          | O(1)            | O(M)            |
+--------------------------+-----------------+-----------------+

Why O(N) Matching Time?
  • The text index i strictly increments and NEVER decrements.
  • The pattern index j falls back at most N times overall throughout search.
  • Amortized work per input character is strictly O(1).

--------------------------------------------------------------------------------
SLIDE 8: REAL-WORLD APPLICATIONS
--------------------------------------------------------------------------------
Where KMP Shines in Production:

  • Streaming Data Processing:
    Ideal for non-seekable inputs (network sockets, live telemetry, continuous
    log files) where moving backward is physically impossible.

  • Bioinformatics & Genomics:
    Fast, deterministic pattern extraction across long sequences with small,
    highly repetitive alphabets (DNA sequences: {A, C, G, T}).

  • Intrusion Detection Systems (IDS):
    Evaluates packet payload signatures against live network traffic buffers in
    real time.

  • Log & Text Processing:
    Efficient single-pass scanning across massive multi-gigabyte log archives.

--------------------------------------------------------------------------------
SLIDE 9: SUMMARY & KEY TAKEAWAYS
--------------------------------------------------------------------------------
  1. Zero Text Backtracking:
     Processes target text strictly left-to-right in a single pass.

  2. Preprocessing Power:
     Invests O(M) time upfront building the LPS array to guarantee deterministic
     O(N) search execution.

  3. Deterministic Performance:
     No worst-case performance penalties or hash collision risks (unlike Rabin-Karp).

  4. Portfolio Ready:
     Implementation, technical specs, and interactive benchmarks available in KMP.py.

================================================================================
                            QUESTIONS & DISCUSSION
                         Created by: Rob Gravelle
                       GitHub: github.com/Rob-Gravelle
================================================================================