from lexer import lex

def repl():
    while True: 
        try:    
            snippet = input(">> ")
            if snippet == "exit":
                break
            tokens = lex(snippet)
            for token in tokens:
                print(f"Token Type: {token.type}, Literal: {token.literal}")
        except KeyboardInterrupt:
            print("\nExiting REPL.")
            break
repl()