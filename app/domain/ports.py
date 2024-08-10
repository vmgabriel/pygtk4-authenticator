import abc

from app.domain import models


class AuthenticationFinderRepositoryPort(abc.ABC):
    
    @abc.abstractmethod
    def get_by_user(self, user: str) -> models.UserRepository | None:
        raise NotImplementedError()