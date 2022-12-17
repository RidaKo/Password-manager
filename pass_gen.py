#Password Generator Project
import random

def create_password_list(characters: str,  char_range: tuple) -> list:
  password_list = [random.choice(characters) for _ in char_range]
  return password_list

def make_pass() -> list:
    
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []



  password_letter_list = create_password_list(letters, range(nr_letters))
  password_symbol_list = create_password_list(symbols, range(nr_symbols))
  password_nr_list = create_password_list(numbers, range(nr_numbers))

  password_list = password_letter_list+ password_symbol_list + password_nr_list
  random.shuffle(password_list)

  
  password = "".join(password_list)

  return password
