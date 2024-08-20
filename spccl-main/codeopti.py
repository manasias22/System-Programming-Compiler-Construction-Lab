
def constant_folding(code):
    folded_code = []
    for line in code:
        if '=' in line:
            var, expr = line.split('=')
            var = var.strip()
            try:
                result = eval(expr.strip(), {})
                folded_code.append(f"{var} = {result}")
            except:
                folded_code.append(line)
        else:
            folded_code.append(line)
    return folded_code

def constant_propagation(code):
    symbol_table = {}
    optimized_code = []
    for line in code:
        if '=' in line:
            var, expr = line.split('=')
            var = var.strip()
            if all(char.isdigit() or char == '.' for char in expr.strip()):
                symbol_table[var] = expr.strip()
            else:
                for key, value in symbol_table.items():
                    expr = expr.replace(key, value)
                optimized_code.append(f"{var} = {expr.strip()}")
        else:
            optimized_code.append(line)
    return optimized_code

# Example usage
if __name__ == "__main__":
    code = [
        "a = 10",
        "b = 5",
        "c = a + b * 2",
        "d = c * 2 + a",
        "e = c + b * 3",
        "f = d - e"
    ]
    
    print("\nConstant Propagation:")
    optimized_code_propagation = constant_propagation(code)
    for line in optimized_code_propagation:
        print(line)

	    
    print("Constant Folding:")
    optimized_code_folding = constant_folding(optimized_code_propagation)
    for line in optimized_code_folding:
        print(line)


# OUTPUT
# Constant Propagation:
# c = 10 + 5 * 2
# d = c * 2 + 10
# e = c + 5 * 3
# f = d - e
# Constant Folding:
# c = 20
# d = c * 2 + 10
# e = c + 5 * 3
# f = d - e