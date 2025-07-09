def extract_digits(n):
    while n > 0:
        last_digit = n % 10
        print(last_digit)
        n = n // 10

extract_digits(5678)
