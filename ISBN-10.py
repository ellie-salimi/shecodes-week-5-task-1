def calculate_isbn10_barcode_check_digit(isbn_10):
    sum = 0
    #Multiply
    for multiply_counter, num in enumerate(isbn_10,-10):
        num = int(num)
        sum += (num*(-multiply_counter))
    #Calculate the remainder of the sum when divided by 11.
    check_digit = 11 - (sum % 11)
    if check_digit == 10:
        check_digit ='X'
        return(check_digit)
    else:
        return(check_digit)


def validate_isbn10_barcode_check_digit(isbn_10):

    sum = 0
    isbn_new = list(isbn_10)
    if isbn_new[9] == 'X':
        isbn_new[9] = '0'
    for position, digit in enumerate(isbn_new):
        num_digit = int(digit)
        # multiply first digit by 10, second by 9..etc
        sum += (num_digit*(len(isbn_10)-position))
    # formula to check if isbn10 is correct
    if sum % 11 == 10 or sum % 11 == 0:
        return('This is a valid isbn10 barcode.')
    else:
        return('This is an invalid isbn10 barcode.')

# print(validate_isbn10_barcode_check_digit('188879997X'))