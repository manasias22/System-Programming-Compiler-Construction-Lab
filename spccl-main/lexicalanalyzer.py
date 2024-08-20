import re

TOKENS = [
    ('IDENTIFIER', r'[a-zA-Z_]\w*'), 
    ('CONSTANT', r'\d+(\.\d+)?'),     
    ('LITERAL', r'\".*?\"'),          
    ('OPERATOR', r'\+|\-|\*|\/|=|==|!=|<|>|<=|>=|&&|\|\|'), 
    ('PUNCTUATOR', r'\(|\)|\{|\}|\[|\]|,|;'),            
    ('WHITESPACE', r'\s+'),          
    ('NEWLINE', r'\n'),                
]

def lexer(input_string):
    tokens = []
    position = 0
    
    while position < len(input_string):
        match = None
        for token_type, regex_pattern in TOKENS:
            regex = re.compile(regex_pattern)
            match = regex.match(input_string, position)
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE' and token_type != 'NEWLINE':
                    tokens.append((token_type, value))
                position = match.end()  
                print(f"Matched: {token_type} - '{value}'")
                break
        
        if not match:
            raise ValueError(f'Invalid character at position {position}')
    
    return tokens


input_string = "x=10 + y * 5; if (x > 0) { print(\"x is positive\"); }"
tokens = lexer(input_string)
for token in tokens:
    print(token)

# OUTPUT
# Matched: IDENTIFIER - 'x'
# Matched: OPERATOR - '='
# Matched: CONSTANT - '10'
# Matched: WHITESPACE - ' '
# Matched: OPERATOR - '+'
# Matched: WHITESPACE - ' '
# Matched: IDENTIFIER - 'y'
# Matched: WHITESPACE - ' '
# Matched: OPERATOR - '*'
# Matched: WHITESPACE - ' '
# Matched: CONSTANT - '5'
# Matched: PUNCTUATOR - ';'
# Matched: WHITESPACE - ' '
# Matched: IDENTIFIER - 'if'
# Matched: WHITESPACE - ' '
# Matched: PUNCTUATOR - '('
# Matched: IDENTIFIER - 'x'
# Matched: WHITESPACE - ' '
# Matched: OPERATOR - '>'
# Matched: WHITESPACE - ' '
# Matched: CONSTANT - '0'
# Matched: PUNCTUATOR - ')'
# Matched: WHITESPACE - ' '
# Matched: PUNCTUATOR - '{'
# Matched: WHITESPACE - ' '
# Matched: IDENTIFIER - 'print'
# Matched: PUNCTUATOR - '('
# Matched: LITERAL - '"x is positive"'
# Matched: PUNCTUATOR - ')'
# Matched: PUNCTUATOR - ';'
# Matched: WHITESPACE - ' '
# Matched: PUNCTUATOR - '}'
# ('IDENTIFIER', 'x')
# ('OPERATOR', '=')
# ('CONSTANT', '10')
# ('OPERATOR', '+')
# ('IDENTIFIER', 'y')
# ('OPERATOR', '*')
# ('CONSTANT', '5')
# ('PUNCTUATOR', ';')
# ('IDENTIFIER', 'if')
# ('PUNCTUATOR', '(')
# ('IDENTIFIER', 'x')
# ('OPERATOR', '>')
# ('CONSTANT', '0')
# ('PUNCTUATOR', ')')
# ('PUNCTUATOR', '{')
# ('IDENTIFIER', 'print')
# ('PUNCTUATOR', '(')
# ('LITERAL', '"x is positive"')
# ('PUNCTUATOR', ')')
# ('PUNCTUATOR', ';')
# ('PUNCTUATOR', '}')