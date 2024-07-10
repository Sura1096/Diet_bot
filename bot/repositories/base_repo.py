from abc import ABC, abstractmethod

from sqlalchemy import select, update, insert
from sqlalchemy.sql import and_
from sqlalchemy.ext.asyncio import AsyncSession


class UsersAbstractRepo(ABC):
    @abstractmethod
    async def get_user(self, telegram_id):
        raise NotImplementedError

    @abstractmethod
    async def insert_user(self, telegram_id):
        raise NotImplementedError


class QuestionsAbstractRepo(ABC):
    @abstractmethod
    async def get_questions(self):
        pass

    @abstractmethod
    async def insert_question(self, question):
        pass


class FillFormAbstractRepo(ABC):
    @abstractmethod
    async def insert_new_user_form(self, user_id, form):
        pass

    @abstractmethod
    async def update_user_form(self, user_id, form):
        pass


class UsersRepo(UsersAbstractRepo):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user(self, telegram_id):
        stmt = select(self.model).where(self.model.telegram_id == telegram_id)
        user = await self.session.execute(stmt)
        result = user.scalar_one_or_none()
        if not result:
            return None
        return result.user_id

    async def insert_user(self, telegram_id):
        await self.session.execute(insert(self.model).values(telegram_id=telegram_id))


class QuestionsRepo(QuestionsAbstractRepo):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_questions(self):
        questions = await self.session.execute(select(self.model))
        result = questions.scalars().all()
        if result:
            return result
        return None

    async def insert_question(self, question):
        await self.session.execute(insert(self.model).values(question=question))


class FillFormRepo(FillFormAbstractRepo):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert_new_user_form(self, user_id, form):
        for question_number, answer in enumerate(form.values(), start=1):
            await self.session.execute(insert(self.model).values(
                user_id=user_id,
                question_id=question_number,
                answer=answer
            ))

    async def update_user_form(self, user_id, form):
        for question_number, answer in enumerate(form.values(), start=1):
            await self.session.execute(
                update(self.model).where(and_(
                    self.model.user_id == user_id,
                    self.model.question_id == question_number
                )).values(
                    answer=answer
                )
            )

