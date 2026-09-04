
password = input("Insert your password:")

lenght = len(password)
words = password.split('@')

if len(words) > 1:
  left = words[0].isalnum()
  right = words[1].isalnum()
else:
    left = False;
    right = False;

if lenght>= 8 and leen(words) == 2 and left == True and right == True:
    print("your password is strong!")
else:
    printf("your password is not strong!")    