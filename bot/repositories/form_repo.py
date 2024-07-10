from ..database.models import Users, Questions, Form
from .base_repo import UsersRepo, QuestionsRepo, FillFormRepo


class UsersRepository(UsersRepo):
    model = Users


class QuestionsRepository(QuestionsRepo):
    model = Questions


class FormRepository(FillFormRepo):
    model = Form
