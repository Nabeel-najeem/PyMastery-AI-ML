from pydantic import BaseModel

class products(BaseModel):
    id :int
    product_name : str
    description : str
    price : float
    quantity : int

    