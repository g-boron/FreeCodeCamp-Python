def arithmetic_arranger(problems, display = False):
    if len(problems) > 5:
      return 'Error: Too many problems.'
      
    for x in problems:
      tmp = x.split()
  
      if tmp[1] in ['/', '*']:
          return "Error: Operator must be '+' or '-'."
      elif not tmp[0].isnumeric() or not tmp[2].isnumeric():
          return 'Error: Numbers must only contain digits.'
      elif len(tmp[0]) > 4 or len(tmp[2]) > 4:
          return 'Error: Numbers cannot be more than four digits.'

    first = []
    operand = []
    second = []
    distances = []
    arranged_problems = ''
    for x in problems:
        tmp = x.split()
        first.append(tmp[0])
        operand.append(tmp[1])
        second.append(tmp[2])
        if len(tmp[0]) > len(tmp[2]):
            distance = len(tmp[0]) + 2
            distances.append(distance)
        elif len(tmp[0]) == len(tmp[2]):
            distance = len(tmp[0]) + 2
            distances.append(distance)
        else:
            distance = len(tmp[2]) + 2
            distances.append(distance)
    
    for i, _ in enumerate(first):
        arranged_problems += (distances[i] - len(first[i])) * ' ' + first[i] + '    '
    else:
        arranged_problems = arranged_problems[:-4]
        arranged_problems += '\n'
    
    
    for i, _ in enumerate(operand):
        arranged_problems += operand[i] + (distances[i] - len(second[i]) - 1)  * ' ' + second[i] + '    '
    else:
        arranged_problems = arranged_problems[:-4]
        arranged_problems += '\n'
    
    for i, _ in enumerate(distances):
        arranged_problems += distances[i] * '-' + '    '
    else:
        arranged_problems = arranged_problems[:-4]
        
        if display:
            arranged_problems += '\n'
            solutions = []
            for i, _ in enumerate(first):
                if operand[i] == '+':
                    solutions.append(int(first[i]) + int(second[i]))
                else:
                    solutions.append(int(first[i]) - int(second[i]))
    
            for i, _ in enumerate(solutions):
                arranged_problems += (distances[i] - len(str(solutions[i]))) * ' ' + str(solutions[i]) + '    '
            else:
                arranged_problems = arranged_problems[:-4]
        
    return arranged_problems