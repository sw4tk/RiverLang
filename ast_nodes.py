from dataclasses import dataclass
from lexer import Token

class Node: 
    pass

class Statement(Node):
    pass

class Expression(Node):
    pass

@dataclass
class Program(Node):
    statement : list[Statement]
    
@dataclass
class Identifier(Expression):
    value : str
    token : Token
    
@dataclass
class LetStatement(Statement):
    name : Token
    value : Expression
    name : Identifier