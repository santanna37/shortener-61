# camada de serviço, onde fica a logica da API 

import pyshorteners
from src.adapters.database.repositories.links_repositories import LinkRepository
from src.adapters.database.models.links_models import LinksModel

class LinkService: 
    def __init__(self, link_repository: LinkRepository):
        self.link_repository = link_repository

    def shorten_link(self, original_link: str) -> str:
        type_tiny = pyshorteners.Shortener()
        short_link = type_tiny.tinyurl.short(original_link)
        return short_link
    
    def build_link(self, original_link: str):
        short_link = self.shorten_link(original_link = original_link)
        new_link = LinksModel(
            original_link = original_link,
            short_link = short_link
        )
        self.link_repository.add_link(new_link)
        return new_link