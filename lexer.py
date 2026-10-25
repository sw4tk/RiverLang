from dataclasses import dataclass

@dataclass
class Token:
    type : str
    literal : str

def lex(snippet : str):
    tokens = []
    i = 0

    while i < len(snippet):
        if snippet[i] == ' ':
            i += 1
            continue
        elif snippet[i] == '=':
            if i + 1 < len(snippet) and snippet[i + 1] == '=':
                tokens.append(Token('EQ', '=='))
                i += 1
            else:
                tokens.append(Token('ASSIGN', '='))
        elif snippet[i] == '+':
            tokens.append(Token('PLUS', '+'))
        elif snippet[i] == '-':
            tokens.append(Token('MINUS', '-'))
        elif snippet[i] == '*':
            tokens.append(Token('MUL', '*'))
        elif snippet[i] == '/':
            tokens.append(Token('DIV', '/'))
        elif snippet[i] == '(':
            tokens.append(Token('LPAREN', '('))
        elif snippet[i] == ')':
            tokens.append(Token('RPAREN', ')'))
        elif snippet[i].isdigit():
            startindex = i
            while i < len(snippet) and snippet[i].isdigit():
                i += 1
            tokens.append(Token('NUMBER', snippet[startindex:i]))
            continue
        elif snippet[i].isalpha():
            keywords = ['let','fn','data']
            startindex = i
            while i < len(snippet) and snippet[i].isalpha():
                i += 1
            if snippet[startindex:i] in keywords:
                tokens.append(Token(f'{snippet[startindex:i].upper()}', snippet[startindex:i]))     
            else:           
                tokens.append(Token('IDENT', snippet[startindex:i]))
            continue
        elif snippet[i] == ';':
            tokens.append(Token('SEMICOLON', ';'))
        elif snippet[i] == '{':
            tokens.append(Token('LBRACE', '{'))
        elif snippet[i] == '}':
            tokens.append(Token('RBRACE', '}'))
        else: 
            tokens.append(Token("ILLEGAL", snippet[i]))
        i += 1
    return tokens


