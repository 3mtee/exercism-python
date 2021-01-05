def find_anagrams(word: str, candidates):
    l_word = word.lower()
    l_candidates = [c.lower() for c in candidates]
    return [c for c, l in zip(candidates, l_candidates) if sorted(l) == sorted(l_word) and l != l_word]
