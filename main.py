allValues = ["a", "b", "c", "d", "e", "f", "g"]

def flatten(t):
    return [item for sublist in t for item in sublist]

def is_1478(text):
  text_length = len(text)
  print(f'"{text}": {text_length}')
  return text_length == 2 or text_length == 3 or text_length == 4 or text_length == 7


def remove_item_if_exists(list, item):
  while item in list: list.remove(item)

def remove_items_if_exists(list, items):
  for item in items:
    while item in list: list.remove(item)

def remove_everything_but(list, remaining):
  for item in list:
    if item not in remaining:
      list.remove(item)

def create_segment_pos_list():
    return allValues.copy()

# Set time

def split_text(word):
  return [char for char in word]

def is_strict_subset(part, whole):
  partSet = set(split_text(part))
  wholeSet = set(split_text(whole))

  # print(f'Part set: "{partSet}", whole set: "{wholeSet}".')

  return len(partSet) < len(wholeSet) and partSet.issubset(wholeSet)

def is_strict_superset(part, whole):
  return is_strict_subset(whole, part)

def count_sub_super(item, allItems):
    superCount = len(list(filter(lambda oneOfAllItems: is_strict_superset(item, oneOfAllItems), allItems)))
    subCount = len(list(filter(lambda oneOfAllItems: is_strict_subset(item, oneOfAllItems), allItems)))
    return (subCount, superCount)

def remove_options(mappingSegment, possibilities, inputPart):
  if mappingSegment in inputPart:
    text_length = len(inputPart)
    if text_length == 2:
      remove_everything_but(possibilities, ["c", "f"]) # 1
    elif text_length == 3:
      remove_everything_but(possibilities, ["a", "c", "f"]) # 7
    elif text_length == 4:
      remove_everything_but(possibilities, ["b", "c", "d", "f"]) # 4
    elif text_length == 5:
      remove_everything_but(possibilities, ["a", "b", "c", "d", "e", "f", "g"]) # 2, 3, 5
    elif text_length == 6:
      remove_everything_but(possibilities, ["a", "b", "c", "d", "e", "f", "g"]) # 0, 6, 9
    elif text_length == 7:
      remove_everything_but(possibilities, ["a", "b", "c", "d", "e", "f", "g"]) # 8

def translate_tup(tup):
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
  return options[tup]

def solve_with_super_sub(io):
  inputParts = io[0].split(" ")
  outputParts = io[1].split(" ")

  print(f'Solving super sub input: "{io[0]}", output: "{io[1]}".')

  for input in inputParts:
    countTup = count_sub_super(input, inputParts)

    print(f'Part: "{input}", count: "{countTup}, translates to: {translate_tup(countTup)}.')

def solve_io(io):
  inputParts = io[0].split(" ")
  outputParts = io[1].split(" ")

  print(f'Solving input: "{io[0]}", output: "{io[1]}".')

  possibleMappingList = [] 

  for val in allValues:
    possibleMappingList.append((val, create_segment_pos_list()))

  for possibleMappingItem in possibleMappingList:
    for inputPart in inputParts:
      mappingSegment = possibleMappingItem[0]
      possibilities = possibleMappingItem[1]
    
      remove_options(mappingSegment, possibilities, inputPart)

#  for possibleMappingItem in possibleMappingList:
#    possibilities = possibleMappingItem[1]
#    if len(possibilities) == 2:
#      for posMapItem in possibleMappingList:
#        posses = posMapItem[1]
#        if len(posses) > 2:
#          remove_items_if_exists(posses, possibilities)

  
  print(f'Finished analyzing "{io[0]}".')
  for possibleMappingItem in possibleMappingList:
    mappingSegment = possibleMappingItem[0]
    possibilities = possibleMappingItem[1]

    print(f'Segment "{mappingSegment}" can map to {possibilities}.')

      




lines = open("Input.txt",'r').read().splitlines()
print(f'Lines count {len(lines)}.')

inAndOutPuts = list(map(lambda t: t.split(" | "), lines))

# for inAndOutput in inAndOutPuts:
#  print(f'{inAndOutput[0]} ==> {inAndOutput[1]}')

for inAndOutput in inAndOutPuts:
  solve_with_super_sub(inAndOutput)
  print()

# for io in inAndOutPuts:
#     solve_io(io)

# outputWords = list(map(lambda t: t.split(" "), outputParts))
# all_words = flatten(outputWords)
# filtered = list(filter(is_1478, all_words))
# print(f'Filtered count {len(filtered)}.')
