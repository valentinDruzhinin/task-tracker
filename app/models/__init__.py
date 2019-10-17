from dataclasses import dataclass


class BaseModel:
    def to_dict(self):
        return {k: v for k, v in vars(self).items()}


@dataclass
class TicketModel(BaseModel):
    title: str = None
    creator_id: int = None
    dashboard_id: int = None
    id: int = None
    date_of_creation: str = None
    description: str = None
    assignee: int = None
    status: str = None


@dataclass
class DashboardModel(BaseModel):
    name: str = None
    creator_id: int = None
    id: int = None
    description: int = None
    date_of_creation: str = None
