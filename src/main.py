#Excercise 1

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False


# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True,
# then return True only if both are negative.

def pos_neg(a, b, negative):
  if negative:
    if a < 0 and b < 0:
      return True
    elif a > 0 or b > 0:
      return False

  if not negative:
    if a < 0 and b < 0:
      return False
    if a < 0 or b < 0:
      return True
    else:
      return False

def not_string(str):
  if str.startswith('not'):
    return str
  else:
    return 'not ' + str



#Given a non-empty string and an int n, return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string
# (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
  return str[:n] + str[n + 1:]
# str[:n] the column indicates that we take everythin unil the index we specify. n doesn't count
# so if n = 1, in "Kitten" we would only take the k
# str [n+1] we take the rest of the word from the index we specified.
# like this we form the word "Ktten"


# Given an "out" string length 4, such as "<<>>",
# and a word, return a new string where the word
# is in the middle of the out string, e.g. "<<word>>".

def make_out_word(out, word):
  return out[:2] + word +out[2:]



# Given a string, return a new string made of 3 copies
# of the last 2 chars of the original string.
# The string length will be at least 2.
# Ex: "Hello" => "lololo"

def extra_end(str):
  end = str[len(str) -2:]
  return end * 3


