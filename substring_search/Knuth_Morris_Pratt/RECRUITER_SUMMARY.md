
# Algorithm Overview: Knuth-Morris-Pratt (KMP)
**Author:** Rob Gravelle | **Category:** Substring Search / Pattern Matching

# Algorithm Overview: Knuth-Morris-Pratt (KMP)
**Category:** Substring Search / Pattern Matching  
**Primary Benefit:** Guaranteed linear-time search with zero backtracking in the target text.

---

### 1. History & Origin
In 1970, computer scientists Donald Knuth, Vaughan Pratt, and James H. Morris independently discovered that string searching didn't need to be so repetitive. Before KMP, search tools worked like a person reading a document who forgot where they were every time they hit a typo—forcing them to jump back and re-read whole sentences. KMP was published jointly in 1977 as the first algorithm guaranteed to search text in linear time without ever forcing the system to re-read characters it had already processed.

---

### 2. Executive Summary
The Knuth-Morris-Pratt (KMP) algorithm efficiently finds a specific word or phrase (a "pattern") inside a large body of text. 

Traditional search methods often re-read the same passages of text over and over when they run into a partial match that fails. KMP solves this by preprocessing the search term first, allowing it to "remember" what it has already inspected. As a result, it moves through the main document strictly from left to right without ever re-reading a single character.

---

### 3. Real-World Analogy: The "Smart Reader"
Imagine you are proofreading a document, searching for the word **ONION**.

* **The Basic Approach:** You start checking letters: O... N... I... O... but then the next letter is X. Realizing ONIOX is wrong, you move your finger back to the start and check the next spot to try again from scratch.
* **The KMP Approach:** When you hit ONIOX, you realize you already read O-N-I-O. KMP notices that the sequence O-N appears at both the **beginning** and the **end** of ONIO. Instead of starting over at square one, KMP keeps your place in the main text, shifts the word ONION forward so the matching O-N lines up, and keeps reading continuously.

---

### 4. Business & Practical Impact
* **Efficiency:** Guarantees fast search times regardless of how complex or repetitive the input text is.
* **Stream Processing:** Because it never moves backward in the source text, KMP can search **live data streams** (like real-time network traffic or continuous log files) where you cannot "scroll back" to re-read previous data.
* **Predictability:** Unlike some search algorithms whose speed varies wildly based on luck or text composition, KMP provides a reliable, fixed execution time guarantee.