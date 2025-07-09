def palindrome(n):
    num = n 
    opp = 0
    while n > 0:
        last_Digit = n % 10
        opp = (opp * 10) + last_Digit
        n = n // 10

    if num == opp:
        print("Palindrome", opp)
    else:
        print("Not a Palindrome" , opp)

palindrome(1221)