def isPalindrome(s):

    def toChar(s):
        s =  s.lower()
        ana = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ana = ana + c
        return ana

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChar(s))
