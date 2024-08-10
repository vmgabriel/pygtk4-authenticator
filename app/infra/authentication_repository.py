import dotenv
import os

from app.domain import models, ports


dotenv.load_dotenv()


_DB = [
    models.UserRepository(
        user="vmgabriel", 
        name="Gabriel",
        last_name="Vargas",
        authentication=models.AuthenticationRequest.create(
            user=os.getenv("USER", ""),
            password=os.getenv("PASSWORD", ""),
        )
    )
]


class AuthenticationFinderAdapter(ports.AuthenticationFinderRepositoryPort):
    def get_by_user(self, user: str) -> models.UserRepository | None:
        data = filter(lambda db_user: db_user.user == user, _DB)
        return next(data, None)