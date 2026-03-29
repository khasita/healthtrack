from app.db.base_class import Base as Base

# Import models so Alembic can detect them
from app.models.role import Role  # noqa: F401
from app.models.user import User, UserRole  # noqa: F401
from app.models.patient import Patient  # noqa: F401
from app.models.provider import Provider  # noqa: F401
from app.models.assignment import PatientProviderAssignment  # noqa: F401
from app.models.vital import VitalSignRecord  # noqa: F401
from app.models.activity import ActivityRecord  # noqa: F401
