from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Text

from datetime import datetime

from app.database.database import Base


class Generation(Base):

    __tablename__ = "generations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    generation_type = Column(
        String,
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )

    document_name = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

class Document(Base):

    __tablename__ = "documents"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(
        String,
        nullable=False
    )

    filepath = Column(
        String,
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=False
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )