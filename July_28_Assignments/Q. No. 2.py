# Program to print nationality based on the input surname using static method


class Nepal:
    @staticmethod
    def print_Nationality(surname):
        surname_file = open("surnames_en.csv", 'r')
        surnames = surname_file.readlines()
        for i in surnames:
            if surname.upper() in i:
                print("Nepali")
                break;
        else:
            print("Foreign")


Nepal.print_Nationality(input("Enter your surname:"))



