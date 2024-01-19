from collections import UserDict
from datetime import date, datetime, timedelta
from random import randint
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.__value)
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    pass


class Phone(Field):
    # def __init__(self, value):
    #     if len(value) != 10 or re.search(r"\D", value):
    #         raise ValueError("Incorrect phone number format")
    #     super().__init__(value)
    @Field.value.setter
    def value(self, new_value):
        if len(new_value) != 10 or re.search(r"\D", new_value):
            raise ValueError("Incorrect phone number format")
        Field.value.fset(self, new_value)


class Birthday(Field):
    @Field.value.setter
    def value(self, new_value):
        try:
            birthday = datetime.strptime(new_value, "%d.%m.%Y")
        except:
            raise ValueError("Incorrect birthday data format. Please use dd.mm.yyyy pattern")
        if birthday > datetime.today():
            raise ValueError(f"Birthday date '{new_value}' is in the future")
        Field.value.fset(self, birthday)
    
    def __str__(self):
        return str(self.value.strftime("%d.%m.%Y"))


class Record:
    def __init__(self, name, birthday = None):
        self.name = Name(name)
        self.phones = []
        if birthday is not None:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, rm_phone):
        for phone in self.phones:
            if phone.value == rm_phone:
                self.phones.remove(phone)
                return
        raise ValueError(f'Phone "{rm_phone}" does not exist')

    def edit_phone(self, old_phone, new_phone):
        for i, _ in enumerate(self.phones):
            if self.phones[i].value == old_phone:
                self.phones[i].value = new_phone
                return
        raise ValueError(f'Phone "{old_phone}" does not exist')

    def find_phone(self, find_phone):
        for phone in self.phones:
            if phone.value == find_phone:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, " \
            f"phones: {'; '.join(p.value for p in self.phones)}, " \
            f"birthday: {self.birthday}"
    
    def days_to_birthday(self):
        if self.birthday is None:
            return None
        
        today = datetime.today()
        # truncating hours, minutes etc.
        today = today.replace(hour=0, minute=0, second=0, microsecond=0)

        current_year = int(today.strftime("%Y"))
        this_year_bday = self.birthday.value.replace(year=current_year)

        if this_year_bday < today:
            this_year_bday = self.birthday.value.replace(year=current_year + 1)

        delta = this_year_bday - today
        return delta.days


class AddressBook(UserDict):
    def add_record(self, record):
        name = record.name.value
        if self.data.get(name):
            raise ValueError(f'Name "{name}" already exist')
        self.data[name] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if self.data.get(name):
            self.data.pop(name)
    
    def iterator(self, n=1):
        if n <= 0:
            raise ValueError("Incorrect N value. N shuld be greater than 0")
        output = {}
        for index, (key, val) in enumerate(self.data.items()):
            output[key] = val
            if (index + 1) % n == 0:
                yield output
                output = {}
        if output:
            yield output



# remove me!!!
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john.days_to_birthday())

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
book.delete("John")

print(str(randint(1111111111, 9999999999)))
name_list = ["Flora", "Jimmy", "Madilyn", "Roland", "Presley", "Lorenzo", "Phoenix", "Jay",
             "Catherine", "Javier", "Julia", "Zechariah", "Blake", "Royal", "Brooke", "Raylan",
              "Kathryn", "Brayden", "Clementine", "John", "Viviana", "Emir", "Ariyah", "Saint",
              "Lauryn", "Koda", "Nylah", "Jamal", "Irene", "Colten", "Katelyn", "Frederick", "Sloane",
              "Princeton", "Emily", "Abraham", "Dallas", "Jayce", "Kayleigh", "Oliver", "Raelyn", "Milan",
              "Kennedy", "Colin", "Anaya", "Michael", "Jayda", "Baylor", "Thea", "Bryan", "Everleigh",
              "Rohan", "Alma", "Eugene", "Avayah", "Riley", "Faye", "Kiaan", "Berkley", "Franco",
              "Nyomi", "Harrison", "Rylan", "Sawyer", "Julieta", "Amari", "Selena", "Hamza", "Linda",
              "Pablo", "Rebekah", "Grayson", "Addilyn", "Jeremiah", "Taylor", "William", "Kaydence",
              "Valentin", "Noa", "Alonso", "Delilah", "Leighton", "Araceli", "Dalton", "Charleigh", "Adan",
              "Joelle", "Ayden", "Giuliana", "Mordechai", "Rose", "Seth", "Paityn", "Adonis", "Ember", "Kabir",
              ]

