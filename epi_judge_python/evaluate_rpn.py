from test_framework import generic_test


def evaluate(expression: str) -> int:
    operand_stack: list[int] = []
    operator_map = {'+': lambda y, x: x + y,
                    '-': lambda y, x: x - y,
                    '/': lambda y, x: x // y,
                    '*': lambda y, x: x * y
                    }
    for token in expression.split(','):
        if token in operator_map:
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            result = operator_map[token](op1, op2)
            operand_stack.append(result)
        else:
            operand_stack.append(int(token))

    return operand_stack[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
