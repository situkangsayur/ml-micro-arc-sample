from app.database import Base
from sqlalchemy import TIMESTAMP, Column, String, Column, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
import uuid

class Model(Base):

    __tablename__ = 'tb_model'
    id = Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    model_name = Column(String(100))
    method_detail = Column(JSONB) 
    model = Column(JSONB)
    preprocessing = Column(JSONB)
    feature_seq = Column(JSONB)
    version = Column(String) 
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

