from datetime import datetime

from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped

from app.model.base import Base


class Member(Base):
    __tablename__ = 'member'
    __table_args__ = {'sqlite_autoincrement': True}

    mno: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, index=True)
    userid: Mapped[str] = mapped_column(String(18), unique=True, nullable=False, index=True)  # 식별관계
    # userid: Mapped[str] = mapped_column(index=True)  # 비식별관계
    passwd: Mapped[str] = mapped_column(String(18))
    name: Mapped[str] = mapped_column(String(10))
    email: Mapped[str] = mapped_column(String(100))
    regdate: Mapped[datetime] = mapped_column(default=datetime.now)










