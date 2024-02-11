import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definicja zmiennych lingwistycznych
smak = ctrl.Antecedent(np.arange(0, 11, 1), 'smak')
pikantnosc = ctrl.Antecedent(np.arange(0, 11, 1), 'pikantnosc')
konsystencja = ctrl.Antecedent(np.arange(0, 11, 1), 'konsystencja')
slodycz = ctrl.Antecedent(np.arange(0, 11, 1), 'slodycz')
przydatnosc = ctrl.Consequent(np.arange(0, 11, 1), 'przydatnosc')

# definicja funkcje przynależności dla każdej zmiennej

smak['bardzo_niesmaczne'] = fuzz.trimf(smak.universe, [0, 2, 8])
smak['niesmaczne'] = fuzz.trimf(smak.universe, [2, 8, 10])
smak['przecietny_smak'] = fuzz.trimf(smak.universe, [4, 6, 8])
smak['smaczne'] = fuzz.trimf(smak.universe, [6, 8, 10])
smak['bardzo_smaczne'] = fuzz.trimf(smak.universe, [8, 10, 10])

pikantnosc['niska'] = fuzz.trimf(pikantnosc.universe, [0, 0, 4])
pikantnosc['bardzo_lagodne'] = fuzz.trimf(pikantnosc.universe, [0, 2, 8])
pikantnosc['lagodne'] = fuzz.trimf(pikantnosc.universe, [2, 8, 10])
pikantnosc['umiarkowane'] = fuzz.trimf(pikantnosc.universe, [4, 6, 8])
pikantnosc['ostra'] = fuzz.trimf(pikantnosc.universe, [6, 8, 10])
pikantnosc['bardzo_ostra'] = fuzz.trimf(pikantnosc.universe, [8, 10, 10])

konsystencja['bardzo_plynna'] = fuzz.trimf(konsystencja.universe, [0, 0, 4])
konsystencja['plynna'] = fuzz.trimf(konsystencja.universe, [0, 4, 6])
konsystencja['srednio_gesta'] = fuzz.trimf(konsystencja.universe, [4, 6, 8])
konsystencja['gesta'] = fuzz.trimf(konsystencja.universe, [6, 8, 10])
konsystencja['bardzo_gesta'] = fuzz.trimf(konsystencja.universe, [8, 10, 10])

slodycz['bez_slodyczy'] = fuzz.trimf(slodycz.universe, [0, 0, 4])
slodycz['niewiele_slodkie'] = fuzz.trimf(slodycz.universe, [0, 4, 6])
slodycz['umiarkowanie_slodkie'] = fuzz.trimf(slodycz.universe, [4, 6, 8])
slodycz['slodkie'] = fuzz.trimf(slodycz.universe, [6, 8, 10])
slodycz['bardzo_slodkie'] = fuzz.trimf(slodycz.universe, [8, 10, 10])

# Definowanie funkcje przynależności dla zmiennej wynikowej 'przydatnosc'
przydatnosc['mniej_przydatne'] = fuzz.trimf(przydatnosc.universe, [0, 0, 5])
przydatnosc['przydatne'] = fuzz.trimf(przydatnosc.universe, [0, 5, 10])
przydatnosc['bardzo_przydatne'] = fuzz.trimf(przydatnosc.universe, [5, 10, 10])

# Reguły "smak"
regula1 = ctrl.Rule(smak['bardzo_niesmaczne'], przydatnosc['mniej_przydatne'])
regula2 = ctrl.Rule(smak['niesmaczne'] | smak['przecietny_smak'], przydatnosc['przydatne'])
regula3 = ctrl.Rule(smak['smaczne'] | smak['bardzo_smaczne'], przydatnosc['bardzo_przydatne'])

# Reguły "pikantnosc"
regula4 = ctrl.Rule(pikantnosc['niska'] | pikantnosc['bardzo_lagodne'], przydatnosc['mniej_przydatne'])
regula5 = ctrl.Rule(pikantnosc['lagodne'] | pikantnosc['umiarkowane'], przydatnosc['przydatne'])
regula6 = ctrl.Rule(pikantnosc['ostra'] | pikantnosc['bardzo_ostra'], przydatnosc['bardzo_przydatne'])

# Reguły "konsystencja"
regula7 = ctrl.Rule(konsystencja['bardzo_plynna'] | konsystencja['plynna'], przydatnosc['mniej_przydatne'])
regula8 = ctrl.Rule(konsystencja['srednio_gesta'] | konsystencja['gesta'], przydatnosc['przydatne'])
regula9 = ctrl.Rule(konsystencja['bardzo_gesta'], przydatnosc['bardzo_przydatne'])

# Reguły "slodycz"
regula10 = ctrl.Rule(slodycz['bez_slodyczy'] | slodycz['niewiele_slodkie'], przydatnosc['mniej_przydatne'])
regula11 = ctrl.Rule(slodycz['umiarkowanie_slodkie'] | slodycz['slodkie'], przydatnosc['przydatne'])
regula12 = ctrl.Rule(slodycz['bardzo_slodkie'], przydatnosc['bardzo_przydatne'])

# Stworzenie systemu wnioskowania
system_expert = ctrl.ControlSystem([regula1, regula2, regula3, regula4, regula5, regula6, regula7, regula8, regula9, regula10, regula11, regula12])
system_oceny = ctrl.ControlSystemSimulation(system_expert)

# Interfejs użytkownika w konsoli
print("Czeszcz witam w mojej systemie oceny potraw !")
print("Podaj oceny od 0 do 10 dla każdej cechy.")

# Pobieranie danych od użytkownika
system_oceny.input['smak'] = float(input("Podaj ocenę smaku: "))
system_oceny.input['pikantnosc'] = float(input("Podaj ocenę pikantności: "))
system_oceny.input['konsystencja'] = float(input("Podaj ocenę konsystencji: "))
system_oceny.input['slodycz'] = float(input("Podaj ocenę słodyczy: "))



# Wykonanie obliczenia systemu
system_oceny.compute()


# Wyświetlenie wyniku
print("\nOcena przydatności potrawy:", system_oceny.output['przydatnosc'])
przydatnosc.view(sim=system_oceny)

# Test 1
system_oceny.input['smak'] = 3.0
system_oceny.input['pikantnosc'] = 2.0
system_oceny.input['konsystencja'] = 4.0
system_oceny.input['slodycz'] = 3.0

system_oceny.compute()
print("\nTest 1 - Ocena przydatności potrawy:", system_oceny.output['przydatnosc'])


# Test 2
system_oceny.input['smak'] = 1.0
system_oceny.input['pikantnosc'] = 2.0
system_oceny.input['konsystencja'] = 1.0
system_oceny.input['slodycz'] = 2.0

system_oceny.compute()
print("Test 2 - Ocena przydatności potrawy:", system_oceny.output['przydatnosc'])


# Test 3
system_oceny.input['smak'] = 6.0
system_oceny.input['pikantnosc'] = 3.0
system_oceny.input['konsystencja'] = 4.0
system_oceny.input['slodycz'] = 7.0

system_oceny.compute()
print("Test 3 - Ocena przydatności potrawy:", system_oceny.output['przydatnosc'])

