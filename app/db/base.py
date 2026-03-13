from app.db.base_class import Base

# Import models here so Alembic can detect them later
from app.models.role import Role
from app.models.user import User, UserRole
from app.models.patient import Patient
from app.models.provider import Provider
from app.models.assignment import PatientProviderAssignment
from app.models.vital import VitalSignRecord
from app.models.activity import ActivityRecord