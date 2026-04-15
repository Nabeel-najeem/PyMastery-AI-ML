from pydantic import BaseModel

class product(BaseModel):
    id :int
    product_name : str
    description : str
    price : float
    quantity : int

    