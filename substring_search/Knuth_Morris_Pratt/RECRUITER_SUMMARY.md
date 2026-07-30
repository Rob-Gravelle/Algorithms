# Algorithm Overview: Knuth-Morris-Pratt (KMP)
**Author:** Rob Gravelle  
**Category:** Substring Search / Pattern Matching  
**Complexity:** Time $O(n + m)$ | Space $O(m)$  
**Primary Benefit:** Guaranteed linear-time search with zero backtracking in the target text.

---

### 1. History & Origin
In 1970, computer scientists Donald Knuth, Vaughan Pratt, and James H. Morris independently discovered that string searching didn't need to be so repetitive. Before KMP, search tools worked like a person reading a document who forgot where they were every time they hit a typo—forcing them to jump back and re-read whole sentences. KMP was published jointly in 1977 as the first algorithm guaranteed to search text in linear time without ever forcing the system to re-read characters it had already processed.

---

### 2. Executive Summary
The Knuth-Morris-Pratt (KMP) algorithm efficiently finds a specific word or phrase (a "pattern") inside a large body of text. 

Traditional search methods often re-read the same passages of text over and over when they run into a partial match that fails. KMP solves this by preprocessing the search term first, allowing it to "remember" what it has already inspected. As a result, it moves through the main document strictly from left to right without ever re-reading a single character.

---

### 3. Real-World Analogy: The Smart Reader

Imagine searching for the pattern **`ABABAC`** inside a long document. 

1. Suppose the algorithm matches **`ABABA`**, but then hits a mismatch on the 6th character.
2. Instead of restarting the search from the beginning, KMP analyzes the portion of the pattern that has already matched. (**`ABABA`**).
3. It recognizes that **`ABA`** appears at both the **beginning** (prefix) and the **end** (suffix) of the matched text.
4. Because those 3 characters (**`ABA`**) are guaranteed to match, KMP shifts the pattern forward and resumes checking from the 4th character (`B`), **saving 3 redundant character checks instantly**.

---

### 4. Business & Practical Impact
* **Efficiency:** Guarantees fast search times regardless of how complex or repetitive the input text is.
* **Stream Processing:** Because it never moves backward in the source text, KMP can search **live data streams** (like real-time network traffic or continuous log files) where you cannot "scroll back" to re-read previous data.
* **Predictability:** Unlike some search algorithms whose speed varies wildly based on luck or text composition, KMP provides a reliable, fixed execution time guarantee.

### Key Takeaways

1. Guarantees O(n + m) worst-case performance.
2. Never backtracks in the text.
3. Ideal for large documents and streaming data.
4. Uses an LPS (Longest Prefix Suffix) table to skip redundant comparisons.
5. Frequently taught in computer science because it introduces preprocessing to eliminate repeated work.