''' *  Modelos são representações que conectam suas entidades ao banco
    * Utilizando ORMs, eles permitem que você trabalhe com objetos python em vez de SQL
'''
from sqlalchemy import Column, Integer, String 
from src.adapters.database.config.base import Base


class LinksModel(Base):
    __tablename__ = "links"
    
    id = Column(Integer, primary_key= True, index= True, autoincrement= True)
    original_link = Column(String)
    short_link = Column(String)
    
    def __repr__(self):
        return f'Link : {self.original_link}'
