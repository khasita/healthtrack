import uuid
from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class ActivityRecord(Base):
    __tablename__ = "activity_records"
    __table_args__ = (
        CheckConstraint("steps >= 0", name="ck_activity_steps_nonnegative"),
        CheckConstraint("distance_km >= 0", name="ck_activity_distance_nonnegative"),
        CheckConstraint(
            "calories_burned >= 0", name="ck_activity_calories_nonnegative"
        ),
        CheckConstraint("active_minutes >= 0", name="ck_activity_minutes_nonnegative"),
        Index("ix_activity_records_patient_recorded_at", "patient_id", "recorded_at"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    patient_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("patients.id", ondelete="CASCADE"),
        nullable=False,
    )
    steps: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    distance_km: Mapped[float] = mapped_column(
        Numeric(10, 2), default=0, nullable=False
    )
    calories_burned: Mapped[float] = mapped_column(
        Numeric(10, 2), default=0, nullable=False
    )
    active_minutes: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    recorded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    patient = relationship("Patient", back_populates="activities")
