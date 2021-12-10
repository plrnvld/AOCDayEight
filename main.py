def split_text(word):
  return [char for char in word]

def is_strict_subset(part, whole):
  partSet = set(split_text(part))
  wholeSet = set(split_text(whole))

  return len(partSet) < len(wholeSet) and partSet.issubset(wholeSet)

def is_strict_superset(part, whole):
  return is_strict_subset(whole, part)

def are_equal_as_set(part1, part2):
    return set(part1) == set(part2)

def count_sub_super(pattern, allPatterns):
    superCount = len(list(filter(lambda item: is_strict_superset(pattern, item), allPatterns)))
    subCount = len(list(filter(lambda item: is_strict_subset(pattern, item), allPatterns)))
    return (subCount, superCount)

def translate_super_and_sub_count(superSubCount):
  options = {
    (0,9) : 8,
    (1, 5) : 9,
    (1, 1) : 6,
    (1, 2) : 0,
    (1, 0) : 2,
    (3, 0) : 5,
    (2, 2) : 3,
    (2, 1) : 4,
    (4, 1) : 7,
    (6, 0) : 1 }
  return options[superSubCount]

def solve_with_super_sub(io):
  inputParts = io[0].split(" ")
  outputParts = io[1].split(" ")

  patternMapping = []
  
  for input in inputParts:
    countTup = count_sub_super(input, inputParts)
    patternMapping.append((set(input), translate_super_and_sub_count(countTup)))
  
  def output_to_digit(output):
    for mapping in patternMapping:
      if mapping[0] == set(output):
        return mapping[1]

  print(f'Solving output "{io[1]}".')

  number = 0
  multipleOfTen = 1
  
  for output in reversed(outputParts):
    res = output_to_digit(output)
    print(f'  Output {output} = {res} * {multipleOfTen}')
    number += res * multipleOfTen
    multipleOfTen *= 10

  print(f'Number = {number}')
  print()

  return number


lines = open("Input.txt",'r').read().splitlines()
print(f'Lines count {len(lines)}.')

inAndOutPuts = list(map(lambda t: t.split(" | "), lines))

total = 0
for inAndOutput in inAndOutPuts:
  total += solve_with_super_sub(inAndOutput)

print(f"Total {total}")
