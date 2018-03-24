'''
 * Name: Elias Andualem
 * Id: ATR/9391/08
 * Architectural Pattern : Pipe and Filter
 * Description: I have tried to show the implementation of pipe and filter Architectural Pattern by using
   a simple matching application which filters people from the total list based of the person specification.
 * Simple data to show the application running is stored in PeopleData.py python file so it has to be in the
   same folder
'''

import peopleData


class SexFilter():
    def __init__(self, person, list_of_people):
        self.person = person
        self.list_of_people = list_of_people
        self.required_sex_people = []


    def find_sex_mach(self):

        for i in self.list_of_people:
            if (i.sex == self.person.desired_person.sex):
                self.required_sex_people.append(i)

        return self.required_sex_people


class PrefenceFilter():
    def __init__(self, person, required_sex_people):
        self.person = person
        self.required_sex_people = required_sex_people
        self.people_fitting_criteria = []

    def their_choising(self):# Select those fitting her/his preference

        for i in self.required_sex_people:

            if (i.age == self.person.desired_person.age and i.job == self.person.desired_person.job and
                i.maried_before == self.person.desired_person.maried_before and i.kids == self.person.desired_person.kids and
                i.economic_status == self.person.desired_person.economic_status):

                self.people_fitting_criteria.append(i)

        return self.people_fitting_criteria


class QualityFilter():
    def __init__(self, person, people_fitting_criteria):
        self.person = person
        self.people_fitting_criteria = people_fitting_criteria
        self.match = []

    def who_likes_them(self): #From people matching their preference those looking for this (the searching persons) qualities

        for i in self.people_fitting_criteria:
            if (i.desired_person.age == self.person.age and i.desired_person.job == self.person.job and
                i.desired_person.maried_before == self.person.maried_before and i.desired_person.kids == self.person.kids and
                i.desired_person.economic_status == self.person.economic_status):

                self.match.append(i)

        return self.match


if __name__ == "__main__":
    print("\t*********************************************************************************")
    print("\t***  Matching  - Showing the implimentation of pipe and filter architecture!  ***")
    print("\t*********************************************************************************\n")

    #
    pipe = SexFilter(peopleData.Hana, peopleData.list_of_people).find_sex_mach()
    pipe = PrefenceFilter(peopleData.Hana, pipe).their_choising()
    Sink = QualityFilter(peopleData.Hana, pipe).who_likes_them()

    print("\tMatching people for ",peopleData.Hana.name, "are:" )

    for i in Sink:
        print("\n\t\t1:", i.name, "\n")

