# Repositorio - Responsavel pela manipulação do banco de dados 

from adapters.database.database import Database
from src.schemas.links_schemas import LinksSchemas 
from src.adapters.database.models.links_models import LinksModel



class LinkRepository:
    def __init__(self, database:Database):
        self.database = database

    def add_link(self, link: LinksModel):
        with self.database as db:
            db.add(link)

    def get_link(self, original_link):
        with self.database as db:
            return db.get(LinksModel,original_link = original_link)
