import dataclasses
import hashlib

from typing import List, Optional

from app.domain import commons


@dataclasses.dataclass
class AuthenticationRequest:
    user: str
    password: str

    @staticmethod
    def create(user: str, password: str) -> "AuthenticationRequest":
        return AuthenticationRequest(
            user=user,
            password=hashlib.sha256(password.encode("utf-8")).hexdigest(),
        )

    def is_valid(self, other: "AuthenticationRequest") -> bool:
        return self.user == other.user and self.password == self.password


@dataclasses.dataclass
class UserRepository:
    user: str
    name: str
    last_name: str
    authentication: AuthenticationRequest

    def is_authenticated(self, other: AuthenticationRequest) -> bool:
        return self.authentication.is_valid(other=other)


@dataclasses.dataclass
class AuthenticationResponse:
    authenticated: bool = False
    user: Optional[UserRepository] = None
    errors: List[commons.Error] = dataclasses.field(default_factory=list)