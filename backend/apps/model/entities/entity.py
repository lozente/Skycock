from abc import ABC

from apps.model.db import db


class Entity(ABC):
    @classmethod
    def from_dto(cls, instance):
        return cls(**instance.__dict__)

    def to_dto(self, dto_class):
        dto_instance = dto_class()

        for attribute in dir(dto_class):
            if not attribute.startswith("_") and not callable(
                getattr(dto_class, attribute)
            ):
                setattr(dto_instance, attribute, getattr(self, attribute, None))

        return dto_instance

    def save(self):
        dto = self.to_dto()
        db.session.add(dto)
        db.session.commit()

    @classmethod
    def bulk_save(cls, obj_list):
        dto_list = [obj.to_dto() for obj in obj_list]
        db.session.bulk_save_objects(dto_list)
        db.session.commit()
