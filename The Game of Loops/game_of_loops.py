def has_unique_letters(pw_1):
    count1=0
    while count1 < len(pw_1):
      count2=count1+1
      while count2 < len(pw_1):
        if pw_1[count1].upper() != pw_1[count2].upper():
          count2=count2+1
        elif pw_1[count1].isdigit()==True:
          return True
        else:
          return False
      count1=count1+1
    return True

def has_even_vowels(pw_2):
  pw_2=pw_2.upper()
  number_of_vowel=pw_2.count("A")+pw_2.count("E")+ pw_2.count("I")+pw_2.count("O")+pw_2.count("U")
  if number_of_vowel%2 == 0:
    return True
  else:
    return False

def has_special_character(pw_3):
  count3=0
  while count3 < len(pw_3):
    if pw_3[count3]=="@" or pw_3[count3]=="#" or pw_3[count3]=="*" or pw_3[count3]=="$":
      return True
    count3=count3+1
  return False

def has_divisible_numbers(pw_4):
  count4=0
  while count4 < len(pw_4):
    if pw_4[count4].isdigit()==True:
      if not(int(pw_4[count4]) % 2 == 0 or int(pw_4[count4]) % 3 == 0):
        return False
    count4=count4+1
  return True

def check_password(pw_5):
  if has_unique_letters(pw_5)==True and has_even_vowels(pw_5)==True and has_special_character(pw_5)==True and has_divisible_numbers(pw_5)==True:
    print "Congratulations, your password meets our criteria."
  else:
    if has_unique_letters(pw_5)==False:
      print "Warning! Please ensure letters are not repeated."
    if has_even_vowels(pw_5)==False:
      print "Warning! Please ensure password contains an even number of vowels."
    if has_special_character(pw_5)==False:
      print "Warning! Please ensure password contains at least one of {@, #, *, $}."
    if has_divisible_numbers(pw_5)==False:
      print "Warning! Please ensure all numbers are divisible by 2 or 3."
    print "Sorry, your password does not meet our criteria."
    
if __name__ == "__main__":
  pw_5=raw_input("Welcome to the Iron Bank of Braavos. Please set your password:")
  check_password(pw_5) 
  
