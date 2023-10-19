# Nazwa programu: Obliczanie średniej długości słów

## Opis: Ten program umożliwia użytkownikowi wprowadzenie tekstu artykułu, a następnie oblicza średnią długość słów w tym tekście. Program liczy liczbę znaków, liczbę słów oraz oblicza średnią długość słów na podstawie tych danych.

### Instrukcje użytkowania:

Uruchom program.
Program poprosi użytkownika o podanie tekstu artykułu. Wprowadź tekst i naciśnij Enter.
Program przetworzy podany tekst i obliczy średnią długość słów w tekście.
Wynik zostanie wyświetlony na ekranie w formie komunikatu.

#### Działanie programu:

Program wczytuje tekst od użytkownika za pomocą funkcji input i zapisuje go w zmiennej text.
Następnie program oblicza liczbę wszystkich znaków w tekście i zapisuje ją w zmiennej characters.
Program oblicza liczbę słów w tekście, dzieląc tekst na części przy użyciu spacji za pomocą funkcji split() i zliczając je. Liczbę słów zapisuje w zmiennej words.
Oblicza średnią długość słów, odejmując od liczby znaków liczbę słów (co odpowiada liczbie spacji między słowami) i dzieląc to przez liczbę słów. Wynik zapisuje w zmiennej average_word_length.
Na koniec program wyświetla wynik w formie komunikatu, wskazując, ile średnio znaków ma słowo w podanym tekście artykułu.
Ten program jest przykładem prostej analizy tekstu i może być używany do obliczenia średniej długości słów w różnych artykułach lub tekstach.