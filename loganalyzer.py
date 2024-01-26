# Daniel Ekholm daniel.ekholm@edu.edugrade.se
import sys
def load(filepath, action):
    file = filepath[1]
    argument = action[2]
    with open(file) as f:
        if argument == 'statistics':   
                count_error = 0     # Skapar en variabel för att kunna räkna upp när 'error' hittas.
                count_notice = 0    # Skapar en variabel för att kunna räkna upp när 'notice' hittas.
                for line in f:      # för varje rad i f, gör:
                    line = line.strip()     # strippar så det inte sker radbrytning och skapar upp variabeln line.
                    if line.find('error') != -1:      # Om error hittats.
                        count_error += 1     # öka count_error med 1.
                    if line.find('notice') != -1:     # Om notice hittats.
                        count_notice = count_notice + 1   # öka count_notice med 1.      
                print('errors ' + str(count_error)) # printa error + antal när for-loopen gått klart.
                print('notice ' + str(count_notice)) # printa notice + antal när for-loopen gått klart.
        elif argument == 'error':
                for line in f:      # för varje rad i f, gör:
                    linestrip = line.strip().split(' ')     # Splitta för att kunna hitta de olika delarna, strip för att det inte ska bli radbrytningar
                    trigger = linestrip[5]      # Error / notice sparas i trigger
                    error = trigger.find('error')       # går igenom trigger och letar efter 'error'
                    datum = linestrip[0:5]      # Plocka ut delen för datumet
                    message = linestrip[6:]     # Plocka ut delen för meddelandet
                    if error != -1:     # Om 'error' har hittats så är värdet INTE -1 så skriver vi ut datum + meddelandet
                        print(' '.join(datum).strip('[]') + ' ' + ' '.join(message)) # Sätt ihop strängarna och skriv ut, trimma bort [] från datumet         
        elif argument == 'notice':
                for line in f:      # för varje rad i f, gör:
                    linestrip = line.strip().split(" ")     # Splitta för att kunna hitta de olika delarna, strip för att det inte ska bli radbrytningar
                    trigger = linestrip[5]      # Error / notice
                    notice = trigger.find('notice')     # går igenom trigger och letar efter 'notice'
                    datum = linestrip[0:5]      # Plocka ut delen för datumet
                    message = linestrip[6:]     # Plocka ut delen meddelandet
                    if notice != -1:        # Om 'notice' har hittats så är värdet INTE -1 så skriver vi ut datum + meddelandet
                        print(' '.join(datum).strip('[]') + ' ' + ' '.join(message)) # Sätt ihop strängarna och skriv ut, trimma bort [] från datumet
if __name__ == "__main__":      # Börja programmet här
    if len(sys.argv) == 3:      # Om programmet körs med 3 argument gör detta:
        load(sys.argv, sys.argv)        # Anropar load och skickar med 2 parametrar
    else:
        print('Skicka med: filnamn och error/notice/statistics')        # Printas ifall man kört programmet utan att ge 3 argument