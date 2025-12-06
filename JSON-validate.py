from pydantic import BaseModel

class MyClass(BaseModel):
    age: int
    name:str
    is_student: bool
    id:dict[str,int]


d={
    "age": 30,
    "name": "Bob",
    "is_student": True,
    "id": {
        "college":5431,
        "employee_id":7211
    },

}
obj=MyClass(**d)
print(obj.id["college"])
