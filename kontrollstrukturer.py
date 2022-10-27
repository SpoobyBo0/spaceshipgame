import time
import fontstyle

# Travelbag
# Skelettkod till uppgiften

accounts = {}
logged_in = False

while True:
    menyval = input(
        "1. Skapa konto\n"
        "2. Logga in\n"
        "3. Läs en rolig historia\n"
        "4. Logga ut\n"
        "5. Avsluta program\n"
    )

    if menyval == "1":
        användarnamn = input("Användarnamn: ")
        lösenord = input("Lösenord: ")
        användarnamn_2 = fontstyle.apply(f"{användarnamn}")
        lösenord_2 = fontstyle.apply(f"{lösenord}")
        
        if användarnamn in accounts:
            print("Detta användarnamn finns redan testa ett annat ")
            
        else:

                
            accounts[användarnamn]=lösenord
            print(f"Ditt användarnamn är nu {användarnamn_2} och ditt lösenord är nu {lösenord_2}")
            time.sleep(2)
            # TODO Skapa ett konto genom att lägga till ett key-value par i accounts
            # username = key, password = value
            # Bonus: Kolla först så att användaren inte redan finns

            
        

    elif menyval == "2":
        # TODO Användaren ska få logga in med username och password
        # Ändra variabeln logged_in till True om de lyckas logga in
        # Bonus: Ge användaren ett visst antal försök att logga in
        försök = 0
        if försök <=3:
            print("Logga in: ")
            användarnamn_försök = input("Anvädarnamn: ")
            lösenord_försök = input("Lösenord: ")
            if användarnamn_försök in accounts:
                if accounts [användarnamn_försök] == lösenord_försök:
                
                    logged_in = True
                    print("Inloggad! ")
                    försök + 1
                    
                    
                
            if logged_in == False:
                                
                print("Fel användarnman eller lösenord ")
                försök + 1
                time.sleep(2)

    elif menyval == "3":
        # TODO skriv ut en rolig historia, men bara om användaren är inloggad
        # Bonus: Skriv ut en tråkig historia om de inte är inloggade
        if logged_in == True:
            print("En rolig historia ")
            time.sleep(2)
            
        else:
            print("Du behvöer logga in för att läsa den roliga historian med du får läsa en tråkig historia \n Din hardcore minecraft server är borta L")
            time.sleep(2)

    elif menyval == "4":
        # TODO Ändra variabeln logged_in till False
        # Bonus: Fråga om de är säkra först
        svar_säker = input("Är du säker på att du vill logga ut det var roligt att ha dig här: ").capitalize
        if svar_säker == "Ja":
            logged_in = False
            
            print("Du är utloggad! ")
            time.sleep(2)
        

    elif menyval == "5":
        break