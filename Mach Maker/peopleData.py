class Person(object):
    def __init__(self, sex, age, job, maried_before, kids, economic_status, desired_person = '', name = ''):
        self.name = name
        self.sex = sex
        self.age = age
        self.job = job
        self.maried_before = maried_before
        self.kids = kids
        self.economic_status =economic_status
        self.desired_person = desired_person #Person object constructed based on the prefernce of this person object


Abel = Person("Male", 22, False, "Employed", 0, "Independent")
AbelDesired = Person("Female", 18, False, "Employed", 0, "Independent")
Abel.desired_person = AbelDesired
Abel.name = "Abel Asefa"

Yewhanis = Person("Male", 30, True, "Employed", 2, "Independent")
YewhanisDesired = Person("Female", 24, False, "Employed", 0, "Independent")
Yewhanis.desired_person = YewhanisDesired
Yewhanis.name = "Yewhanis Yilma"

Tadael = Person("Male", 30, True, "Employed", 1, "Independent")
TadaelDesired = Person("Female", 26, True, "Employed", 1, "Independent")
Tadael.desired_person = TadaelDesired
Tadael.name = "Tadael Xilahun"

Meron = Person("Female", 19, False, "Unemployed", 0, "Dependent")
MeronDesired = Person("Male", 22, False, "Unemployed", 0, "Dependent")
Meron.desired_person = MeronDesired
Meron.name = "Meron Getnet"

Zehara = Person("Female", 22, False, "Unemployed", 0, "Dependent")
ZeharaDesired = Person("Male", 26, False, "Employed", 0, "Independent")
Zehara.desired_person = ZeharaDesired
Zehara.name = "Zehara Mokeni"

list_of_people = [Abel, Yewhanis, Tadael, Meron, Zehara] #People who have subscribed and looking for match

Hana = Person("Female", 26, True, "Employed", 1, "Independent", )
HanaDesired = Person("Male", 30, True, "Employed", 1, "Independent")
Hana.desired_person = HanaDesired
Hana.name = "Hana Asefa"