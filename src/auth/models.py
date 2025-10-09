from sqlmodel import SQLModel, Field, Column
from datetime import datetime, timezone
import sqlalchemy.dialects.postgresql as pg
import uuid



class User(SQLModel, table=True):
    __tablename__ = "users"

    uid: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(pg.UUID(as_uuid=True), primary_key=True, nullable=False),
    )

    username: str = Field(sa_column=Column(pg.VARCHAR, nullable=False))
    email: str = Field(sa_column=Column(pg.VARCHAR, nullable=False, unique=True))
    first_name: str = Field(sa_column=Column(pg.VARCHAR, nullable=True))
    last_name: str = Field(sa_column=Column(pg.VARCHAR, nullable=True))
    is_verified: bool = Field(
        default=False, sa_column=Column(pg.BOOLEAN, default=False)
    )
    password_hash: str = Field(
        exclude=True, sa_column=Column(pg.VARCHAR, nullable=False)
    )

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(
            pg.TIMESTAMP(timezone=True), default=lambda: datetime.now(timezone.utc)
        ),
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(
            pg.TIMESTAMP(timezone=True), default=lambda: datetime.now(timezone.utc)
        ),
    )

    def __repr__(self) -> str:
        return f"<User {self.username}>"
