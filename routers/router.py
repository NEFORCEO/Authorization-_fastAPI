from fastapi import APIRouter, Response
from sqlalchemy import select

from database.models.model import SessionDep
from database.db import RegLog
from schemas.param_schemas.param_schema import ParamObj
from schemas.return_schemas.return_schema import Error, GetResponse, Login, RegLogSchema, Register


router = APIRouter()


@router.get('/db', response_model=GetResponse)
async def db_result(db: SessionDep):
    res = await db.execute(select(RegLog))
    data = res.scalars().all()
    if data:
        # Преобразуем объекты RegLog в RegLogSchema
        result = [RegLogSchema.model_validate(user) for user in data]
        return GetResponse(
            status=200,
            result=result
        )
    else:
        return Response(
            status_code=404,
            content="Возмжно база данных пустая"
        )
        
@router.post('/register', response_model=Register)
async def register(param: ParamObj, db: SessionDep):
    result = await db.execute(select(RegLog).filter(RegLog.name == param.name))
    ext = result.scalar_one_or_none()
    if ext:
        return Response(
            status_code=409,
            content="Пользователь с данным именем уже существует"
        )
    # Преобразуем пароль в строку для сохранения в базу
    new_password = bin(param.password)[2:]
    new_user = RegLog(name=param.name, password=new_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return Register(
        id=new_user.id,
        name=new_user.name,
        password=param.password
    )
    
@router.post('/login')
async def login(param: ParamObj, db: SessionDep):
    result = await db.execute(select(RegLog).filter(RegLog.name == param.name))
    ext = result.scalar_one_or_none()
    if ext:
        if int(bin(param.password)[2:]) == ext.password:
            return Login(
                password=param.password,
                result=True
            )
        else:
            return Error(message="Неверный пароль")
    else:
        return Response(
            status_code=404,
            content="Придумаю позже"
        )