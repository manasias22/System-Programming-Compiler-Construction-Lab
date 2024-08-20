
def parse_input(input_string):

    def E():
        nonlocal cursor
        print(f"{cursor.ljust(16)} E -> T E'")
        if T():
            if Edash():
                return True
            else:
                return False
        else:
            return False


    def Edash():
        nonlocal cursor
        if cursor and cursor[0] == '+':
            print(f"{cursor.ljust(16)} E' -> + T E'")
            cursor = cursor[1:]
            if T():
                if Edash():
                    return True
                else:
                    return False
            else:
                return False
        else:
            print(f"{cursor.ljust(16)} E' -> $")
            return True

    def T():
        nonlocal cursor
        print(f"{cursor.ljust(16)} T -> F T'")
        if F():
            if Tdash():
                return True
            else:
                return False
        else:
            return False

 
    def Tdash():
        nonlocal cursor
        if cursor and cursor[0] == '*':
            print(f"{cursor.ljust(16)} T' -> * F T'")
            cursor = cursor[1:]
            if F():
                if Tdash():
                    return True
                else:
                    return False
            else:
                return False
        else:
            print(f"{cursor.ljust(16)} T' -> $")
            return True

   
    def F():
        nonlocal cursor
        if cursor and cursor[0] == '(':
            print(f"{cursor.ljust(16)} F -> ( E )")
            cursor = cursor[1:]
            if E():
                if cursor and cursor[0] == ')':
                    cursor = cursor[1:]
                    return True
                else:
                    return False
            else:
                return False
        elif cursor and cursor[0] == 'i':
            print(f"{cursor.ljust(16)} F -> i")
            cursor = cursor[1:]
            return True
        else:
            return False

    cursor = input_string
    if E() and not cursor:
        print("--------------------------------")
        print("String is successfully parsed")
        return True
    else:
        print("--------------------------------")
        print("Error in parsing String")
        return False


# Main function
def main():
    print("Enter the string:")
    input_string = input().strip()  
    print("\nInput          Action")
    print("--------------------------------")
    if parse_input(input_string):
        return 0
    else:
        return 1


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)


# OUTPUT
# Enter the string:
# i+(i*i)

# Input          Action
# --------------------------------
# i+(i*i)          E -> T E'
# i+(i*i)          T -> F T'
# i+(i*i)          F -> i
# +(i*i)           T' -> $
# +(i*i)           E' -> + T E'
# (i*i)            T -> F T'
# (i*i)            F -> ( E )
# i*i)             E -> T E'
# i*i)             T -> F T'
# i*i)             F -> i
# *i)              T' -> * F T'
# i)               F -> i
# )                T' -> $
# )                E' -> $
#                  T' -> $
#                  E' -> $
# --------------------------------
# String is successfully parsed