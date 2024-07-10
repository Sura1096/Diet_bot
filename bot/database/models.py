from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base


class Users(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(index=True)


class Questions(Base):
    __tablename__ = 'questions'

    question_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True, autoincrement=True)
    question: Mapped[str]


class Form(Base):
    __tablename__ = 'form'

    form_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    question_id: Mapped[int] = mapped_column(ForeignKey('questions.question_id'))
    answer: Mapped[str]
    user_relationship = relationship('Users')
    question_relationship = relationship('Questions')
