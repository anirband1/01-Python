output = ""
engtxt = input("what do you want coded?   ")
morse ={
    'a': '/.-',
    'b': '/-...',
    'c': '/-.-.',
    'd': '/-..',
    'e': '/.',
    'f': '/..-.',
    'g': '/--.',
    'h': '/....',
    'i': '/..',
    'j': '/.---',
    'k': '/-.-',
    'l': '/.-..',
    'm': '/--',
    'n': '/-.',
    'o': '/---',
    'p': '/.--.',
    'q': '/--.-',
    'r': '/.-.',
    's': '/...',
    't': '/-',
    'u': '/..-',
    'v': '/...-',
    'w': '/.--',
    'x': '/-..-',
    'y': '/-.--',
    'z': '/--..',
    '1': '/.----',
    '2': '/..---',
    '3': '/...--',
    '4': '/....-',
    '5': '/.....',
    '6': '/-....',
    '7': '/--...',
    '8': '/---..',
    '9': '/----.',
    '0': '/-----',
    '.': '/.-.-.-',
    ',': '/--..--',
    '?': '/..--..',
    '@': '/.--.-.',
    ' ': '/'
}
for char in engtxt.lower():
    try:
        output+=morse[char]
    except:
        print(char,'is an invalid symbol')
print(output)