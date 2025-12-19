#https://open.kattis.com/problems/anewalphabet

new_alphabet = {
    'a': '@',   'b': '8',   'c': '(',   'd': '|)',  'e': '3',
    'f': '#',   'g': '6',   'h': '[-]', 'i': '|',   'j': '_|',
    'k': '|<',  'l': '1',   'm': '[]\\/[]','n': '[]\\[]', 'o': '0',
    'p': '|D',  'q': '(,)', 'r': '|Z',  's': '$',   't': "']['",
    'u': '|_|', 'v': '\\/',  'w': '\\/\\/', 'x': '}{', 'y': '`/', 'z': '2'
}

def solve(text):

    result = ""
    for s in text:
        sl = s.lower()
        if sl in new_alphabet.keys():
            result = result + new_alphabet[sl]
        else:
            result = result + sl

    return result

solve("All your base are belong to us.")