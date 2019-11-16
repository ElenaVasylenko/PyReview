from abc import ABC, abstractmethod
from datetime import date


class Employee(ABC):

    def __init__(self, doc_id: str, name: str, birthday: str):
        self.__doc_id = doc_id
        self.name = name
        self.birthday = birthday
        print('employee created')

    @abstractmethod
    def get_duties(self):
        pass

    @abstractmethod
    def get_contract(self):
        pass


class Engineer(Employee):

    def __init__(self, grade, doc_id: str, name: str, birthday: str):
        self.__grade = grade
        super().__init__(doc_id, name, birthday)
        print('engineer created')

    def get_duties(self):
        print('engineer duties')
        return 'engineer duties'

    def get_contract(self):
        print('engineer contract')
        return 'engineer contract'


class BackendSWE(Engineer):

    def __init__(self, grade: str, doc_id: str, name: str, birthday: str, programming_language: str):
        self.__salary = 2000
        self.programming_language = programming_language
        super().__init__(grade, doc_id, name, birthday)
        print('backend swe created')

    def get_duties(self):
        print('backend swe duties')
        return 'backend swe duties'

    def get_contract(self):
        print('backend swe contract')
        return 'backend swe contract'


swe = BackendSWE(grade='middle', doc_id='fb541509', name='olena',
                 birthday='18.03.98', programming_language='python')

swe.get_duties()
swe.get_contract()
# access private variable of child class
print(swe._BackendSWE__salary)
print(swe._Engineer__grade)
print(swe._Employee__doc_id)


# _MangledGlobal__mangled = 23
#
# class MangledGlobal:
#     def test(self):
#         return __mangled
#
# >>> MangledGlobal().test()
# 23