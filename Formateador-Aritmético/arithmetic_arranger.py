def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ["", "", ""]
    for problem in problems:
        parts = problem.split()
        operand1, operator, operand2 = parts[0], parts[1], parts[2]

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_length = max(len(operand1), len(operand2)) + 2  
        arranged_problems[0] += operand1.rjust(max_length)
        arranged_problems[1] += operator + operand2.rjust(max_length - 1)
        arranged_problems[2] += '-' * max_length

        if show_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            arranged_problems.append(answer.rjust(max_length))

        if problem != problems[-1]:
            arranged_problems[0] += '    '
            arranged_problems[1] += '    '
            arranged_problems[2] += '    '

    return '\n'.join(arranged_problems)