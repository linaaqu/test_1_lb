def r_string(s):
    return s[::-1]

def t_polindrome(s):
    return s == s[::-1]

def e_vowels(s):
    vowels = "aeiouyAEIOUY"
    return ''.join([char for char in s if char in vowels])

def r_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))
