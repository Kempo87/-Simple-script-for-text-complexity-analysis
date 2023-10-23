# Opis programu:

Program przetwarza tekst wprowadzony przez użytkownika i oblicza średnią długość słów, wyłączając liczby. Oto kluczowe elementy programu:

PUNCTUATIONS: To ciąg znaków zawierający zestaw znaków interpunkcyjnych, które zostaną usunięte z tekstu podczas przetwarzania. Obejmuje to przecinek, kropkę, znak zapytania, znak wykrzyknika i znak procenta.

remove_punctuation(text): Ta funkcja przyjmuje tekst wejściowy i usuwa określone znaki interpunkcyjne przy użyciu pętli. Zwraca ona tekst, w którym znaki interpunkcyjne zostały zamienione na spacje.

compute_average_length(text): Ta funkcja oblicza średnią długość słowa (wyłączając liczby) w podanym tekście. Najpierw wywołuje funkcję remove_punctuation(), aby usunąć znaki interpunkcyjne, a następnie dzieli tekst na słowa. Wyklucza słowa zawierające cyfry z obliczeń i zgłasza wyjątek ZeroDivisionError, jeśli w tekście nie ma żadnych słów. Funkcja oblicza średnią długość słów i zwraca ją.

main(): Główna funkcja programu. Pobiera od użytkownika tekst, wywołuje funkcję compute_average_length() do obliczenia średniej długości słów, a następnie wyświetla wynik z dwoma miejscami po przecinku.

## Program umożliwia użytkownikowi wprowadzenie tekstu, przetwarza go, usuwając określone znaki interpunkcyjne, a następnie oblicza i wyświetla średnią długość słów. Program zawiera również obsługę błędów, aby radzić sobie z przypadkami, w których w tekście nie ma żadnych słów, co zapobiega jego awarii.
