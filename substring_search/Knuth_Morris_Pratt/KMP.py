"""
Knuth-Morris-Pratt (KMP) Substring Search Algorithm
Author: Rob Gravelle 
Complexity: Time O(n + m) | Space O(m)
"""

from typing import List


def build_lps(pattern: str) -> List[int]:
    """
    Constructs the Longest Prefix Suffix (LPS) array for the given pattern.
    
    LPS[i] stores the length of the longest proper prefix of pattern[0..i]
    that is also a suffix of pattern[0..i].

    Args:
        pattern (str): The search pattern.

    Returns:
        List[int]: Precomputed partial match / failure table.

    Example:
        >>> build_lps("ABABAC")
        [0, 0, 1, 2, 3, 0]
    """
    if not pattern:
        return []

    lps = [0] * len(pattern)
    length = 0  # Length of previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text: str, pattern: str) -> List[int]:
    """
    Searches for all occurrences of 'pattern' inside 'text' using the KMP algorithm.

    Guarantees O(n) search time with zero text pointer backtracking.

    Args:
        text (str): The target document or string buffer.
        pattern (str): The search pattern to locate.

    Returns:
        List[int]: List of 0-based starting indices where pattern matches occur.

    Examples:
        >>> kmp_search("ABABDABACDABABCABAB", "ABABCABAB")
        [10]
        >>> kmp_search("AAAAA", "AAA")
        [0, 1, 2]
    """
    # Guard clauses for empty string or invalid length edge cases
    if not pattern or not text or len(pattern) > len(text):
        return []

    lps = build_lps(pattern)
    matches = []

    i = 0  # Pointer for text
    j = 0  # Pointer for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            # Record starting index of the match
            matches.append(i - j)
            # Shift pattern pointer via failure table to catch overlaps
            j = lps[j - 1]

        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


if __name__ == "__main__":
    sample_text = "ABABDABACDABABCABAB"
    sample_pattern = "ABABCABAB"

    print("=" * 60)
    print("Knuth-Morris-Pratt (KMP) Search Demo")
    print("=" * 60)
    print(f"Text:     {sample_text}")
    print(f"Pattern:  {sample_pattern}\n")
    
    lps_table = build_lps(sample_pattern)
    print(f"LPS Table: {lps_table}")

    results = kmp_search(sample_text, sample_pattern)
    print(f"Match Indices Found: {results}")
    print("=" * 60)