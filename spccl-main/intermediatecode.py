class ThreeAddressGenerator:
    def __init__(self):
        self.temp_count = 1

    def generate_temp(self):
        temp = f"T{self.temp_count}"
        self.temp_count += 1
        return temp

    def postfix_to_three_address(self, postfix):
        stack = []
        three_address_code = []
        for token in postfix:
            if token.isalnum():
                stack.append(token)
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                temp = self.generate_temp()
                three_address_code.append(f"{temp} = {op1} {token} {op2}")
                stack.append(temp)
        return three_address_code

    def infix_to_postfix(self, infix):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
        postfix = []
        stack = []
        # Remove spaces from the input expression
        infix = infix.replace(" ", "")
        for token in infix:
            if token.isalnum():
                postfix.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                # Pop operators until '(' is encountered
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()  # Remove '('
            else:
                # Pop operators with higher or equal precedence
                while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                    postfix.append(stack.pop())
                stack.append(token)
        # Append remaining operators from stack
        postfix.extend(stack[::-1])
        return postfix


if __name__ == "__main__":
    generator = ThreeAddressGenerator()

    infix_expr = input("Enter the infix expression: ")
    postfix_expr = generator.infix_to_postfix(infix_expr)
    postfix_str = ' '.join(postfix_expr)
    print("Postfix representation of the expression:", postfix_str)

    postfix_tokens = postfix_expr
    three_address_code = generator.postfix_to_three_address(postfix_tokens)
    print("\nThree-address code for the expression:")
    for code in three_address_code:
        print(code)


# OUTPUT
# Enter the infix expression: a+b*c
# Postfix representation of the expression: a b c * +

# Three-address code for the expression:
# T1 = b * c
# T2 = a + T1