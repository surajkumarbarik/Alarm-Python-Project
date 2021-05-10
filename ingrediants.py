import time

#comment added


print("\t\t\tHey!!! FOODY Welcome to The Ingrediants World....:-)")
def mainsec():
    try:
        n = int(input("Round Your Dish- \n 1. Prime Dishes \n 2. Special Premium \n 3. Exit\n Your Choice -  "))
    except Exception:
        print("Input is Not valid... \nPlease Try Again")
        mainsec()
    if n == 1:
        print("______________Welcome to PRIME DISHES______________")
        def sec2():
            print("\n\t\t\tHEY BUDDY!!! WELCOME TO VEG & NON-VEG SECTION ")
            try:
                ch1= int(input("\nLet's choice your taste \n1. VEG \n2. NON_VEG \n3. Exit"))
            except Exception:
                print("Input is Not valid... \nPlease Try Again")
                sec2()
            if ch1==1:
                print("\t\t\tHELLO VEG LOVER... Let's Enjoy...:-)")
                try:
                    ch=int(input("Select Your Numbers Of Meals- "))
                except Exception:
                    print("Input is Not valid... \nPlease Try Again")
                    sec2()
                try:
                    vg=int(input("Select your dish- \n 1. Dalma \n 2. Allu Vaja \n 3. Kobi vaja \n 4. Saga Vaja \n 5. Potala Vaja \n "
                             "6. Kadali Vaja \n 7. Jhudanga vaja \n 8. Mix Curry \n 9. Kobi Curry \n 10. Soyabin Curry \n 11. Allu Kasaa \n "
                             "12. Mushroom Curry \n 13. Paneer Curry"))
                except Exception:
                    print("Input is Not valid... \nPlease Try Again")
                    sec2()
                if vg==1:
                    print("\nYour DALAMA is on the way..... \n\n")
                    print("The  INGREDIANTS are- ")
                    time.sleep(2)
                    print("Harad Dal= ", ch * 50, " gm\nPotato= ", ch*50,
                          "gm\nWatermmellon= ", ch * 25, " gm \nCaroot= ", ch, " piece\nJhudanga= ", ch*50,
                          " gm\nBrinjal ", ch*50, " gm\nTej Patta= 2 piece \nOil= ", ch * 1.5,
                          " spoon\nDry Chilli= 2 piece\nPhutan= ", ch * 0.75, " spoon\nJeera= ", ch * 0.5,
                          " gm\nWater= ", ch * 70, " ml \nSalt= ", ch, " spoon\nTurmeric= ", ch * 0.25,
                          " spoon\nTomatto= ", ch, "Onion= ", ch * 0.25, " piece \nOil= ", ch * 1.5,
                          " spoon\nChilli= 2 piece\nPhutan= ", ch * 0.75, " spoon\nJeera= ", ch * 0.5, "spoon")
                    try:
                        vgoption=int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        mainsec()
                    if vgoption==1:
                        mainsec()
                    else:
                        print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                        exit()
                elif vg==2:
                    print("\nYour ALLU VAJA is on the way..... \n\n")
                    print("The  INGREDIANTS are- ")
                    time.sleep(2)
                    print("Potato= ", ch , " piece\nWater= ", 100, " ml \nSalt= ", ch, " spoon\nTurmeric= ", ch * 0.25,
                          " spoon\nOnion= ", ch * 0.25, " piece \nOil= ", ch * 1.5,
                          " spoon\nChilli= 2 piece\nPhutan= ", ch * 0.75," spoon")
                    try:
                        vgoption=int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        mainsec()
                    if vgoption==1:
                        mainsec()
                    else:
                        print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                        exit()

                elif vg==3:
                    print("\nYour KOBI VAJA is on the way..... \n\n")
                    print("The  INGREDIANTS are- ")
                    time.sleep(2)
                    print("Cauliflower= ", ch*60, " gm\nWater= ", ch*100, " ml \nSalt= ", ch, " spoon\nTurmeric= ", ch * 0.25,
                          " spoon\nOnion= ", ch * 0.25, " piece \nOil= ", ch * 1.5,
                          " spoon\nChilli= 2 piece\nJeera= ", ch * 0.75, " spoon\nRed Chilli Powder= ",ch*0.5," spoon")
                    try:
                        vgoption=int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        mainsec()
                    if vgoption==1:
                        mainsec()
                    else:
                        print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                        exit()

                elif vg==4:
                    print("\nYour SAGA VAJA is on the way..... \n\n")
                    print("The  INGREDIANTS are- ")
                    time.sleep(2)
                    print("Amarnath Leaves(Leutia Saga)= ", ch*175, " gm\nWater= ", 100, " ml\nSalt= ", ch, " spoon\nTurmeric= ", ch * 0.25,
                          " spoon\nOnion= ", ch * 0.25, "piece \nOil= ", ch * 1.5,
                          " spoon\nDry Chilli= 2 piece\nGarlic= 5 piece")
                    try:
                        vgoption=int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        mainsec()
                    if vgoption==1:
                        mainsec()
                    else:
                        print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                        exit()

                elif vg==5:
                    print("\nYour POTALA VAJA is on the way..... \n\n")
                    print("The  INGREDIANTS are- ")
                    time.sleep(2)
                    print("Pointed Gourd(Potala)= ", ch*3, " piece\nWater= ", 100, " ml\nSalt= ", ch, " spoon\nTurmeric= ", ch * 0.25,
                          " spoon\nOnion= ", ch * 0.25, " piece \nOil= ", ch * 1.5,
                          " spoon\nGreen Chilli= 2 piece\nPhutan= ", ch * 0.75, " spoon\nRoasted Cumin Powder= 0.5 spoon")
                    try:
                        vgoption=int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        mainsec()
                    if vgoption==1:
                        mainsec()
                    else:
                        print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                        exit()

                elif vg==6:
                    print("\nYour KADALI VAJA is on the way..... \n\n")
                    print("The  INGREDIANTS are- ")
                    time.sleep(2)
                    print("Raw Banana= ", ch*2, " piece\nWater= ", 100, " ml\nSalt= ", ch, " spoon\nTurmeric= ", ch * 0.25,
                          " spoon\nOnion= ", ch * 0.25, " piece \nOil= ", ch * 1.5,
                          " spoon\nDry Red Chilli= 2 piece\nPhutan= ", ch * 0.75, " spoon\nRoasted Cumin Powder= ",ch," spoon")
                    try:
                        vgoption=int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        mainsec()
                    if vgoption==1:
                        mainsec()
                    else:
                        print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                        exit()

                elif vg==7:
                    print("\nYour JHUDANGA VAJA is on the way..... \n\n")
                    print("The  INGREDIANTS are- ")
                    time.sleep(2)
                    print("Yard Long Beans= ", ch * 50, " gm\nWater= ", ch * 100, " ml\nSalt= ", ch, " spoon\nTurmeric= ",
                          ch * 0.25,
                          " spoon\nOnion= ", ch * 0.25, " piece \nOil= ", ch * 1.5,
                          " spoon\nChilli= 2 piece\nJeera= ", ch * 0.75, " spoon\nRed Chilli Powder= ", ch * 0.5, " spoon")
                    try:
                        vgoption=int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        mainsec()
                    if vgoption==1:
                        mainsec()
                    else:
                        print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                        exit()

                elif vg==8:
                    print("\nYour MIX VEG is on the way..... \n\n")
                    print("The  INGREDIANTS are- ")
                    time.sleep(2)
                    print("Paneer= ", ch * 8, " piece\nBadam= ", ch * 7, " piece \nPatato= ", ch, " piece\nCarrot= ",
                          ch * 0.5," piece\nMatar= ", ch * 10, " gm \nCapsicum= ", ch * 0.5,
                          " piece\nCauliflower= ", ch * 35, " gm\nWater= ", ch * 150, "ml \nSalt= ", ch, " spoon\nTurmeric= ",
                          ch * 0.25,
                          " spoon\nOnion= ", ch * 0.5, " piece \nOil= ", ch * 1.5,
                          " spoon\nRed Chilli Powder= ",ch," spoon\nJeera= ", ch * 0.75, " spoon\nKashmir Chilli Powder= ", ch * 0.5,
                          " spoon\nTej Patta= 2 piece\nKasuri Methi= ",ch*75," gm\nGinger Garlic Paste= ",ch," spoon\nGreen Chilli=",ch,
                          "piece\nCoriander Powder= ",ch," spoon\nCumin Powder= ",ch," spoon\nGaram Masala= ",ch," spoon")
                    try:
                        vgoption=int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        mainsec()
                    if vgoption==1:
                        mainsec()
                    else:
                        print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                        exit()


                elif vg==9:
                    print("\nYour KOBI CURRY is on the way..... \n\n")
                    print("The  INGREDIANTS are- ")
                    time.sleep(2)
                    print("Patato= ", ch, " piece\nCauliflower= ", ch * 150, " gm\nWater= ", ch * 150, "ml \nSalt= ", ch,
                          " spoon\nTurmeric= ",
                          ch * 0.25,
                          " spoon\nOnion= ", ch * 0.5, " piece \nOil= ", ch * 1.5,
                          " spoon\nRed Chilli Powder= ", ch, " spoon\nJeera= ", ch * 0.75, " spoon\nKashmir Chilli Powder= ",
                          ch * 0.5,
                          " spoon\nTej Patta= 2 piece\nGinger Garlic Paste= ", ch*1.5,
                          " spoon\nGreen Chilli=", ch,
                          "piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ",ch," spoon")
                    try:
                        vgoption=int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        mainsec()
                    if vgoption==1:
                        mainsec()
                    else:
                        print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                        exit()

                elif vg==10:
                    print("\nYour SOYABIN CURRY is on the way..... \n\n")
                    print("The  INGREDIANTS are- ")
                    time.sleep(2)
                    print("Patato= ", ch, " piece\nSoyabean= ", ch * 150, " gm\nWater= ", ch * 150, "ml \nSalt= ", ch,
                          " spoon\nTurmeric= ",
                          ch * 0.25,
                          " spoon\ntomato= ",ch," piece\nOnion= ", ch * 0.5, " piece \nOil= ", ch * 1.5,
                          " spoon\nRed Chilli Powder= ", ch, " spoon\nJeera= ", ch * 0.75, " spoon\nKashmir Chilli Powder= ",
                          ch * 0.5,
                          " spoon\nTej Patta= 2 piece\nGinger Garlic Paste= ", ch * 1.5,
                          " spoon\nGreen Chilli=", ch,
                          "piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ",ch," spoon")
                    try:
                        vgoption=int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        mainsec()
                    if vgoption==1:
                        mainsec()
                    else:
                        print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                        exit()

                elif vg==11:
                    print("\nYour ALLU KASAA is on the way..... \n\n")
                    print("The  INGREDIANTS are- ")
                    time.sleep(2)
                    print("Patato= ", ch*1.5, " piece\nWater= ", ch * 150, "ml \nSalt= ", ch,
                          " spoon\nTurmeric= ",
                          ch * 0.25,
                          " spoon\ntomato= ", ch, " piece\nOnion= ", ch , " piece \nOil= ", ch * 1.5,
                          " spoon\nRed Chilli Powder= ", ch, " spoon\nJeera= ", ch * 0.75, " spoon\nKashmir Chilli Powder= ",
                          ch * 0.5,
                          " spoon\nTej Patta= 2 piece\nGinger Garlic Paste= ", ch * 1.5,
                          " spoon\nGreen Chilli=", ch,
                          "piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ", ch,
                          " spoon")
                    try:
                        vgoption=int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        mainsec()
                    if vgoption==1:
                        mainsec()
                    else:
                        print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                        exit()

                elif vg==13:
                    print("\nYour PANEER MASALA is on the way..... \n\n")
                    print("The  INGREDIANTS are- ")
                    time.sleep(2)
                    print("Patato= ", ch, " piece\nPaneer= ", ch * 100, " gm\nWater= ", ch * 150, "ml \nSalt= ", ch,
                          " spoon\nTurmeric= ",
                          ch * 0.25,
                          " spoon\ntomato= ", ch, " piece\nOnion= ", ch * 0.5, " piece \nOil= ", ch * 1.5,
                          " spoon\nRed Chilli Powder= ", ch, " spoon\nJeera= ", ch * 0.75, " spoon\nKashmir Chilli Powder= ",
                          ch * 0.5," spoon\nCashews= ",ch*8,
                          " piece\nTej Patta= 2 piece\nGinger Garlic Paste= ", ch * 2,
                          " spoon\nGreen Chilli=", ch,
                          "piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ", ch,
                          " spoon")
                    try:
                        vgoption=int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        mainsec()
                    if vgoption==1:
                        mainsec()
                    else:
                        print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                        exit()

                elif vg==12:
                    print("\nYour MUSHROOM MASALA is on the way..... \n\n")
                    print("The  INGREDIANTS are- ")
                    time.sleep(2)
                    print("Mushroom= ", ch * 200, " gm\nWater= ", ch * 150, "ml \nSalt= ", ch,
                          " spoon\nTurmeric= ",
                          ch * 0.25,
                          " spoon\ntomato= ", ch, " piece\nOnion= ", ch * 0.5, " piece \nOil= ", ch * 1.5,
                          " spoon\nRed Chilli Powder= ", ch, " spoon\nJeera= ", ch * 0.75, " spoon\nKashmir Chilli Powder= ",
                          ch * 0.5, " spoon\nCashews= ", ch * 8,
                          " piece\nTej Patta= 2 piece\nGinger Garlic Paste= ", ch * 2,
                          " spoon\nGreen Chilli=", ch,
                          "piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ", ch,
                          " spoon")
                    try:
                        vgoption=int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        mainsec()
                    if vgoption==1:
                        mainsec()
                    else:
                        print("\n\n\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                        exit()

                else:
                    print("HEY!!! WRONG INPUT... PLEASE TRY AGAIN")
                    sec2()

            elif ch1 == 2:
                def sec4():
                    print("\t\t\tHELLO NON-VEG LOVER... Let's Enjoy...:-)")
                    ch = int(input("Select Your Numbers Of Meals- "))
                    try:
                        nnvg = int(input(
                        "Select your dish- \n 1. MACHA VAJA \n 2. MACHA BESARA \n 3. MACHA CURRY \n 4. CHINGUDI VAJA \n 5. CHINGUDI CURRY \n "
                        "6. EGG FRY \n 7. CHICKEN KASAA \n 8. MUTTON KASAA"))
                    except Exception:
                        print("Input is Not valid... \nPlease Try Again")
                        sec4()
                    if nnvg == 1:
                        print("\nYour MACHA VAJA is on the way..... \n\n")
                        print("The  INGREDIANTS are- ")
                        time.sleep(2)
                        print("Fish(Machaa)= ", ch * 2, " piece\nSalt= ", ch*2, " spoon\nTurmeric= ", ch * 2,
                              " spoon\nOil= ", ch * 4,
                              " spoon")
                        try:
                            vgoption = int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                        except Exception:
                            print("Input is Not valid... \nPlease Try Again")
                            sec4()
                        if vgoption == 1:
                            mainsec()
                        else:
                            print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                            exit()
                    elif nnvg == 2:
                        print("\nYour MACHA BESARA is on the way..... \n\n")
                        print("The  INGREDIANTS are- ")
                        time.sleep(2)
                        print("Fish(Macha)= ", ch*2, " piece\nWater= ", 100, " ml \nSalt= ", ch, " spoon\nTurmeric= ", ch * 0.25,
                              " spoon\nOnion= ", ch * 0.25, " piece \nOil= ", ch * 1.5,
                              " spoon\nChilli= 2 piece\nMustard Seed= ", ch * 1.5, " spoon\nTomato= ",ch," piece\nRed Chilli Powder= ",ch,
                              " spoon\nPhutan= ",ch," spoon\nCoriander Powder= ",ch," spoon\nCumin Powder= ",ch," spoon")
                        try:
                            vgoption = int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                        except Exception:
                            print("Input is Not valid... \nPlease Try Again")
                            sec4()
                        if vgoption == 1:
                            mainsec()
                        else:
                            print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                            exit()

                    elif nnvg == 3:
                        print("\nYour MACHA CURRY is on the way..... \n\n")
                        print("The  INGREDIANTS are- ")
                        time.sleep(2)
                        print("Patato= ", ch*0.5, " piece\nFish(Macha)= ", ch * 2, " piece\nWater= ", ch * 150, "ml \nSalt= ", ch,
                              " spoon\nTurmeric= ",
                              ch * 0.25,
                              " spoon\nOnion= ", ch * 0.5, " piece \nOil= ", ch * 1.5,
                              " spoon\nRed Chilli Powder= ", ch, " spoon\nJeera= ", ch * 0.75,
                              " spoon\nKashmir Chilli Powder= ",ch * 0.5,
                              " spoon\nTej Patta= 2 piece\nGinger Garlic Paste= ", ch * 1.5,
                              " spoon\nGreen Chilli=", ch,
                              " piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ", ch,
                              " spoon")
                        try:
                            vgoption = int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                        except Exception:
                            print("Input is Not valid... \nPlease Try Again")
                            sec4()
                        if vgoption == 1:
                            mainsec()
                        else:
                            print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                            exit()

                    elif nnvg == 4:
                        print("\nYour CHINGUDI VAJA is on the way..... \n\n")
                        print("The  INGREDIANTS are- ")
                        time.sleep(2)
                        print("Chingudi= ", ch * 4, " piece\nOil= ", ch * 1.5,
                              " spoon\nSalt= ", ch*2, " spoon\nTurmeric= ", ch * 2,
                              " spoon\nOil= ", ch * 4,
                              " spoon")
                        try:
                            vgoption = int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                        except Exception:
                            print("Input is Not valid... \nPlease Try Again")
                            sec4()
                        if vgoption == 1:
                            mainsec()
                        else:
                            print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                            exit()

                    elif nnvg == 5:
                        print("\nYour CHINGUDI CURRY is on the way..... \n\n")
                        print("The  INGREDIANTS are- ")
                        time.sleep(2)
                        print("Prawn(Chingudi)= ", ch * 4, " piece\nWater= ", ch * 150, "ml \nSalt= ", ch,
                              " spoon\nTurmeric= ",
                              ch * 0.25,
                              " spoon\nOnion= ", ch * 0.5, " piece \nOil= ", ch * 1.5,
                              " spoon\nRed Chilli Powder= ", ch, " spoon\nJeera= ", ch * 0.75,
                              " spoon\nKashmir Chilli Powder= ",ch * 0.5,
                              " spoon\nTej Patta= 2 piece\nGinger Garlic Paste= ", ch * 1.5,
                              " spoon\nGreen Chilli=", ch,
                              " piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ", ch,
                              " spoon")
                        try:
                            vgoption = int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                        except Exception:
                            print("Input is Not valid... \nPlease Try Again")
                            sec4()
                        if vgoption == 1:
                            mainsec()
                        else:
                            print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                            exit()

                    elif nnvg == 6:
                        print("\nYour EGG FRY is on the way..... \n\n")
                        print("The  INGREDIANTS are- ")
                        time.sleep(2)
                        print("Boiled Egg= ", ch * 2, " piece\nWater= ", ch * 150, "ml \nSalt= ", ch,
                              " spoon\nTurmeric= ",ch * 0.25,
                              " spoon\nOnion= ", ch * 0.5, " piece \nOil= ", ch * 1.5,
                              " spoon\nRed Chilli Powder= ", ch, " spoon\nJeera= ", ch * 0.75,
                              " spoon\nKashmir Chilli Powder= ",ch * 0.5,
                              " spoon\nTej Patta= 2 piece\nGinger Garlic Paste= ", ch * 1.5,
                              " spoon\nGreen Chilli=", ch,
                              " piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ", ch,
                              " spoon")
                        try:
                            vgoption = int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                        except Exception:
                            print("Input is Not valid... \nPlease Try Again")
                            sec4()
                        if vgoption == 1:
                            mainsec()
                        else:
                            print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                            exit()

                    elif nnvg == 7:
                        print("\nYour CHICKEN KASAA is on the way..... \n\n")
                        print("The  INGREDIANTS are- ")
                        time.sleep(2)
                        print("Chicken= ", ch * 200, " gm\nWater= ", ch * 150, "ml \nSalt= ", ch,
                              " spoon\nTurmeric= ",ch * 0.25,
                              " spoon\nOnion= ", ch * 0.5, " piece \nOil= ", ch * 1.5,
                              " spoon\nRed Chilli Powder= ", ch, " spoon\nJeera= ", ch * 0.75,
                              " spoon\nKashmir Chilli Powder= ",ch * 0.5,
                              " spoon\nTej Patta= 2 piece\nGinger Garlic Paste= ", ch * 1.5,
                              " spoon\nGreen Chilli=", ch,
                              " piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ", ch,
                              " spoon\nChicken Masala= ",ch," spoon")
                        try:
                            vgoption = int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                        except Exception:
                            print("Input is Not valid... \nPlease Try Again")
                            sec4()
                        if vgoption == 1:
                            mainsec()
                        else:
                            print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                            exit()

                    elif nnvg == 8:
                        print("\nYour MUTTON KASAA is on the way..... \n\n")
                        print("The  INGREDIANTS are- ")
                        time.sleep(2)
                        print("Mutton= ", ch * 200, " gm\nWater= ", ch * 150, "ml \nSalt= ", ch,
                              " spoon\nTurmeric= ",ch * 0.25,
                              " spoon\nOnion= ", ch * 0.5, " piece \nOil= ", ch * 1.5,
                              " spoon\nRed Chilli Powder= ", ch, " spoon\nJeera= ", ch * 0.75,
                              " spoon\nKashmir Chilli Powder= ",ch * 0.5,
                              " spoon\nTej Patta= 2 piece\nGinger Garlic Paste= ", ch * 1.5,
                              " spoon\nGreen Chilli=", ch,
                              " piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ", ch,
                              " spoon\nMeat/Mutton Masala= ",ch," spoon")
                        try:
                            vgoption = int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For Other Dishes \n2. Exit"))
                        except Exception:
                            print("Input is Not valid... \nPlease Try Again")
                            sec4()
                        if vgoption == 1:
                            mainsec()
                        else:
                            print("\n\n\t\tT     H     A     N     K        Y     O     U ")
                            exit()
                    else:
                        print("HEY!!! WRONG INPUT... PLEASE TRY AGAIN")
                        sec2()
                    print("\n\t\t\tT H A N K    Y O U")
                sec4()
            elif ch1==3:
                print("\n\t\t\tT H A N K   Y O U")
                exit()
            else:
                print("WRONG INPUT... TRY AGAIN!!!")
                sec2()



        def sec1():
            item = int(input("Select Your Basic Meal's Item- \n1. Rice \n2. Dal \n3. Exit\nYour Choice- "))
            try:
                ch = int(input("Select your numbers of Meals- "))
            except Exception:
                print("Input is Not valid... \nPlease Try Again")
                sec1()
            if item == 1:
                print("\nYour RICE is on the way.....\n\n")
                print("The INGREDIANTS are- \n")
                time.sleep(2)
                print("Rice= ", ch * 120, "gm\nWater= ", ch, "ltr\nSalt= 1 spoon")
                try:
                    feedback = int(input("\nPress \n1. Any Other Basic Meals \n2. Move to Veg-Non Veg Section \n3. Exit Menu"))
                except Exception:
                    print("Input is Not valid... \nPlease Try Again")
                    sec1()
                if feedback == 1:
                    sec1()
                elif feedback==2:
                    sec2()
            elif item == 2:
                print("\nYour DAL is on the way..... \n\n")
                print("The  INGREDIANTS are- \n")
                time.sleep(2)
                print("Harad Dal= ", ch * 50, "gm\nWater= ", ch * 70, "ml \nSalt= ", ch, "spoon\nTurmeric= ", ch * 0.25,
                      "spoon\nTomatto= ", ch, "Onion= ", ch * 0.25, "piece \nOil= ", ch * 1.5,
                      "spoon\nChilli= 2 piece\nPhutan= ", ch * 0.75, "spoon\nJeera= ", ch * 0.5, "spoon")
                try:
                    feedback = int(input("\nPress \n1. Any Other Basic Meals \n2. Move to Veg-Non Veg Section \n3. Exit Menu"))
                except Exception:
                    print("Input is Not valid... \nPlease Try Again")
                    sec1()
                if feedback == 1:
                    sec1()
                elif feedback == 2:
                    sec2()
                else:
                    print("Invalid Input. \nTry Again")
                    sec1()
            elif item == 3:
                print("\n\t\t\t\n\nT     H     A     N     K        Y     O     U ")
                exit()
            else:
                print("Invalid Input. \nTry Again")
                sec1()
        sec1()

    elif n==2:
        def sec3():
            print("______________Welcome to SPECIAL PREMIUM SECTION[THE BIRYANI & PAKHALA]______________")
            try:
                ch = int(input("Select Your Numbers Of Meals- "))
            except Exception:
                print("Input is Not valid... \nPlease Try Again")
                sec3()
            try:
                spcl = int(input(
                "Select your dish- \n 1. DAHI PAKHALA \n 2. VEG BIRYANI \n 3. CHICKEN BIRYANI \n 4. MUTTON BIRYANI \n 5. PRAWN BIRYANI"))
            except Exception:
                print("Input is Not valid... \nPlease Try Again")
                sec3()
            if spcl == 1:
                print("\nYour DAHI PAKHALA is on the way..... \n\n")
                print("The  INGREDIANTS are- \n")
                time.sleep(2)
                print("Rice= ", ch * 2, " cup\nSalt= ", ch * 2, " spoon(as taste)\nGreen Chilli= ",ch*2,
                      " piece\nCurry Leaves= 5,6 pieces\nDry Red Chilli= ",ch*2," pieces\nCurd(Dahi)= ",ch*150," gm\nPhutana= ",ch," spoon")
                try:
                    vgoption = int(input("\n\nThis is All About Recipe.\n Choose One- \n1. For SPECIAL PREMIUM \n2. For MAIN MENU \n3. Exit"))
                except Exception:
                    print("Input is Not valid... \nPlease Try Again")
                    sec3()
                if vgoption == 1:
                    sec3()
                elif vgoption== 2:
                    mainsec()
                else:
                    print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                    exit()
            elif spcl == 3:
                print("\nYour CHICKEN BIRYANI is on the way..... \n\n")
                print("The  INGREDIANTS are- \n")
                time.sleep(2)
                print("Basmati Rice= ",ch*2," cup\nLeg Piece Chicken= ",ch*250," gm\nWater= ",ch*6," cup\nOnion= ",ch*2,
                      " pieces\nOil= ",ch*4," spoon\nYogurt(curd)= ",ch*200," gm\nTomato Puree= ",ch*6,
                      " spoon\nGinger Garlic Paste= ",ch*1.5," spoon\nGhee= ",ch*2," spoon\nSalt= ",ch*3.25,
                      " spoon\nCloves & Cardamom= 8/9 pieces\nMint Leaves= 1 cup\nCoriander Leaves= ",ch," cup\nKashmir Chilli Powder= ",ch * 0.5,
                          " spoon\nTej Patta= 2 piece\nGreen Chilli=", ch,
                          " piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ", ch,
                          " spoon\nChicken Masala= ",ch," spoon\nBiryani Masala= 1 packet")
                try:
                    vgoption = int(input(
                    "\n\nThis is All About Recipe.\n Choose One- \n1. For SPECIAL PREMIUM \n2. For MAIN MENU \n3. Exit"))
                except Exception:
                    print("Input is Not valid... \nPlease Try Again")
                    sec3()
                if vgoption == 1:
                    sec3()
                elif vgoption == 2:
                    mainsec()
                else:
                    print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                    exit()

            elif spcl == 4:
                print("\nYour MUTTON BIRYANI is on the way..... \n\n")
                print("The  INGREDIANTS are- \n")
                time.sleep(2)
                print("Basmati Rice= ",ch*2," cup\nLarge Size Mutton= ",ch*250," gm\nWater= ",ch*6," cup\nOnion= ",ch*2,
                      " pieces\nOil= ",ch*4," spoon\nYogurt(curd)= ",ch*200," gm\nTomato Puree= ",ch*6,
                      " spoon\nGinger Garlic Paste= ",ch*1.5," spoon\nGhee= ",ch*2," spoon\nSalt= ",ch*3.25,
                      " spoon\nCloves & Cardamom= 8/9 pieces\nMint Leaves= 1 cup\nCoriander Leaves= ",ch," cup\nKashmir Chilli Powder= ",ch * 0.5,
                          " spoon\nTej Patta= 2 piece\nGreen Chilli=", ch,
                          " piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ", ch,
                          " spoon\nMeat Masala= ",ch," spoon\nBiryani Masala= 1 packet\nDahi Raita= ",ch*2," cup")
                try:
                    vgoption = int(input(
                    "\n\nThis is All About Recipe.\n Choose One- \n1. For SPECIAL PREMIUM \n2. For MAIN MENU \n3. Exit"))
                except Exception:
                    print("Input is Not valid... \nPlease Try Again")
                    sec3()
                if vgoption == 1:
                    sec3()
                elif vgoption == 2:
                    mainsec()
                else:
                    print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                    exit()

            elif spcl == 5:
                print("\nYour PRAWN BIRYANI is on the way..... \n\n")
                print("The  INGREDIANTS are- \n")
                time.sleep(2)
                print("Basmati Rice= ",ch*2," cup\nBagda Prawn(Chingudi)= ",ch*4," piece\nWater= ",ch*6," cup\nOnion= ",ch*2,
                      " pieces\nOil= ",ch*4," spoon\nYogurt(curd)= ",ch*200," gm\nTomato Puree= ",ch*6,
                      " spoon\nGinger Garlic Paste= ",ch*1.5," spoon\nGhee= ",ch*2," spoon\nSalt= ",ch*3.25,
                      " spoon\nCloves & Cardamom= 8/9 pieces\nMint Leaves= 1 cup\nCoriander Leaves= ",ch," cup\nKashmir Chilli Powder= ",ch * 0.5,
                          " spoon\nTej Patta= 2 piece\nGreen Chilli=", ch,
                          " piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ", ch,
                          " spoon\nMeat Masala= ",ch," spoon\nBiryani Masala= 1 packet\nDahi Raita= ",ch*2," cup")
                try:
                    vgoption = int(input(
                    "\n\nThis is All About Recipe.\n Choose One- \n1. For SPECIAL PREMIUM \n2. For MAIN MENU \n3. Exit"))
                except Exception:
                    print("Input is Not valid... \nPlease Try Again")
                    sec3()
                if vgoption == 1:
                    sec3()
                elif vgoption == 2:
                    mainsec()
                else:
                    print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                    exit()

            elif spcl == 2:
                print("\nYour VEG BIRYANI is on the way..... \n\n")
                print("The  INGREDIANTS are- \n")
                time.sleep(2)
                print("Basmati Rice= ",ch*2," cup\nPaneer= ", ch * 6, " piece\nBadam= ", ch * 7, " piece \nPatato= ", ch, " piece\nCarrot= ",
                          ch * 0.5," piece\nSoyabean= ",ch*8," piece\nMatar= ", ch * 10, " gm \nCapsicum= ", ch * 0.5,
                          " piece\nCauliflower= ", ch * 35, " gm\nWater= ",ch*6," cup\nOnion= ",ch*2,
                      " pieces\nOil= ",ch*8," spoon\nYogurt(curd)= ",ch*200," gm\nTomato Puree= ",ch*6,
                      " spoon\nGinger Garlic Paste= ",ch*1.5," spoon\nGhee= ",ch*2," spoon\nSalt= ",ch*3.25,
                      " spoon\nCloves & Cardamom= 8/9 pieces\nMint Leaves= 1 cup\nCoriander Leaves= ",ch," cup\nKashmir Chilli Powder= ",ch * 0.5,
                          " spoon\nTej Patta= 2 piece\nGreen Chilli=", ch,
                          " piece\nCoriander Powder= ", ch, " spoon\nCumin Powder= ", ch, " spoon\nGaram Masala= ", ch,
                          " spoon\nBiryani Masala= 1 packet\nDahi Raita= ",ch*2," cup")
                try:
                    vgoption = int(input(
                    "\n\nThis is All About Recipe.\n Choose One- \n1. For SPECIAL PREMIUM \n2. For MAIN MENU \n3. Exit"))
                except Exception:
                    print("Input is Not valid... \nPlease Try Again")
                    sec3()
                if vgoption == 1:
                    sec3()
                elif vgoption == 2:
                    mainsec()
                else:
                    print("\n\n\t\t\tT     H     A     N     K        Y     O     U ")
                    exit()

            else:
                print("HEY!!! WRONG INPUT... PLEASE TRY AGAIN")
                sec3()
        sec3()
    elif n==3:
        print("\n\t\t\tT    H    A    N    K      Y    O    U ")
        exit()
    else:
        print("WRONG INPUT... YOU SHOULD TRY AGAIN!!!")
        mainsec()


mainsec()

