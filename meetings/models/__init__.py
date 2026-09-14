from meetings.models.base import Model
from meetings.models.users import UserModel
from meetings.models.projects import ProjectModel
from meetings.models.statuses import StatusModel
from meetings.models.issues import IssueModel
from meetings.models.standup_notes import StandupNoteModel



tables = [
    UserModel.__table__,
    ProjectModel.__table__,
    StatusModel.__table__,
    IssueModel.__table__,
    StandupNoteModel.__table__
]