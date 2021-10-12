import random


class BillSplitter:
    def __init__(self):
        self.number_of_people = 0
        self.people_dictionary = {}
        self.total_bill = 0

    def main(self):
        self.check_number_of_people()
        self.create_the_people_dictionary()
        self.split_the_bill()
        self.select_the_lucky_person()
        print(self.people_dictionary)

    def check_number_of_people(self):
        try:
            self.number_of_people = int(input("Enter the number of friends joining (including you):""\n"))
            assert self.number_of_people > 0
        except (ValueError, AssertionError):
            print("\n""No one is joining for the party")
            exit()

    def create_the_people_dictionary(self):
        print("\n""Enter the name of every friend (including you), each on a new line:")
        self.people_dictionary = {input(): 0 for _ in range(self.number_of_people)}
        self.total_bill = int(input("\n""Enter the total bill value:""\n"))

    def split_the_bill(self):
        self.people_dictionary = dict.fromkeys(self.people_dictionary,
                                               round((self.total_bill / self.number_of_people), 2))

    def select_the_lucky_person(self):
        try:
            lucky_feature = input('\n''Do you want to use the "Who is lucky?" feature? Write Yes/No:''\n').lower()
            assert lucky_feature == 'yes'
        except (ValueError, AssertionError):
            print('\n''No one is going to be lucky''\n')
        else:
            lucky_person = random.choice(list(self.people_dictionary.keys()))
            print('\n'f'{lucky_person} is the lucky one!''\n')
            del self.people_dictionary[lucky_person]
            self.number_of_people -= 1
            self.split_the_bill()
            self.people_dictionary.update({lucky_person: 0})


if __name__ == '__main__':
    BillSplitter().main()