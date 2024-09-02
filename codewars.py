# def is_pangram(st):
#   text = st = ''.join([char for char in st if char.isalpha()]).lower()
#   lista = set(text)
  
 
#   if ' ' in lista:
#     lista.remove(' ')
  
#   print(lista)
#   if len(lista) == 26:
#     return True
#   else:
#     return False 


  
 

# print(is_pangram('Y wG s\x0cjST^ 1Sqs:SEDymZjcsoCVC!l ipPXJHE{x|A,qFtG |-N I@<wkRUb'))



# def cakes(recipe, available):
#   max_cakes = float('inf')
#   for ingirident, quantity in recipe.items():
#     if ingirident not in available:
#       print(f"you don`t have {ingirident}")
#       return max_cakes
#     if available[ingirident] < quantity:
#       print(f"Not enough {ingirident}. You need {quantity}, but you have {available[ingirident]}")
#       return max_cakes
#     num_cakes = available[ingirident] // quantity
#     if num_cakes < max_cakes:
#       max_cakes = num_cakes
#   print(f"{max_cakes}")
#   return max_cakes




# cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})

# # cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000})


# ## Narcist
# def narcissistic( value ):
#   x = list(map(int, str(value)))
#   potega = len(x)
#   y = 0
#   for i in x:
#     y = y + i**potega
#   print(potega)
#   if y == value:
#     return True
#   else:
#     return False
  

# print(narcissistic(7))

def first_non_repeating_letter(s):
  # Normalize the string to lower case for comparison
  lower_s = s.lower()

  # Create a dictionary to count occurrences of each character
  char_count = {}
  for char in lower_s:
      if char in char_count:
          char_count[char] += 1
          print(char_count)
      else:
          char_count[char] = 1
          print(char_count)

  # Find the first non-repeating character
  for index, char in enumerate(lower_s):
      if char_count[char] == 1:
          return s[index]  # Return the character in its original case

  # If no non-repeating character is found, return an empty string
  return ""

# Examples
print(first_non_repeating_letter('stress'))  # Should return 't'
print(first_non_repeating_letter('sTreSS'))  # Should return 'T'
print(first_non_repeating_letter('aabbcc'))  # Should return ''