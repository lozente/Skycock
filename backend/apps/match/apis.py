# from app import db
# from apps.match.match_maker import REGULAR_EVENT_MATCH_MAKING_MAP_BY_RANK
# from apps.member import apis as member_apis
# from apps.model import constants
# from apps.model.DTO.event import EventDTO
# from apps.model.DTO.match import MatchDTO


# def create_event(
#     event_type: str, event_status: str, participant_ids: list[int]
# ) -> EventDTO:
#     new_event = EventDTO()
#     new_event.event_type = event_type
#     new_event.status = event_status
#     new_event.participants = member_apis.get_members_by_ids(participant_ids)

#     db.session.add(new_event)
#     db.session.commit()

#     return new_event


# def create_matches(event: EventDTO) -> list[MatchDTO]:
#     if event.event_type == constants.EVENT_TYPE__REGULAR:
#         pass
#     else:
#         raise NotImplementedError("Non-regular event match creation is not implemented")
