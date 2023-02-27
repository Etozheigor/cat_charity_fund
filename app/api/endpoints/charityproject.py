from fastapi import APIRouter, Depends
from app.core.user import current_user, current_superuser
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.db import get_async_session
from app.schemas.charityproject import CharityProjectDB, CharityProjectCreateUpdate
from app.crud.charityproject import charity_project_crud

router = APIRouter()

@router.get(
    '/charity_project',
    response_model=List[CharityProjectDB],
    response_model_exclude_none=True,
    description='Получает список всех проектов'
)
async def get_all_charity_projects(session: AsyncSession = Depends(get_async_session)):
    all_charity_projects = await charity_project_crud.get_multi(session)
    return all_charity_projects

@router.post(
    '/charity_project',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    description='Создает благотворительный проект.'
    )
async def create_charity_project(
    charity_project: CharityProjectCreateUpdate, 
    session: AsyncSession = Depends(get_async_session)):
    new_charity_project = await charity_project_crud.create(charity_project, session)
    return new_charity_project

@router.patch(
    '/charity_project/{project_id}', 
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    description=('Закрытый проект нельзя редактировать, также нельзя ' 
                 'установить требуемую сумму меньше уже вложенной.'))
async def update_chariry_project(
    project_id: int,
    obj_in: CharityProjectCreateUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    charity_project = await charity_project_crud.get(project_id, session)
    charity_project = await charity_project_crud.update(charity_project, obj_in, session)
    return charity_project

@router.delete(
    '/charity_project/{project_id}', 
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    description=('Удаляет проект. Нельзя удалить проект, в который уже ' 
                 'были инвестированы средства, его можно только закрыть.'))
async def delete_charity_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session)
):  
    charity_project = await charity_project_crud.get(project_id, session)
    charity_project = await charity_project_crud.remove(charity_project, session)
    return charity_project

