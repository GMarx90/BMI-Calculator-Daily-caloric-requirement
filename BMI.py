# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

name = input("Podaj imie: ")
print('Hello ', name.capitalize(), "!, I'll count your BMI")
decision=100
while not(decision==1):
        decision=100
        while True:
            height= input("What is your height in cm? ")
            try:
                height=float(height)/100
                if height<1.5 or height>2.3:
                    print('I think you put wrong height. you write: ')
                    print(height, "m. I'm sorry but this is weird but ok. Let's move on")

                break
            except ValueError:
                print("Wzrost podajemy w liczbie!")
        while True:        
            try:
                weight= float(input("What is your weight in kg? "))
                if weight<40 or weight>200:
                    print('I think you put wrong height. you write: ')
                    print(weight, "kg. I'm sorry but this is weird but ok. Let's move on")
                break
            except ValueError:
                print("Wage podajemy w liczbie!")
        try:
            BMI=weight/(height*height)
            BMI=float(BMI)
        except ZeroDivisionError:
            print('You cant give 0.. it cant be counted')
            BMI=0
			
        if BMI==0:
            print('You cant give 0.. it cant be counted')
            print("You can try again")
			
        if BMI<=16 and BMI!=0:
            print('Yours BMI is very bad! It is equal:  ', BMI, ' ! Thats mean you are starving')
    
        if  BMI>16 and BMI<=16.99:
            print('Yours BMI is bad! It is equal:  ', BMI, ' ! Thats mean you are skinny')
    
        if BMI > 17 and BMI<= 18.49:
            print('Yours BMI isnt good! It is equal:  ', BMI, ' ! Thats mean you are underweight')
    
        if BMI > 18.49 and BMI<= 24.99:
            print('Yours BMI is very good!! It is equal:  ', BMI, ' ! Thats mean Yours BMI has correct value')

        if BMI > 24.99 and BMI<= 29.99:
            print('Yours BMI isnt good!! It is equal:  ', BMI, ' ! Thats mean you are overweight')

        if BMI > 29.99 and BMI<= 34.99:
          print('Yours BMI is bad!! It is equal:  ', BMI, ' ! Thats mean you are in first degree of obesity')

        if BMI > 34.99 and BMI<= 39.99:
           print('Yours BMI is very bad!! It is equal:  ', BMI, ' ! Thats mean you are in second degree of obesity')
    
        if BMI > 39.99:
            print('Yours BMI is very very bad!! It is equal:  ', BMI, ' ! Thats mean you are in extreme obesit')
        while not(decision==2 or decision==1 or decision==0 ):
                    print("What now 0/1/2")
                    print("Select 0 to run again")
                    print("Select 1 to calculate total caloric requirement")
                    print("Select 2 to stop the app")
                    try:
                        decision=int(input('What to do (0/1/2) :\n'))
                        if decision==1:
                            sex=1111
                            sex=int(input("""What is yours sex? 0/1 \n 0 MALE \n 1 FAMALE \n"""))
                            if sex==0:
                                age=float(input("What is your age?"))
                                Activity=1111
                                Activity=input("""What is your activity - select correct answer: 
                                ______________________________________________________________________________________________
                                Czas aktywności fizycznej    |   Aktywność zawodowa                             |   Option    |
                                _____________________________|__________________________________________________|_____________|
                                                             |                                                  |             |
                                Brak aktywności fizycznej    | Brak aktywności zawodowej, chory, leżący         |       0     |
                                _____________________________|__________________________________________________|_____________|
                                Lekka aktywność (aktywność   | Pracownik biurowy, którego aktywność             |             |
                                – ok. 140 minut tygodniowo)  | związana jest wyłącznie z obowiązkami domowymi   |       1     |
                                _____________________________|__________________________________________________|_____________|
                                Średnia aktywność (aktywność | Pracownik biurowy, trenujący 2-3 razy w tygodniu |             |
                                – ok. 280 minut tygodniowo)	 | przez minimum godzinę                            |       2     |
                                _____________________________|__________________________________________________|_____________|
                                Wysoka aktywność (aktywność  | Pracownik biurowy, trenujący 3-4 razy w tygodniu |             |
                                – ok. 420 minut tygodniowo)	 | przez minimum godzinę                            |       3     |
                                _____________________________|__________________________________________________|_____________|
                                Bardzo wysoka aktywność      | Zawodowy sportowiec, trenujący minimum 6 godzin  |             |
                                (aktywność – ok. 560 minut   | tygodniowo lub osoba ciężko pracująca fizycznie  |       4     |
                                tygodniowo)                  |	                                                |             |
                                _____________________________|__________________________________________________|_____________|""")   
                                BMR = 655 + (9.6 * weight) + (1.8*height*100) - (4.7*age)*PAL
                                print(BMR)
                            else:
                                print("dupa")
                            print(sex)
                        if decision==2:
                            print(decision)
                            break;
                        if decision==0:
                            print('Ok, so one more time')
                            break;
                        else:
                            print('You have a choice 1 or 0')
                    except ValueError:
                        print('You have a choice 1 or 0')
                        
            
print("OK! Bye " + name.capitalize())
