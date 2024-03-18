# Expert-system-based-on-fuzzy-inference
System oceny preferencji kulinarnej z wykorzystaniem logiki rozmytej


<p align="center">
   <img src="https://img.shields.io/badge/Engine-PyCharm%2023-B7F352" alt="Engine">
</p>

## About


Projekt polegał na stworzeniu funkcjonalnego systemu ekspertowego opartego na wnioskowaniu rozmytym w języku Python. W celu osiągnięcia tego zadania przeprowadzono szereg kroków, które obejmowały definiowanie zbioru reguł, tworzenie zestawu danych z funkcjami przynależności rozmytej, implementację algorytmów wnioskowania rozmytego, opracowanie interfejsu użytkownika, testowanie i ewaluację systemu oraz optymalizację.
</br>

## Documentation

### Libraries
- `NumPy`, `skfuzzy`,`matplotlib`

### Zdefiniowanie zbióru reguł
- Reguły oceny przydatności potraw mogą obejmować kombinacje różnych cech rozmytych, na przykład: "Jeśli smak jest bardzo dobry, a pikantność jest umiarkowana, to potrawa jest uważana za bardzo przydatną".
### Zdefiniowanie zbióru danych
- Stworzenie zestawu danych obejmującego cechy rozmyte potraw, takie jak smak, pikantność, konsystencja i słodycz. Możemy zdefiniować te cechy za pomocą funkcji przynależności rozmytej, takich jak trójkątne, trapezoidalne lub gaussowskie.
### Implementacja wnioskowania rozmytego:
- Wykorzystanie zdefiniowanych reguł i danych wejściowych do oceny przydatności potraw. Możemy zaimplementować mechanizmy wnioskowania rozmytego, takie jak Minimum lub Maximum, aby uzyskać ocenę.
### Przygotowanie interfejsu użytkownika
- Stworzenie prostego interfejsu użytkownika, który umożliwi użytkownikowi podanie cech rozmytych potrawy. System powinien obliczyć ocenę przydatności potrawy na podstawie wprowadzonych danych.
### Testowanie i ewaluacja: 
- Przetestowanie systemu poprzez wprowadzenie różnych kombinacji cech rozmytych potraw i sprawdzenie, czy ocena przydatności jest zgodna z oczekiwaniami na podstawie zdefiniowanych reguł.
### Optymalizacja:
- Eksperymentowanie z różnymi regułami, funkcjami przynależności i algorytmami wnioskowania w celu poprawy wydajności i trafności systemu.
## Developers

- Danyil Muzychenko (https://github.com/DanyilMuzychenko)
