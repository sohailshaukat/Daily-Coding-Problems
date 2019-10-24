#! python3

brackets = "([])[]({})"
is_opening_bracket = {'(': True, '{': True, '[': True,
                      ']': '[', '}': '{', ')': '('
                      }


def balancedBrackets(brackets):
    bracket_stack = []
    for bracket in brackets:
        if is_opening_bracket[bracket] == True:
            bracket_stack.append(bracket)
        else:
            if bracket_stack[-1] == is_opening_bracket[bracket]:
                del bracket_stack[-1]
            else:
                return False
    return bracket_stack == []


print(balancedBrackets(brackets))
