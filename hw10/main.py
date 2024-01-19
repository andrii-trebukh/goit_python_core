from collections import UserDict
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or re.search(r"\D", value):
            raise ValueError("Incorrect phone number format")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

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
            "phones: {'; '.join(p.value for p in self.phones)}"


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
