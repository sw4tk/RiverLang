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
            tokens.append(Token('ASSIGN', '='))
            i += 1
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
        else: 
            tokens.append(Token("ILLEGAL", snippet[i]))
        i += 1
    return tokens

snippet = "let x =10 + 59"
print(lex(snippet))