
LETTER = 0
DIGIT = 1
UNKNOWN = 99

INT_LIT = 10
IDENT = 11
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26

char_class = None
lexeme = []
next_char = ''
next_token = None
input_str = "(sum + 66) / total"
index = 0

def add_char():
    if len(lexeme) < 98:
        lexeme.append(next_char)
    else:
        print("Error - lexeme is too long")

def get_char():
    global next_char, char_class, index
    if index < len(input_str):
        next_char = input_str[index]
        index += 1
        if next_char.isalpha():
            char_class = LETTER
        elif next_char.isdigit():
            char_class = DIGIT
        else:
            char_class = UNKNOWN
    else:
        next_char = ''
        char_class = None  

def get_non_blank():
    while next_char.isspace():
        get_char()

def lookup(ch):
    global next_token
    lookup_dict = {
        '(': LEFT_PAREN,
        ')': RIGHT_PAREN,
        '+': ADD_OP,
        '-': SUB_OP,
        '*': MULT_OP,
        '/': DIV_OP
    }
    add_char()
    next_token = lookup_dict.get(ch, None)
    return next_token

def lex():
    global lexeme, next_token
    lexeme = []
    get_non_blank()

    if char_class == LETTER:
        add_char()
        get_char()
        while char_class in (LETTER, DIGIT):
            add_char()
            get_char()
        next_token = IDENT

    elif char_class == DIGIT:
        add_char()
        get_char()
        while char_class == DIGIT:
            add_char()
            get_char()
        next_token = INT_LIT

    elif char_class == UNKNOWN:
        lookup(next_char)
        get_char()

    elif char_class is None:
        next_token = -1
        lexeme.extend(['E', 'O', 'F'])

    print(f"Next token is: {next_token}, Next lexeme is {''.join(lexeme)}")
    return next_token

def main():
    get_char()
    while True:
        token = lex()
        if token == -1:
            break

if __name__ == "__main__":
    main()
