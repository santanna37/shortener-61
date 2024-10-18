from fastapi import APIRouter, Depends, HTTPException
from src.schemas.links_schemas import LinksSchemas
from src.adapters.database.repositories.links_repositories import LinkRepository
from src.adapters.database.database import Database
from src.adapters.services.link_service import LinkService


#criandos as rotas 
router = APIRouter()

# Função de DEpends
def get_link_service_depends(db:Database = Depends()) -> LinkService:
    link_repository = LinkRepository(db)
    return LinkService(link_repository)



@router.post('/postlink')
async def created_short_link(
    original_link:str,
    link_service: LinkService = Depends(get_link_service_depends)):
        try:
            new_link = link_service.build_link(original_link = original_link)
            return {"original_link":new_link.original_link, "short_link": new_link.short_link}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
