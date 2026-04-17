from sqlalchemy import *
from sqlalchemy.orm import *
import datetime

class Base(DeclarativeBase):
    pass
engine = create_engine("sqlite:///load.db",echo=False)

class Record(Base):
    __tablename__ = "record"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), index=True)
    time: Mapped[datetime.datetime] = mapped_column(DateTime,default=datetime.datetime.now)
    questions: Mapped[str] = mapped_column(Text)
    answers: Mapped[str] = mapped_column(Text)

    def __repr__(self):
        return f"用户名为{self.name},会话时间为：{self.time},会话内容为:{self.answers},会话问题为：{self.questions}"

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


