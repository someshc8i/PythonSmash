""" Tokens defining syntaxes in the language"""

RESERVED = 'RESERVED'
INT = 'INT'
ID = 'ID'


token_exprs = [
    (r'[ \n\t]+',              None),
    (r'#[^\n]*',               None),
    ]

token_exprs += [
    (r'\:=',                   RESERVED),
    (r'\(',                    RESERVED),
    (r'\)',                    RESERVED),
    (r';',                     RESERVED),
    (r'\+',                    RESERVED),
    (r'-',                     RESERVED),
    (r'\*',                    RESERVED),
    (r'/',                     RESERVED),
    (r'<=',                    RESERVED),
    (r'<',                     RESERVED),
    (r'>=',                    RESERVED),
    (r'>',                     RESERVED),
    (r'=',                     RESERVED),
    (r'!=',                    RESERVED),
    (r'and',                   RESERVED),
    (r'or',                    RESERVED),
    (r'not',                   RESERVED),
    (r'if',                    RESERVED),
    (r'then',                  RESERVED),
    (r'else',                  RESERVED),
    (r'while',                 RESERVED),
    (r'do',                    RESERVED),
    (r'end',                   RESERVED),
]


token_exprs += [
      (r'[0-9]+',                INT),
      (r'[A-Za-z][A-Za-z0-9_]*', ID),
]
