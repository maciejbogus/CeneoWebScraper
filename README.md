# CeneoWebScraper

|SKLADOWA|SELEKTOR|NAZWA ZMIENNEJ|TYP ZMIENNEJ|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|opinion|obj
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id|str
|autor opinii|span.user-post__author-name|author|str
|rekomendacja|span.user-post__author-recomendation > em|recomendation|str
|liczba gwiazdek|span.user-post__score-count|stars|string
|tresc opinii|div.user-post__text|content|str
|lista zalet|div[class?="positives"]~ div.review-feature__item|pros|list
|lista wad|div[class?="negatives"]~ div.review-feature__item|cons|list
|dla ilu osob przydatna|span[id^="votes-yes"]|usefull|int
|dla ilu osob nieprzydatna|span[id^="votes-no"]|useless|int
|data wystawienia opinii|user-post__published > time:nth-child(1)["datetime"]|publish_date|date
|data zakupu|user-post__published > time:nth-child(1)["datetime"]|purchase_date|date

## ETAPY PRACY

1. Pobieranie pojedynczych zmiennych skladowych danej opinii
2. Zapisanie wszystkich skladowych danej opinii do slownika
3. Pobranie wszystkich opinii o danym produkcie
4. Zapisanie wzystkich opinii do pliku .json
5. Zaktualizowanie kodu o mozliwosc wskazania konkretnego produktu przez uzytkownika
6. Optymalizacja kodu:
    a. Utworzenie funkcji do ekstrakcji elementow skladowych
    b. Utworzenie slownika selektorow
    c. Uzycie dictionary comprehension do pobrania skladowych opjedynczej opinii na podstawie slownika selektorow
7. Stworzenie witryny interentowej z odpowiednimi podstronami i hosting za pomoca Flask
8. Dodanie systemu analizy pobranych danych:
    a. Wyliczenie dancyh statystycznych
    b. Kod tworzacy grafy na podstawie wygenerowanych danych
    c. Zapisanie statystyk do plikow .json i grafow do plikow .png
9. Wyswietlenie statystyk i grafow na stronie w odpowiednich podstronach

## BIBLIOTEKI

bs4 - pakiet do analizowania dokumentow HTML i XML
flask - mikro framework aplikacji webowych napisany w jezyku Python
requests - biblioteka HTTP dla jezyka programowania Python. Celem projektu jest uczynienie zadan HTTP prostszymi i bardziej przyjaznymi dla czlowieka.
pandas - biblioteka do manipulacji i analizy danych
numpy - Obsluga tabel struktury danych i operacje sluzace do manipulowania tabelami liczbowymi i szeregami czasowymi
json - obsluga plikow z rozszerzeniem .json
matplotlib - biblioteka do tworzenia wykresow dla jezyka programowania Python
markdown - praser do jezyka markdown