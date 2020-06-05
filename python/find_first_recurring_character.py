# string = 'ABCA' ; returns A
# string = 'ABCBAD' returns B
# string = 'ABC' returns "NIL"


# Strategy: Use a dictionary to store numbers, keep checking the count.


def return_rec_char(input_string):
    char_count = dict()
    for i in input_string:
      if i not in char_count.keys():
        char_count.update({i: 1})
      else:
        print('Found the recurring char %s' %i)
        return i


def main():

  string = 'ABCDB'

  a = return_rec_char(string)

  print a


if __name__=="__main__":
   main()
