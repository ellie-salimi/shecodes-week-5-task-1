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
    for multiply_counter, num in enumerate(isbn_10,-10):
        if num.isnumeric():
            num = int(num)
            sum += (num*(-multiply_counter))
        else:
            print ('This is an invalid number')
    #check if isbn10 is correct
    if sum % 11 == 10 or sum % 11 == 0:
        return('This is a valid isbn10 barcode.')
    else:
        return('This is an invalid isbn10 barcode.')

print(validate_isbn10_barcode_check_digit('1888799978'))
print(validate_isbn10_barcode_check_digit('188879997X'))
