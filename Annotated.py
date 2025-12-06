from typing import Annotated
from annotated_types import Gt, Len
from pydantic import BaseModel

class MyClass(BaseModel):
    age: Annotated[int, Gt(18)]                         # Valid: 19, 20, ...
                                                        # Invalid: 17, 18, "19", 19.0, ...
    # factors: list[Annotated[int, Predicate(is_prime)]]  # Valid: 2, 3, 5, 7, 11, ...
                                                        # Invalid: 4, 8, -2, 5.0, "prime", ...

    my_list: Annotated[list[int], Len(0, 10)]

obj=MyClass(age=25, my_list=[1, 2, 3]) 
print(obj)