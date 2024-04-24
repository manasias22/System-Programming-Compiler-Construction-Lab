#Code Optimization for common sub expression

class CodeOptimizer:
    @staticmethod
    def optimize(intermediate_code):
        expression_table = {}  # To store expressions and their corresponding temporary variables
        optimized_code = []

        for line in intermediate_code:
            if "=" in line:
                parts = line.split("=")
                left_side = parts[0].strip()
                right_side = parts[1].strip()

                # Check if the right side is a common subexpression
                if right_side in expression_table:
                    optimized_line = f"{left_side} = {expression_table[right_side]}"
                    optimized_code.append(optimized_line)
                else:
                    optimized_code.append(line)

                    # Update expression table if the right side is not a common subexpression
                    expression_table[right_side] = left_side
            else:
                # Replace common subexpressions in non-assignment statements
                for expression, temp_variable in expression_table.items():
                    line = line.replace(expression, temp_variable)
                optimized_code.append(line)

        return optimized_code


# Example usage:
intermediate_code = [
    "b = c + d",
    "e = c + d",
    "f = b + e",
    "r = f"
]

optimized_code = CodeOptimizer.optimize(intermediate_code)
for line in optimized_code:
    print(line)
