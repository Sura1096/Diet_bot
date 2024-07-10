from ..utils.unitofwork import IUnitOfWork


class UsersService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def get_user_id(self, telegram_id):
        async with self.uow:
            user_id_from_db = await self.uow.users.get_user(telegram_id)
            await self.uow.commit()
            return user_id_from_db

    async def insert_user_id(self, telegram_id):
        async with self.uow:
            await self.uow.users.insert_user(telegram_id)
            await self.uow.commit()


class QuestionsService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def get_questions_list(self):
        async with self.uow:
            questions = await self.uow.questions.get_questions()
            await self.uow.commit()
            return questions

    async def insert_new_question(self, question):
        async with self.uow:
            await self.uow.questions.insert_question(question)
            await self.uow.commit()


class FormService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def insert_new_form(self, user_id, form):
        async with self.uow:
            await self.uow.form.insert_new_user_form(user_id, form)
            await self.uow.commit()

    async def update_form(self, user_id, form):
        async with self.uow:
            await self.uow.form.update_user_form(user_id, form)
            await self.uow.commit()
