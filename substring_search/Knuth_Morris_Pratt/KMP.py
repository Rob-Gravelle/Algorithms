"""
Knuth-Morris-Pratt (KMP) Substring Search Algorithm
Author: Robert Gravelle 
Portfolio Project
Time Complexity: O(n + m)
Space Complexity: O(m)
"""

from typing import List


def build_lps(pattern: str) -> List[int]:
    """
    Builds the Longest Prefix Suffix (LPS) array for the given pattern.
    LPS[i] = length of the longest proper prefix of pattern[0..i]
             that is also a suffix of pattern[0..i].
    """
    lps = [0] * len(pattern)
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Fallback to the previous longest prefix length
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text: str, pattern: str) -> List[int]:
    """
    Searches for all occurrences of 'pattern' in 'text' using KMP algorithm.
    Returns a list of starting indices where pattern is found.
    """
    if not pattern or not text or len(pattern) > len(text):
        return []

    lps = build_lps(pattern)
    matches = []

    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            # Found pattern at index (i - j)
            matches.append(i - j)
            j = lps[j - 1]  # Reset j using LPS to find next match

        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]  # Skip redundant comparisons
            else:
                i += 1

    return matches


# Demo execution
if __name__ == "__main__":
    sample_text = "ABABDABACDABABCABAB"
    sample_pattern = "ABABCABAB"

    print(f"Text:    {sample_text}")
    print(f"Pattern: {sample_pattern}")
    
    lps_table = build_lps(sample_pattern)
    print(f"LPS Array: {lps_table}")

    results = kmp_search(sample_text, sample_pattern)
    print(f"Pattern found at indices: {results}")