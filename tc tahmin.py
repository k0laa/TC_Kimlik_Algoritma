eksik_tc = [int(c) for c in input("eksik tc gir:")]

eksik_basamak = 11 - len(eksik_tc)

for r in range(eksik_basamak):
    eksik_tc.append(9)

def format_kontrol(sayi):
    tek, cift,toplam = 0,0,0
    tek += sum(i for i in eksik_tc[0:9:2])
    cift += sum(i for i in eksik_tc[1:8:2])
    toplam += sum(i for i in eksik_tc[0:10])
    
    kural1 = (tek * 7 + cift * 9) % 10 == sayi[9]
    kural2 = (tek * 8) % 10 == sayi[10] 
    kural3 = toplam %10 == sayi[10] 
    
    return kural1 and kural2 and kural3

count = 0
for a in range(10 ** eksik_basamak):
    if(format_kontrol(eksik_tc)):
        print(''.join(map(str, eksik_tc)))
        count += 1
    number = int(''.join(map(str, eksik_tc)))
    number -= 1
    eksik_tc = [int(c) for c in str(number)]
    
print(f"{count} tane bulundu")