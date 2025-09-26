from pydantic import BaseModel

class Book(BaseModel):
    title : str
    author : str
    image_url : str
    
class BookRecommendations(BaseModel):
    genre : str
    recommendations: list[Book]

