# Schemas -  Recebe os Dados do Requests(BD) - contruir o BD primeiro 

from pydantic import BaseModel

class LinksSchemas(BaseModel): 
    id: int 
    original_link: str 
    short_link: str 

    class config:
        orm_mode = True
