# Brian Waldron
# G00350150
# Code adapted from Lab exercises

def shunt(infix):
    """Convert infix expressions to postfix"""
    # The eventual output
    postfix = ""
    # The shunting yard operator stack
    stack = ""
    # Operator precedence
    prec = {'*': 100, '.': 90, '|': 80}
    # Loop through the input a character at a time
    for c in infix:
        # c isan operator
        if c in {'*', '.', '|'}:
            # Check what is on the stack
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                # AppendMove operator at top of stack to output
                postfix = postfix + stack[-1]
                # Remove operator from stack
                stack = stack[:-1]
            # Push c to stack
            stack = stack + c
        elif c == '(':
            # Push c to stack
            stack = stack + c
        elif c == ')':
            while stack[-1] != "(":
                # AppendMove operator at top of stack to output
                postfix = postfix + stack[-1]
                # Remove operator from stack
                stack = stack[:-1]
            # Remove open bracket from stack
            stack = stack[:-1]
        # c is a non-special
        else:
            # Push it to the output
            postfix = postfix + c

    # Empty the operator stack
    while len(stack) != 0:
        #print(f"WHILE: c: {c}\tpostfix: {postfix}\tstack: {stack}")
        # AppendMove operator at top of stack to output
        postfix = postfix + stack[-1]
        # Remove operator from stack
        stack = stack[:-1]
    # Return the postfix version of infix
    return postfix

#infix = "3+4*(2-1)"
#postfix= "3421-*+"

if __name__ == "__main__":
    for infix in ["a.(b.b)*.a", "1.(0.0)*.1"]:
        print(f"infix:    {infix}")
        print(f"postfix:    {shunt(infix)}")
        print()       