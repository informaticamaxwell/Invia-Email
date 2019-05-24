import smtplib #simple mail transfer protocol(protocollo di comunicazione usato
#dagli indirizzi di posta elettronica)

#variabili

username = raw_input('Inserisci il nome utente: ') 
psw = raw_input('Inserisci la password: ')

#############################################################

s=smtplib.SMTP('smtp.gmail.com',587) #provo a connettermi al server
s.ehlo() #se la connessione e' avvenuta allora invio un messaggio al server per dirgli che sono connesso
s.starttls() #avvio una comunicazione criptata

while(1==1):
    
    try:
        s.login(username, psw) #provo a loggarmi
        print 'Accesso effettuato, ora puoi scrivere il messaggio'
        destinatario = raw_input('Inserisci il destinatario della mail: ')
        messaggio = raw_input('Inserisci il testo della mail: ')
        s.sendmail(username, destinatario, messaggio) #invio la email
        print 'Messaggio inviato con successo'
        i = raw_input("Vuoi inviare un altra email[y]: ")
        if(i=='y'):
            continue
        else:
            break


    except: #gestisco l'eccezione 
        print('Credenziali errate...riprova')
        continue

print 'Chiudo programma...'

