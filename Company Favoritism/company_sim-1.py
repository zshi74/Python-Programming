#name:Zicheng Shi
# function1: Create employee
def create_employee():
    """ Return a dictionary to create random employees """
    choice=[True,False]
    favored = random.choice(choice) #randomly get True or False information
    if favored == True: #according to the instructions, get different nbr
        nbr = random.randint(1,100)
        employee= {'favored':favored,'score':nbr}
        return employee
    elif favored == False:
        nbr = random.randint(0,99)
        employee= {'favored':favored,'score':nbr}
        return employee #we must return the dictionary, otherwise we cannot use it in the following functions.

# function2: Create company
def create_company(sizes):
    """ list of list, which means we need to nest the list into another lsit """
    infor=[] # This is an empty list used to store the company's information
    for char in range(len(sizes)):
        level=[] #Used to store many different employees' information, which is dictionary.
        for index in range(sizes[char]):
            new_name = create_employee()
            level.append(new_name)
        infor.append(level) #append to the outside list
    return infor

# function3: Get percent of favored employees
def get_pct_favored(company, level):
  """ Get percent of favored emplyees use simple average method """
  nbr=0 # initial number of favored emplyees in one level
  for index in range(len(company[level])): #loop through every favored emplyees
    if company[level][index]['favored'] == True:
        nbr += 1
  pct = float(nbr) / float(len(company[level]))
  return pct #return the percent so we can use it in function5

# function5: main
def main(num_simulations, sizes, pct):
  """ This main function used to get the percentage of each level after running several times """
  print 'After',num_simulations,'trials, here are the average distributions of employees:'
  print
  print '          favored non-favored'
  company = create_company(sizes)
  final_company = [[] for index2 in range(len(company))] # Creating some empty lists to store the final levels
  for index3 in range(num_simulations): #loop several times
    company = create_company(sizes)
    for level in range(len(sizes)): #there're "sizes" level in our company list
      pct = get_pct_favored(company,level)
      final_company[level].append(pct) #get percentage of each level and then append them into the final_company level
  for level in range(len(sizes)):
      favored = int(sum(final_company[level])/len(final_company[level])*100) #we have got the final_company level list and then we need to use it to get the average of each level
      un_favored = 100-favored
      print 'level',level,' | ',str(favored)+'%',' | ',str(un_favored)+'%'
