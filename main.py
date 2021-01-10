alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceaser(text2, p_shift,d1):
  end_text = ""
  if d1 == "decode":
      p_shift *= -1
  for letter in text2: 
    position = alphabet.index(letter)
    n_position = position + p_shift
    end_text  += alphabet[n_position]
  print(f"The {d1}d text is {end_text}")
      

ceaser(text2 = text, p_shift = shift, d1 = direction)
