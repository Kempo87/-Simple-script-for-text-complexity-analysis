text = input("Podaj tekst artykułu:")

characters = len(text)

words = len(text.split())

average_word_lenght = (characters - words) / words 

print ("Słowa w Twoim tekście mają średnio", average_word_lenght, "znaków")