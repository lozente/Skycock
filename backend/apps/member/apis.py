from apps.model.DTO.member import MemberDTO, ScoreRecordDTO
from apps.model.entities.member.member import Member


def get_members_by_id(member_ids: list[int]) -> list[Member]:
    member_dto_list = MemberDTO.query.filter(MemberDTO.id.in_(member_ids)).all()
    member_list = [Member.from_dto(member_dto) for member_dto in member_dto_list]
    return member_list


def get_member_dict_by_score(quarter: str) -> dict[int, Member]:
    score_record = ScoreRecordDTO.query.filter(ScoreRecordDTO.quarter == quarter)
