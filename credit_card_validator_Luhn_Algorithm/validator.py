# Sample card: 5610591081018250
def is_valid_card(card_no):
    
    if not card_no:
        return "Card number cannot be empty"

    card_no = card_no.replace(" ", "").replace("-", "")

    if not card_no.isdigit():
        return "Card number must contain only digits"

    if not 13 <= len(card_no) <= 19:
        return "Invalid card length"
    

    total = 0

    for idx, digit in enumerate(card_no):
        n = int(digit)

        if idx % 2 == 0:      # double digits at even index
            n *= 2
            if n > 9:
                n -= 9

        total += n

    return "This card is valid" if total % 10 == 0 else "This card is invalid"


card_no = input("Enter the card number: ")
print(is_valid_card(card_no))
