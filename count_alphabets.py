def hasAllAlphabet(txt):
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    txt_list = txt.lower()
    res = set()
    txt_list = txt_list.replace(" ", '')
    for i in txt_list:
        res.add(i)
    if len(res) == len(alphabet_list):
        return True
    else:
        return False


print(hasAllAlphabet('afdjhaguguilg afdjhaguguilg afdjhaguguilg'))
print(hasAllAlphabet('aaaaa aaaaa aaaaa aaaaa aaaaa aaaaa aaaaa'))
print(hasAllAlphabet('aeiod aeiod aeiod aeiod aeiod aeiod aeiod aeiod'))
print(hasAllAlphabet('The quick brown fox jumps over the lazy dog'))
