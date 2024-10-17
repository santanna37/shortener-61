from fastapi import APIRouter, Depends, status
from src.schemas.links_schemas import LinksSchemas
from src.adapters.database.repositories.links_repositories import LinkRepository
from src.adapters.database.database import Database


#criandos as rotas 
router = APIRouter()
