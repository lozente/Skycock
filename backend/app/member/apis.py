from backend.app.model.member import MemberDTO


def get_members_by_ids(member_ids: list[int]) -> list[MemberDTO]:
    return MemberDTO.query.filter(MemberDTO.id.in_(member_ids)).all()
