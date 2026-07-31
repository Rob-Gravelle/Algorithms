"""
Rabin-Karp Substring Search Algorithm
Author: Rob Gravelle
Complexity: Time O(n + m) avg, O(n * m) worst | Space O(1) auxiliary
"""

from typing import List


def rabin_karp_search(
    text: str, pattern: str, base: int = 256, prime: int = 101
) -> List[int]:
    """
    Searches for all occurrences of 'pattern' in 'text' using the Rabin-Karp rolling hash.

    Args:
        text (str): The target text/string buffer.
        pattern (str): The pattern string to locate.
        base (int): Size of the character alphabet (default 256 for extended ASCII).
        prime (int): A prime number used for modulo hashing to prevent overflow.

    Returns:
        List[int]: Starting indices where pattern matches occur.

    Examples:
        >>> rabin_karp_search("ABABDABACDABABCABAB", "ABABC")
        [10]
        >>> rabin_karp_search("AAAAA", "AAA")
        [0, 1, 2]
    """
    n = len(text)
    m = len(pattern)

    # Guard clauses
    if not pattern or not text or m > n:
        return []

    matches = []
    pattern_hash = 0
    window_hash = 0
    h = 1

    # The value of h would be pow(base, m-1) % prime
    for i in range(m - 1):
        h = (h * base) % prime

    # Calculate initial hash value for pattern and first window of text
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        window_hash = (base * window_hash + ord(text[i])) % prime

    # Slide the pattern over target text
    for i in range(n - m + 1):
        # Check if hash values of current window and pattern match
        if pattern_hash == window_hash:
            # Character-by-character verification to handle hash collisions
            if text[i : i + m] == pattern:
                matches.append(i)

        # Calculate hash value for next window of text
        # Remove leading character, add trailing character
        if i < n - m:
            window_hash = (
                base * (window_hash - ord(text[i]) * h) + ord(text[i + m])
            ) % prime

            # We might get negative hash values, convert to positive
            if window_hash < 0:
                window_hash += prime

    return matches


def rabin_karp_multi_search(
    text: str, patterns: List[str], base: int = 256, prime: int = 101
) -> dict:
    """
    Multi-pattern search using Rabin-Karp. Calculates hashes for multiple patterns 
    of equal length to evaluate against text windows in a single pass.

    Args:
        text (str): Target text.
        patterns (List[str]): List of equal-length search patterns.

    Returns:
        dict: Mapping of pattern -> list of starting index matches.
    """
    if not text or not patterns:
        return {}

    # Group patterns by length for batch sliding window evaluation
    results = {p: [] for p in patterns}
    
    # Filter out invalid patterns
    valid_patterns = [p for p in patterns if p and len(p) <= len(text)]
    if not valid_patterns:
        return results

    # Process per pattern length
    lengths = set(len(p) for p in valid_patterns)

    for m in lengths:
        sub_patterns = [p for p in valid_patterns if len(p) == m]
        pattern_hashes = {p: 0 for p in sub_patterns}

        h = pow(base, m - 1, prime)

        # Hash all patterns of current length
        for p in sub_patterns:
            ph = 0
            for char in p:
                ph = (base * ph + ord(char)) % prime
            pattern_hashes[p] = ph

        # Calculate initial window hash
        window_hash = 0
        for i in range(m):
            window_hash = (base * window_hash + ord(text[i])) % prime

        # Slide window across text
        for i in range(len(text) - m + 1):
            for p, ph in pattern_hashes.items():
                if ph == window_hash and text[i : i + m] == p:
                    results[p].append(i)

            if i < len(text) - m:
                window_hash = (
                    base * (window_hash - ord(text[i]) * h) + ord(text[i + m])
                ) % prime
                if window_hash < 0:
                    window_hash += prime

    return results


if __name__ == "__main__":
    sample_text = "ABABDABACDABABCABAB"
    sample_pattern = "ABABC"

    print("=" * 60)
    print("Rabin-Karp Rolling Hash Search Demo")
    print("=" * 60)
    print(f"Text:     {sample_text}")
    print(f"Pattern:  {sample_pattern}\n")

    matches = rabin_karp_search(sample_text, sample_pattern)
    print(f"Match Indices Found: {matches}")

    # Multi-pattern search demo
    patterns = ["ABABC", "ABABA", "AB"]
    print(f"\nMulti-Pattern Search for: {patterns}")
    multi_results = rabin_karp_multi_search(sample_text, patterns)
    print(f"Results: {multi_results}")
    print("=" * 60)