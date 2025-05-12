def verify_card_number(card_number):
    # You can put card validation logic here if needed
    print("Verified card number:", card_number)

def main():
    card_number = '411-111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    print("Clean card number:", translated_card_number)
    
    verify_card_number(translated_card_number)

main()
