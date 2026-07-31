"""
Automated Test Suite for Rabin-Karp Substring Search
Framework: pytest
Execution: python -m pytest test_rabin_karp.py -v
"""

import pytest
from Rabin_Karp import rabin_karp_search, rabin_karp_multi_search


def test_standard_match():
    """Verify standard single pattern match in target text."""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABC"
    assert rabin_karp_search(text, pattern) == [10]


def test_overlapping_matches():
    """Verify Rabin-Karp correctly detects overlapping pattern occurrences."""
    assert rabin_karp_search("AAAAA", "AAA") == [0, 1, 2]


def test_no_match():
    """Verify behavior when pattern does not exist in target text."""
    assert rabin_karp_search("ABCDEFG", "XYZ") == []


def test_pattern_equals_text():
    """Verify exact full-string match."""
    assert rabin_karp_search("RABINKARP", "RABINKARP") == [0]


def test_pattern_longer_than_text():
    """Verify behavior when pattern length exceeds text length."""
    assert rabin_karp_search("ABC", "ABCDE") == []


def test_empty_pattern_or_text():
    """Verify guard clause handling for empty string inputs."""
    assert rabin_karp_search("ABC", "") == []
    assert rabin_karp_search("", "ABC") == []
    assert rabin_karp_search("", "") == []


def test_unicode():
    """Verify character encoding stability with unicode and emoji inputs."""
    assert rabin_karp_search("naïve naïve", "naïve") == [0, 6]
    assert rabin_karp_search("🐍⭐🐍⭐🐍", "🐍⭐") == [0, 2]


def test_multi_pattern_search():
    """Verify multi-pattern hash comparison."""
    text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    patterns = ["FOX", "DOG", "CAT"]
    results = rabin_karp_multi_search(text, patterns)
    assert results["FOX"] == [16]
    assert results["DOG"] == [40]
    assert results["CAT"] == []