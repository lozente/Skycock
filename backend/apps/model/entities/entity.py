from abc import ABC, ABCMeta

from flask_sqlalchemy.model import Model

from apps.model.db import db


class EntityMeta(ABCMeta):
    def __new__(cls, name, bases, dct):
        if name != "Entity" and "dto_class" not in dct:
            raise TypeError(f"Class {name} must define a 'dto_class' attribute.")
        return super().__new__(cls, name, bases, dct)


class Entity(ABC, metaclass=EntityMeta):
    dto_class: Model

    @classmethod
    def from_dto(cls, instance):
        filtered_attributes = {
            key: value
            for key, value in instance.__dict__.items()
            if not key.startswith("_")
        }
        return cls(**filtered_attributes)

    # def get_dto(self):
    #     id = getattr(self, "id", None)
    #     if id is None:
    #         raise RuntimeError("The object does not have an id.")
    #     return self.dto_class.query.get(id)

    def create_dto(self):
        dto_instance = self.dto_class()
        for attribute in dir(self.dto_class):
            if not attribute.startswith("_") and not callable(
                getattr(self.dto_class, attribute)
            ):
                setattr(dto_instance, attribute, getattr(self, attribute, None))

        return dto_instance

    def save(self):
        dto = self.create_dto()
        db.session.add(dto)
        db.session.commit()

    @classmethod
    def bulk_save(cls, obj_list):
        dto_list = [obj.create_dto() for obj in obj_list]
        db.session.bulk_save_objects(dto_list)
        db.session.commit()
