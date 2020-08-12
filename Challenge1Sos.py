sos = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
       'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
       'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
       'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', }


def sos_gen(code):
    final_code = ''
    for i in code:
        for k, v in sos.items():
            if i.lower() == k:
                final_code += v
    print(final_code)


sos_gen('SOS')
sos_gen("I'll build your bot this weekend hue hue hue")