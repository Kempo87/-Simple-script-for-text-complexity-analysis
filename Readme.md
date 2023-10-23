# Opis programu:

Program przetwarza tekst wprowadzony przez użytkownika i oblicza średnią długość słów, wyłączając liczby. Oto kluczowe elementy programu:

PUNCTUATIONS: To ciąg znaków zawierający zestaw znaków interpunkcyjnych, które zostaną usunięte z tekstu podczas przetwarzania. Obejmuje to przecinek, kropkę, znak zapytania, znak wykrzyknika i znak procenta.

remove_punctuation(text): Ta funkcja przyjmuje tekst wejściowy i usuwa określone znaki interpunkcyjne przy użyciu pętli. Zwraca ona tekst, w którym znaki interpunkcyjne zostały zamienione na spacje.

compute_average_length(text): Ta funkcja oblicza średnią długość słowa (wyłączając liczby) w podanym tekście. Najpierw wywołuje funkcję remove_punctuation(), aby usunąć znaki interpunkcyjne, a następnie dzieli tekst na słowa. Wyklucza słowa zawierające cyfry z obliczeń i zgłasza wyjątek ZeroDivisionError, jeśli w tekście nie ma żadnych słów. Funkcja oblicza średnią długość słów i zwraca ją.

main(): Główna funkcja programu. Pobiera od użytkownika tekst, wywołuje funkcję compute_average_length() do obliczenia średniej długości słów, a następnie wyświetla wynik z dwoma miejscami po przecinku.

## Program umożliwia użytkownikowi wprowadzenie tekstu, przetwarza go, usuwając określone znaki interpunkcyjne, a następnie oblicza i wyświetla średnią długość słów. Program zawiera również obsługę błędów, aby radzić sobie z przypadkami, w których w tekście nie ma żadnych słów, co zapobiega jego awarii.

### testy automatyczne: 

test_spaces(): Testuje, czy funkcja compute_average_length() poprawnie oblicza średnią długość słów w tekście, który zawiera spacje między słowami. Oczekiwana średnia wynosi 3.0, co jest równoważne średniej długości słów "one" (3 liter) i "two" (3 litery).

test_punctuation(): Testuje, czy funkcja poprawnie radzi sobie z tekstem zawierającym znaki interpunkcyjne. Oczekiwana średnia wynosi 3.0, ponieważ znaki interpunkcyjne ("." w tym przypadku) są usuwane, a tekst jest traktowany tak, jakby zawierał tylko dwa słowa: "one" i "two".

test_numbers(): Sprawdza, czy funkcja radzi sobie z tekstem, który zawiera zarówno litery, jak i liczby. Oczekiwana średnia wynosi 3.0, ponieważ liczby nie są uwzględniane w obliczeniach średniej długości słów.

test_nicknames(): Testuje, czy funkcja uwzględnia długość słów, które zawierają liczby wewnątrz słowa. Oczekiwana średnia wynosi 4.5, ponieważ średnia długość słów "one" (3 litery) i "two123" (6 liter) wynosi 4.5.

test_multiple(): Sprawdza, czy funkcja poprawnie oblicza średnią długość w tekście, który zawiera wiele słów o takiej samej długości. Oczekiwana średnia wynosi 10.0, ponieważ wszystkie słowa w tekście ("aaaaaaaaaa") mają 10 liter.

test_nothing(): Testuje zachowanie funkcji, gdy podany tekst jest pusty. Oczekiwana średnia wynosi 0.0, ponieważ nie ma żadnych słów do obliczenia średniej długości.

Te testy mają na celu sprawdzenie, czy funkcja compute_average_length() zachowuje się zgodnie z oczekiwaniami w różnych sytuacjach, takich jak obecność spacji, znaków interpunkcyjnych, liczb, skomplikowanych słów i pustego tekstu.
