"""
Automated Test Suite for Knuth-Morris-Pratt (KMP) Substring Search
Framework: pytest
Execution: python -m pytest test_kmp.py -v
"""

import pytest
from KMP import build_lps, kmp_search


def test_build_lps():
    """Verify LPS table construction against known prefix-suffix lengths."""
    assert build_lps("ABABAC") == [0, 0, 1, 2, 3, 0]
    assert build_lps("AAAA") == [0, 1, 2, 3]
    assert build_lps("ABCDE") == [0, 0, 0, 0, 0]


def test_standard_match():
    """Verify standard single pattern match in target text."""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    assert kmp_search(text, pattern) == [10]


def test_overlapping_matches():
    """Verify KMP correctly detects overlapping pattern occurrences."""
    assert kmp_search("AAAAA", "AAA") == [0, 1, 2]


def test_no_match():
    """Verify behavior when pattern does not exist in target text."""
    assert kmp_search("ABCDEFG", "XYZ") == []


def test_pattern_equals_text():
    """Verify exact full-string match."""
    assert kmp_search("KMP", "KMP") == [0]


def test_pattern_longer_than_text():
    """Verify behavior when pattern length exceeds text length."""
    assert kmp_search("ABC", "ABCDE") == []


def test_empty_pattern():
    """Verify guard clause handling when pattern is an empty string."""
    assert kmp_search("ABC", "") == []


def test_empty_text():
    """Verify guard clause handling when text is an empty string."""
    assert kmp_search("", "ABC") == []


def test_both_empty():
    """Verify guard clause handling when both inputs are empty strings."""
    assert kmp_search("", "") == []


def test_unicode():
    """Verify character encoding stability with unicode and emoji inputs."""
    assert kmp_search("naïve naïve", "naïve") == [0, 6]
    assert kmp_search("🐍⭐🐍⭐🐍", "🐍⭐") == [0, 2]