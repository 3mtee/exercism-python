def find_anagrams(word: str, candidates):
    return [c for c in candidates if is_anagram(word, c)]


def is_anagram(word: str, candidate: str):
    l_word = word.lower()
    l_candidate = candidate.lower()
    return sorted(l_candidate) == sorted(l_word) and l_candidate != l_word
