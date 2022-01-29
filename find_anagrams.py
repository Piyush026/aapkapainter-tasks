def find_anagram(val, val1):
    s1 = val.lower()
    s2 = val1.lower()
    if sorted(s1) == sorted(s2):
        return "YES"
    else:
        return "NO"


s1 = "Mary"
s2 = "Army"
find_anagram(s1, s2)
