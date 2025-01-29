"""Hjälpkod för att komma igång
 * Notera att båda klasserna är i samma fil för att det ska underlätta.
 * Om programmet blir större bör man ha klasserna i separata filer såsom jag går genom i filmen
 * Då kan det vara läge att ställa in startvärden som jag gjort.
 * Man kan också skriva ut saker i konsollen i konstruktorn för att se att den "vaknar"
 * Denna kod hjälper mest om du siktar mot betyget E och C
 * För högre betyg krävs mer självständigt arbete
 """





class Buss:
    passagerare = []
    antal_passagerare = 0

    def run(self):  
        print("Välkommen till Buss-simulatorn")
        # Här ska menyn ligga för att göra saker
        # Vi rekommenderar switch och case här
        # Dessutom visar jag hur man anropar metoderna nedan via menyn
        # Börja nu med att köra koden för att se att det fungerar innan ni sätter igång med menyn.
        # Bygg sedan steg-för-steg och testkör koden.
        menu = """
        1. Add a passenger
        2. Print the bus, or rather – print all ages of passengers.
        3. Calculate the total age of all passengers.
        4. Exit the program
        """
        print(menu)
        while True:
            response = input("Choose from meun(1, 2, 3 or 4): ")
            if response == "1":
                self.add_passanger()
            elif response == "2":
                self.print_buss()
            elif response == "3":
                self.calc_average_age()
            else:
                exit()

    # Metoder för betyget E

    def add_passanger(self):
        # ordet pass måste finnas i "tomma" funktioner för att de ska kunna kompileras i Python, när du har 
        # något som inte är en kommentar i funktion, tex print("test") skall "pass" tas bort
        if self.antal_passagerare > 25:
            print("The buss capacity is full")
            return 

        print("We are in add passanger.")
        gender = input("Gender (m, f): ")
        age = int(input("Age: "))
        passanger = {"gender": gender, "age": age}
        self.passagerare.append(passanger)
        self.antal_passagerare += 1
        print("Passanger sitdown to the buss.")

        # Lägg till passagerare. Här skriver man då in ålder men eventuell annan information.
        # Om bussen är full kan inte någon passagerare stiga på

    def print_buss(self):
        print('-' * 40) 
        for passanger in self.passagerare:
            print("Gender:", passanger["gender"], "Age:", passanger["age"])

        print('-' * 40) 
        print("Total passangers:", self.antal_passagerare)
        print('-' * 40) 
        self.calc_average_age()
        print('-' * 40) 
        print("Passanger highest age:", self.max_age())
        print('-' * 40) 
        

    def calc_total_age(self):
        # Beräkna den totala åldern. 
        # För att koden ska fungera att köra så måste denna metod justeras, alternativt att man temporärt sätter metoden med void
        total = 0
        for passanger in self.passagerare:
            total += passanger["age"]
        return total

    # Metoder för betyget C

    def calc_average_age(self):
        # Betyg C
        # Beräkna den genomsnittliga åldern. Kanske kan man tänka sig att denna metod ska returnera något annat värde än heltal?
        # För att koden ska fungera att köra så måste denna metod justeras, alternativt att man temporärt sätter metoden med void
        total = self.calc_total_age()
        ave =  total / self.antal_passagerare
        print(f"Passanger Average: {ave:.2f}")
        return ave


    def max_age(self):
        # Betyg C
        # ta fram den passagerare med högst ålder. Detta ska ske med egen kod och är rätt klurigt.
        # För att koden ska fungera att köra så måste denna metod justeras, alternativt att man temporärt sätter metoden med void
        max_age = 0
        for passanger in self.passagerare:
            passanger_age = passanger["age"]
            if passanger_age > max_age:
                max_age = passanger_age
        return max_age 

    def find_age(self):
        # Visa alla positioner med passagerare med en viss ålder
        # Man kan också söka efter åldersgränser - exempelvis 55 till 67
        # Betyg C
        print("Passanger age: ")
        ages = []
        age = int(input("Enger age: "))
        for passanger in self.passagerare:
            ages.append(passanger["age"])
        try:
            pos = ages.index(age)
        except ValueError:
            pos = "The passanger's age not found."

        return pos 



    def sort_buss(self):
        # Sortera bussen efter ålder. Tänk på att du inte kan ha tomma positioner "mitt i" vektorn.
        #         
    # Man ska kunna sortera vektorn med bubble sort
        pass


    # Metoder för betyget A

    def print_sex(self):
        # Betyg A
        # Denna metod är nödvändigtvis inte svårare än andra metoder men kräver att man skapar en klass för passagerare.
        # Skriv ut vilka positioner som har manliga respektive kvinnliga passagerare.
        pass

    def poke(self):
        # Betyg A
        # Vilken passagerare ska vi peta på?
        # Denna metod är valfri om man vill skoja till det lite, men är också bra ur lärosynpunkt.
        # Denna metod ska anropa en passagerares metod för hur de reagerar om man petar på dom (eng: poke)
        # Som ni kan läsa i projektbeskrivningen så får detta beteende baseras på ålder och kön.
        pass

    def getting_off(self):
        # Betyg A
        # En passagerare kan stiga av
        # Detta gör det svårare vid inmatning av nya passagerare (som sätter sig på första lediga plats)
        # Sortering blir också klurigare
        # Den mest lämpliga lösningen (men kanske inte mest realistisk) är att passagerare bakom den plats..
        # .. som tillhörde den som lämnade bussen, får flytta fram en plats.
        # Då finns aldrig någon tom plats mellan passagerare.
        pass

class Program:
    def __init__(self, *args):
        # Skapar ett objekt av klassen Buss som heter minbuss
        # Denna del av koden kan upplevas väldigt förvirrande. 
    # Men i sådana fall är det bara att "skriva av".
        minbuss = Buss()
        minbuss.run()

        # "press any key to continue" blir lite svårt i python. För att göra detta behövs antingen 
        # en specialgjord funktion eller en "Python module" som hanterar tangenttryck
        # Den enklaste lösningen har jag skrivit nedan, att trycka på enter för att komma vidare
        input("Press Enter to continue . . . ")

# Nedanstående kod är kryptisk. Om ni vill kan ni behålla de raderna.
# Följande kod aktiveras när denna python fil körs
if __name__ == "__main__":
    # skapa en instans (kopia) av klassen Program 
    my_program = Program()
