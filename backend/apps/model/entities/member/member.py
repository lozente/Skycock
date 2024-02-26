from apps.model.entities.entity import Entity


class Member(Entity):
    def __init__(
        self, id: int, nickname: str, phone: str, member_type: str, is_staff: bool
    ) -> None:
        self.id = id
        self.nickname = nickname
        self.phone = phone
        self.member_type = member_type
        self.is_staff = is_staff
