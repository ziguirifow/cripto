1. # Caesar Cipher

 2.

 3. MAX_KEY_SIZE = 26

 4.

 5. def getMode():

 6.     while True:

 7.         print('Do you wish to encrypt or decrypt a message?')

 8.         mode = input().lower()

 9.         if mode in 'encrypt e decrypt d'.split():

10.             return mode

11.         else:

12.             print('Enter either "encrypt" or "e" or "decrypt" or "d".')

13.

14. def getMessage():

15.     print('Enter your message:')

16.     return input()

17.

18. def getKey():

19.     key = 0

20.     while True:

21.         print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))

22.         key = int(input())

23.         if (key >= 1 and key <= MAX_KEY_SIZE):

24.             return key

25.

26. def getTranslatedMessage(mode, message, key):

27.     if mode[0] == 'd':

28.         key = -key

29.     translated = ''

30.

31.     for symbol in message:

32.         if symbol.isalpha():

33.             num = ord(symbol)

34.             num += key

35.

36.             if symbol.isupper():

37.                 if num > ord('Z'):

38.                     num -= 26

39.                 elif num < ord('A'):

40.                     num += 26

41.             elif symbol.islower():

42.                 if num > ord('z'):

43.                     num -= 26

44.                 elif num < ord('a'):

45.                     num += 26

46.

47.             translated += chr(num)

48.         else:

49.             translated += symbol

50.     return translated

51.

52. mode = getMode()

53. message = getMessage()

54. key = getKey()

55.

56. print('Your translated text is:')

57. print(getTranslatedMessage(mode, message, key))
