# home-made encryption algorithm
standard = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
val = 0
keyval = 0
while True:
  choice = input("ENCRYPT or DECRYPT")
  if choice == "ENCRYPT":
    msg = input("What is your message?") #not to be confused with Monosodium glutamate
    
    key = input("What key")
    
    res = [char for char in msg]
    keyres = [char2 for char2 in key]
    output = []
    for char in res:
      val = standard.index(char)
      
      keyval = standard.index(char2)
      
      encryptval = val + keyval + 1
      if encryptval >= 37:
        encryptval -= 37
      #print(encryptval)
      
      encryptchar = standard[encryptval]
      
      output.append(str(encryptchar))
      #print(val + keyval)
    print(''.join(output))
  elif choice == "DECRYPT":
    
    msg = input("What is the encrypted code?")
    key = input("What is your key?")
    
    res = [char for char in msg]
    keyres = [char2 for char2 in key]
    output = []
    for char in res:
      val = standard.index(char)
      
      keyval = standard.index(char2)
      
      encryptval = val - keyval - 1
      if encryptval < 0:
        encryptval += 37
      #print(encryptval)
      
      encryptchar = standard[encryptval]
      
      output.append(str(encryptchar))
      #print(val + keyval)
    print(''.join(output))
    
    
