# def add_numbers(a: int, b: int) -> int:
#     return a + b


# x = 10
# if isinstance(x, str):
#     print('True')
#
# print(type(x))
#
# if type(x) is int:
#     print('True')


# issubclass
# class MyClass:
#     pass
#
# class MyDerivedClass(MyClass):
#     pass
#
# if issubclass(MyDerivedClass, MyClass):
#     print("MyDerivedClass является подклассом MyClass")

# try:
#     a = 'abcd' + 1
# except ZeroDivisionError:
#     print()

# import pydantic
# from pydantic import BaseModel
#
# class Registration(BaseModel):
#     name: str
#     number: int
#     password: str
# data = {'name': 'Andrey', 'number': 100.5, 'password': 'wertu1'}
# registartion = Registration(**data)
# print(registartion)

# from pydantic import BaseModel, ValidationError
#
# # Определение схемы данных с использованием pydantic
# class Person(BaseModel):
#     name: str
#     age: int
#
# # Пример функции с валидацией
# def process_person_data(person_data):
#     try:
#         # Валидация входных данных
#         person = Person(**person_data)
#     except ValidationError as e:
#         return {"error": str(e)}
#
#     # Выполнение каких-то операций с валидными данными
#     result = f"Привет, {person.name}! Тебе {person.age} лет."
#     return {"result": result}
#
# # Пример использования функции
# data1 = {"name": "John", "age": 30}
# result1 = process_person_data(data1)
# print(result1)
#
# data2 = {"name": "Alice", "age": "twenty"}
# result2 = process_person_data(data2)
# print(result2)

