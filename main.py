PUNCTUATIONS = ',.!?%'

def remove_punctuation(text):
    for punc in PUNCTUATIONS:
        text = text.replace(punc, ' ')
    return text

def compute_average_length(text):
    '''Returns average word length (excluding numbers). Raises ZeroDivisionError if there are no words.'''
    words = remove_punctuation(text).split()
    without_numbers = [w for w in words if not w.isnumeric()] # Można też użyć w.isalpha(), wtedy warunek jest mocniejszy
    if not without_numbers:
        raise ZeroDivisionError("No words in the text")
    lengths = [len(w) for w in without_numbers]
    average = sum(lengths) / len(lengths) # Tutaj może pojawić się ZeroDivisionError.
    return average

def main():
    text = input('Podaj tekst: ')
    average = compute_average_length(text)
    print(f'Średnia długość słowa: {average:.2f}')

if __name__ == "__main__":
    main()
