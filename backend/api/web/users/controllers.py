import http

from fastapi import Response

from api.web.exceptions import NotAuthenticated
from api.web.routing import APIRouter
from api.web.users.service import AnnotatedUser, Password, PasswdContext

router = APIRouter()


@router.post("/login")
async def login(
        response: Response,
        password: Password,
        user: AnnotatedUser,
        passwd_context: PasswdContext,
):
    if not user or not passwd_context.verify(password, user.password):
        raise NotAuthenticated(detail="Invalid login or password")
    response.headers["X-Authenticated"] = user.id
    response.status_code = http.HTTPStatus.ACCEPTED
    return response