birthday_list = ["24.12.2023", "09.03.2003", "07.07.2002", "20.09.1993", "22.11.2015", "27.02.2017", "28.01.2018",
                 "08.07.2014", "13.09.2022", "17.08.2001", "26.08.1988", "16.04.1986", "25.06.2013", "02.12.1989",
                 "25.01.1999", "03.03.2015", "05.10.1989", "07.11.2008", "10.08.2003", "04.08.2000", "18.05.1999",
                 "19.08.1987", "14.07.1990", "08.04.1983", "31.12.2014", "05.01.2019", "19.06.2012", "09.09.2014",
                 "20.11.2006", "31.03.2015", "04.12.1998", "04.12.2005", "30.09.2012", "29.09.2007", "23.09.1980",
                 "15.08.1998", "27.04.2015", "25.01.2001", "08.03.1998", "04.11.2014", "21.07.1991", "03.11.1984",
                 "26.02.2003", "29.06.2014", "10.01.1995", "25.10.1982", "15.06.1983", "17.04.2005", "13.11.2016",
                 "13.07.1987", "12.08.2002", "05.05.2009", "16.05.1985", "14.02.1984", "16.12.2013", "15.02.1995",
                 "17.04.2012", "18.02.1990", "13.12.2020", "01.11.2006", "06.09.2018", "05.10.2001", "04.11.1993",
                 "20.10.1985", "11.12.2003", "12.10.2009", "02.01.1998", "11.04.2018", "27.03.2019", "23.01.1996",
                 "14.08.2019", "13.08.2000", "16.07.2013", "30.06.1990", "17.02.2008", "08.01.1991", "24.08.1999",
                 "11.06.1986", "13.11.2013", "10.06.2012", "07.03.1991", "06.08.1983", "10.11.1997", "25.10.1983",
                 "26.06.1994", "22.03.1980", "01.12.1995", "28.08.1994", "12.11.1985", "14.08.2014", "17.07.2012",
                 "01.04.1982", "08.05.1997", "27.12.1992", "06.10.2015", "22.01.1996", "29.08.1980", "30.07.2015", 
                 "29.05.1997", "12.08.1986", "20.06.2000", "11.12.2011", "26.10.2012", "26.01.2008", "01.11.2012",
                 "07.06.1980", "26.08.2005", "24.06.1980", "31.08.2016", "22.07.2004", "15.11.2003", "04.07.1981",
                 "16.07.2007", "31.08.2021", "06.01.2003", "05.04.1988", "12.02.2022", "25.11.2017", "18.09.2019",
                 "20.08.1996", "22.11.2008", "18.05.1984", "03.11.1996", "11.09.1996", "17.06.1995", "23.06.1987",
                 "29.12.2014", "14.03.2014", "20.02.2020", "12.09.1990", "08.10.1994", "29.12.2014", "23.11.2007",
                 "20.04.2009", "25.06.2012", "21.05.2004", "11.05.1991", "25.06.2018", "17.03.2007", "26.08.1989",
                 "04.04.1981", "15.09.2020", "29.11.1985", "23.02.1993", "28.01.1997", "20.02.1996", "24.05.1983",
                 "26.08.2023", "06.04.1991", "05.10.2017", "20.04.2016", "08.01.1996", "26.02.2005", "06.11.2020",
                 "01.12.1985", "19.08.2016", "10.12.1998", "04.03.1980", "07.09.2008", "26.11.1989", "08.03.2018",
                 "07.10.1993", "07.01.1996", "17.04.2010", "08.03.1982", "27.09.1985", "09.03.2001", "17.11.1985",
                 "07.05.1992", "09.03.1993", "18.09.1986", "02.04.2015", "31.05.2004", "05.08.1983", "24.11.2012",
                 "01.04.2020", "02.11.2004", "25.10.2020", "20.08.1997", "15.01.1989", "26.04.1991", "26.04.1984",
                 "24.11.2016", "18.08.1996", "02.04.1986", "19.10.1987", "05.08.1981", "02.12.2014", "07.01.2010",
                 "21.09.1982", "16.10.2015", "07.08.2007"
                 ]

for i, curr_name in enumerate(name_list):
    record = Record(curr_name, birthday=birthday_list[i])
    for j in range (randint(1,3)):
        record.add_phone(str(randint(1111111111, 9999999999)))
    book.add_record(record)

# record = Record("Test")
# record.add_phone("242")
# record.add_phone("1234567a90")

# book.add_record(record)

for name, record in book.data.items():
    print(record)

# datetime.today()

record = book.find("John")
print(record)
print(record.birthday)
# record.birthday.value = "24.12.2000"
print(record.days_to_birthday())

for i in book.iterator(7):
    print(len(i))