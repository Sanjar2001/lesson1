#1
def sum(a, b):
    a: int
    b: int
    result1 = {'Your result': a+b}
    print(result1)

sum(2, 3)

def distract(a, b):
    a: int
    b: int
    result2 = {'Your result': a-b}
    print(result2)

distract(2, 3)

def multiply(a, b):
    a: int
    b: int
    print({'Your result': a*b})

multiply(2, 3)

#2
value1 = input('Value1:')
value2 = input('Value2:')
if value1 < value2:
    try:
        print('Good')
    except Exception as e:
        print(e)

#3
from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    name: str
    mail: str
    address: str

class Banks(BaseModel):
    name: str
    rating: int
    opened: Union[int, str]
class Cards(BaseModel):
    cartholder: str
    which_bank: str
    opened: Union[int, str]
class Balance(BaseModel):
    card: int
    amount: int
    currency: str