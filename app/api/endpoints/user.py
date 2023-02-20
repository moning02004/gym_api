from fastapi import APIRouter

from app import schemas, cruds

router = APIRouter()


@router.get(path="/{_id}", status_code=200, response_model=schemas.UserDetail)
def get_item(_id: int):
    return cruds.get_user(_id)


@router.post(path="", status_code=201, response_model=schemas.UserDetail | schemas.NotFoundSchema)
def post_item(_in: schemas.UserCreate):
    if cruds.find_user_by_username(_in.username):
        return {
            "message": "already"
        }
    result = cruds.create_user(_in)
    return result
