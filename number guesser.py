print 'please think of a number between 0  and 100!'

x = 100
numguesses = 0
low = 0
high = x
AI = False

while not AI:
          ans = (high + low)/2
          print ('Is your secret number ' +str(ans)+ ' ??') 
          input = raw_input("Enter 'h' if it's too high, 'l' if it's too low, 'c if it's corret'")
          numguesses += 1
          

          if input == 'h':
             high = ans
          elif input == 'l':
             low = ans
          elif input == 'c':
              AI = True
          else:
              print('error')

print('I got you ' + str(ans) + ' with ' +str(numguesses) + ' times')



