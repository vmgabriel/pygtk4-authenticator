from app.domain import commons


class FailedAuthentication(commons.Error):
    def __init__(self) -> None:
        super().__init__(
            code = 401,
            message = "Authorizacion Fallida",
            description = "Ha fallado la authorizacion debido a una incongruencia con los datos",
        )