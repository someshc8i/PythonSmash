import sys
import re
from tokens import token_exprs


def lexer(characters, token_exprs):
    """The lexer function which takes inputs of characters and
    predefined tokens and return the tokens with mapping present in
     the list of charcters.
    """
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens


def lex(characters):
    """The actual function taking characters as input and
     calling lexer function to generate array of tokens.
     """
    # for c in characters:
    #     print(c)
    # print(characters)
    return lexer(characters, token_exprs)
