

from datetime import datetime


class RavindraTask:
    

    def __init__(
        self,
        task_number,
        task_title,
        completion_status=False,
        created_date=None,
    ):
        self.task_number = task_number
        self.task_title = task_title
        self.completion_status = completion_status
        self.created_date = created_date or self.get_current_date()

    def get_current_date(self):
        return datetime.now().strftime("%d-%m-%Y %I:%M %p")

    def mark_completed(self):
        self.completion_status = True

    def get_status_text(self):
        if self.completion_status:
            return "Completed"

        return "Pending"

    def to_dictionary(self):
        return {
            "task_number": self.task_number,
            "task_title": self.task_title,
            "completion_status": self.completion_status,
            "created_date": self.created_date,
        }

    @classmethod
    def from_dictionary(cls, task_data):
        return cls(
            task_number=task_data["task_number"],
            task_title=task_data["task_title"],
            completion_status=task_data["completion_status"],
            created_date=task_data["created_date"],
        )
