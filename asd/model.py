from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class UsersOrm(Base):
    __tablename__ = "users" 

    id: Mapped[int] = mapped_column(primary_key=True)