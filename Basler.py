__author__ = 'Majkl'                                                                                               #já

import time                                                                                                        #Importuje knihovnu time
import webbrowser                                                                                                  #Importuje knihovnu webbrowser

t = time.localtime()                                                                                               #hodnota t je stejná jako time.localtime()
current_time = time.strftime("%H:%M", t)                                                                           #hodnota current_time je stejná jako time.strftime("%H:%M", t)

print("Zdravím. Jsem pouze jednoduchej script v Pythonu")                                                          # v terminálu napíše věc, co je v závorce
time.sleep(1)                                                                                                      #počká 1 sekundu
print("Zatím umím pouze říci čas :-(")                                                                             # v terminálu napíše věc, co je v závorce
time.sleep(1)                                                                                                     #počká 1 sekundu
print("Chceš, abych ti řekl čas? Ano/Ne/Autor")                                                                    # v terminálu napíše věc, co je v závorce
otazka = input()                                                                                                   #čeká na odpověď uživatele

if otazka == "Ano":                                                                                                #pokud je odpověď Ano, tak napíše čas do terminálu
    print(current_time)                                                                                            #napíše čas do terminálu
    time.sleep(1)                                                                                                  #počká 1 sekundu
    print("Nyní se ukončím.")                                                                                      # v terminálu napíše věc, co je v závorce
    time.sleep(5)                                                                                                  #počká 5 vteřin
    exit                                                                                                           #konec
# komentovaný kód se mi nepodařilo implementovat, protože neumím pracovat s "nested if statement" (neumím česky vyjádřit)
#    print("Chceš abych ti čas zobrazoval každou vteřinu, nebo se mám ukončit? Ano/Ne")                            # v terminálu napíše věc, co je v závorce
#    o2 = input()                                                                                                  #čeká na odpověď od uživatele
#   if o2 == "Ano":                                                                                                #pokud je odpověď Ano, tak bude do terminálu psát čas každou vteřinu, pokud je odpověď Ne, tak se script ukončí
#      print("Dobře. Zastavit mě můžeš pomocí tlačítek CTRL + C")                                                  # v terminálu napíše věc, co je v závorce
#       while 3 > 2:                                                                                               #když je 3 větší než 2 (cyklus [opakuje pořád dokola])
#        print(current_time)                                                                                       # v terminálu napíše věc, co je v závorce
#        time.sleep(1)                                                                                             #počká 1 sekundu
#    else:                                                                                                         # nebo
#        print("OK. Nyní se ukončím")                                                                              # v terminálu napíše věc, co je v závorce

elif otazka == "Ne":                                                                                               #pokud je odpověď na otázku Ne, tak se ukončí
    print("Ok. Nevadí. Nyní se ukončím")                                                                           # v terminálu napíše věc, co je v závorce
    time.sleep(5)                                                                                                  #počká 5 vteřin
    exit                                                                                                           # konec
elif otazka == "Rick":                                                                                             #pokud je odpověd na otázku Rick, tak otevře výchozí prohlížeč a spustí stránku
    print("Oh. Ty jsi našel skrytou část kódu. Well, tohle máš za odměnu ")                                        # v terminálu napíše věc, co je v závorce
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')                                                 #otevře se výchozí prohlížeč a spustí stránku
    time.sleep(5)                                                                                                  #počká 5 vteřin
    exit                                                                                                           #konec
elif otazka == "Autor":                                                                                            #pokud je odpověď Autor, vypíše se do terminálu text níže
    print(" ")                                                                                                     # v terminálu napíše mezeru
    print("Mým autorem je Michal Basler (E3)")                                                                     # v terminálu napíše věc, co je v závorce
    print("Byl jsem vytvořen 5.1.2021")                                                                            # v terminálu napíše věc, co je v závorce
    print("Pokud bude mít líné hovado na mě čas, tak mé aktualizace naleznete zde:" )                              # v terminálu napíše věc, co je v závorce
    print("https://github.com/Majklzbastlirny/SIV-Python-Simple")                                                  # v terminálu napíše věc, co je v závorce
    time.sleep(10)                                                                                                 #počká 10 vteřin
    exit                                                                                                           #konec
else:                                                                                                              #nebo
    print("Omlouvám se, ale to nebyla očekávaná odpověď. Nyní se ukončím")                                         # v terminálu napíše věc, co je v závorce
    time.sleep(3)                                                                                                  #počká 3 vteřin

exit                                                                                                               #konec