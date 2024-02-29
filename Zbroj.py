broj_znamenaka = int(input())
zbroj_znamenaka = int(input())

def zbrojznamenaka(broj):
    return 0 if broj == 0 else int(broj % 10) + zbrojznamenaka(int(broj / 10))

najmanji = 10*(broj_znamenaka-1)
najmanji_bool = False


while not najmanji_bool:
    if zbrojznamenaka(najmanji) == zbroj_znamenaka:
        najmanji_bool = True
        print(najmanji)
    else:
        najmanji += 1

najveci = (10**broj_znamenaka) - 1
najveci_bool = False


while not najveci_bool:
    if zbrojznamenaka(najveci) == zbroj_znamenaka:
        najveci_bool = True
        print(najveci)
    else:
        najveci -= 1