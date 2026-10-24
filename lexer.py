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
        elif snippet[i] == '+':
            tokens.append(Token('PLUS', '+'))
            i += 1
        elif snippet[i] == '-':
            tokens.append(Token('MINUS', '-'))
            i += 1
        elif snippet[i] == '*':
            tokens.append(Token('MUL', '*'))
            i += 1
        elif snippet[i] == '/':
            tokens.append(Token('DIV', '/'))
            i += 1
        elif snippet[i] == '(':
            tokens.append(Token('LPAREN', '('))
            i += 1
        elif snippet[i] == ')':
            tokens.append(Token('RPAREN', ')'))
            i += 1
        elif snippet[1].isdigit():
            startindex = i
            while i < len(snippet) and snippet[i].isdigit():
                i += 1
            tokens.append(Token('NUMBERS', snippet[startindex:i]))
            continue
        else: 
            tokens.append(Token("ILLIGAL", + snippet[i]))
        i += 1
    return tokens

snippet = "10 + 59"
print(lex(snippet))