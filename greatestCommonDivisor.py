def gcdRecur(a,b):



      if b == 0:
          return a

      return gcdRecur(b, a%b)


print gcdRecur(4,46)

