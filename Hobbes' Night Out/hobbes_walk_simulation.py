import random

# function1

def run_simulation():
    """ The whole function calls the below three other functions
        and use two loops to test the current_position of Hobbes
    """
    input_number = int(raw_input("Enter random seed value:"))
    random.seed(input_number)
    num_drinks = int(raw_input("How many shots did Hobbes take?"))
    distance = int(raw_input("How far is it to Hobbes' home?"))
    hole_position = random.randint(1,distance-1)
    print "Hole position is", hole_position
    print "Level is", get_level(num_drinks)
    drunk_level = get_level(num_drinks)
    walking = get_walk(drunk_level)
    print "Step length is", walking[0]
    print "Step pattern is",walking[1],"forward and", walking[2],"backward"
    step_length = walking[0]
    current_position = 0
    count2 = []
    count2.append(current_position)
    while current_position < distance and current_position != hole_position:
      index1 = 0
      while index1 < walking[1]:
        step_direction = 1
        current_position = update(current_position,step_direction,step_length)
        count2.append(current_position)
        index1 += 1
      index2 = 0
      while index2 < walking[2]:
        step_direction = -1
        current_position = update(current_position,step_direction,step_length)
        count2.append(current_position)
        index2 += 1
    if hole_position in count2:
        print "Oh no! Hobbes fell near the bar!"
    else:
      print "Hurray! Hobbes makes it through the day!"
    return count2



# function2

def get_level(num_drinks):
  """ use if statements to get Hobbes' drunk level """
  if 0 <= num_drinks <= 2:
      drunk_level = 0
      return drunk_level
  if 3 <= num_drinks <= 5:
      drunk_level = 1
      return drunk_level
  if 6 <= num_drinks <= 8:
      drunk_level = 2
      return drunk_level
  if 9 <= num_drinks <= 11:
      drunk_level = 3
      return drunk_level
  if num_drinks >= 12:
      drunk_level = 4
      return drunk_level


# function3

def get_walk(drunk_level):
  """ get Hobbes' walk patterns, then append them to
      my counts as a list
  """
  counts=[]
  step_length = random.randint(1,5-drunk_level)
  counts.append(step_length)
  forward = random.randint(4,6)
  counts.append(forward)
  backward = forward- random.randint(1,3)
  counts.append(backward)
  return counts


# function4

def update(current_position, step_direction, step_length):
    """ return Hobbes' current position according to
        Hobbes' walking patterns
    """
    current_position = current_position + step_direction * step_length
    return current_position

if __name__ == "__main__":
    run_simulation()