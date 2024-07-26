def caesar_cipher(text, shift, mode):
  """Encrypts or decrypts text using Caesar cipher algorithm.

  Args:
      text: The text to encrypt or decrypt.
      shift: The number of positions to shift letters by.
      mode: 'encrypt' or 'decrypt' to specify the operation.

  Returns:
      The encrypted or decrypted text.
  """
  result = ""
  for char in text:
    if char.isalpha():
      # Convert character to uppercase for easier handling
      char = char.upper()
      # Get the character code (ASCII value)
      char_code = ord(char)
      # Perform the shift based on mode
      new_code = char_code + shift if mode == 'encrypt' else char_code - shift
      # Handle wrapping around the alphabet
      new_code = (new_code - 65) % 26 + 65 if char.isupper() else (new_code - 97) % 26 + 97
      # Convert back to character
      new_char = chr(new_code)
      result += new_char
    else:
      # Keep non-alphabetic characters unchanged
      result += char
  return result

# Get user input
message = input("Enter your message: ")
shift = int(input("Enter shift value (1-25): "))
mode = input("Enter 'encrypt' or 'decrypt': ").lower()

# Check for valid shift value
if shift < 1 or shift > 25:
  print("Invalid shift value. Please enter a value between 1 and 25.")
  exit()

# Check for valid mode
if mode not in ('encrypt', 'decrypt'):
  print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
  exit()

# Perform encryption or decryption
result = caesar_cipher(message, shift, mode)

# Print the result
print(f"{mode.title()}d message: {result}")
