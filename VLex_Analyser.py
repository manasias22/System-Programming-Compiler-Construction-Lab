import re

MAX_LENGTH = 100

def isDelimiter(chr):
    return chr in [' ', '+', '-', '*', '/', ',', ';', '%', '>', '<', '=', '(', ')', '[', ']', '{', '}']

def isOperator(chr):
    return chr in ['+', '-', '*', '/', '>', '<', '=']

def isValidIdentifier(s):
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', s))

def isKeyword(s):
    keywords = ["auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else",
                "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return",
                "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union",
                "unsigned", "void", "volatile", "while"]
    return s in keywords

def isInteger(s):
    return s.isdigit()

def getSubstring(s, start, end):
    return s[start:end+1]

def lexicalAnalyzer(input_str):
    left = 0
    right = 0
    length = len(input_str)

    while right < length:
        if isDelimiter(input_str[right]):
            if left != right:
                sub_str = getSubstring(input_str, left, right - 1)
                if isOperator(sub_str):
                    print("Token: Operator, Value:", sub_str)
                elif isKeyword(sub_str):
                    print("Token: Keyword, Value:", sub_str)
                elif isInteger(sub_str):
                    print("Token: Integer, Value:", sub_str)
                elif isValidIdentifier(sub_str):
                    print("Token: Identifier, Value:", sub_str)
                else:
                    print("Token: Unidentified, Value:", sub_str)
            if isOperator(input_str[right]):
                print("Token: Operator, Value:", input_str[right])
            left = right + 1
        right += 1

# Main function
if __name__ == "__main__":
    # Input 01
    lex_input = " int a = b + c "
    print("For Expression \"{}\":\n".format(lex_input))
    lexicalAnalyzer(lex_input)
    print("")

    # Input 02
    lex_input01 = "int x=ab+bc+30+switch+ 0y "
    print("For Expression \"{}\":\n".format(lex_input01))
    lexicalAnalyzer(lex_input01)
