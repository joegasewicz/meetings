from issue_tracker.models.base import Model
from issue_tracker.models.users import UserModel
from issue_tracker.models.projects import ProjectModel
from issue_tracker.models.statuses import StatusModel
from issue_tracker.models.issues import IssueModel
from issue_tracker.models.standup_notes import StandupNoteModel



tables = [
    UserModel.__table__,
    ProjectModel.__table__,
    StatusModel.__table__,
    IssueModel.__table__,
    StandupNoteModel.__table__
]