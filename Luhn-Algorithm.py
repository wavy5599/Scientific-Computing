# Function to verify a credit card number using the Luhn algorithm
def verify_card_number(card_number):
    sum_of_odd_digits = 0

    # Reverse the card number string so we can process it from right to left
    card_number_reversed = card_number[::-1]

    # Take every other digit starting from index 0 (i.e., the actual last digit)
    odd_digits = card_number_reversed[::2]

    # Add those odd-position digits directly to the sum
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0

    # Now take the digits in the even positions (starting from index 1)
    even_digits = card_number_reversed[1::2]

    for digit in even_digits:
        number = int(digit) * 2  # Double the digit

        # If the result is two digits, split and sum the digits
        if number >= 10:
            number = (number // 10) + (number % 10)  # e.g., 16 → 1 + 6 = 7

        # Add the result to the even sum
        sum_of_even_digits += number

    # Combine both sums
    total = sum_of_odd_digits + sum_of_even_digits

    # If total is divisible by 10, the card number is valid
    return total % 10 == 0


# Main function to handle input and call the verification function
def main():
    card_number = '4111-1111-4555-1142'  # Original card number with dashes

    # Remove dashes and spaces from the input
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Run the verification function and print result
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Run the main function
main()
