from abc import ABC, abstractclassmethod


class Entity(ABC):
    @abstractclassmethod
    def from_dto(cls, instance):
        return cls(**instance.__dict__)
