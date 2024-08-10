from app.domain import models, exceptions

from app import config


def authenticate(request: models.AuthenticationRequest) -> models.AuthenticationResponse:
    user = config.SETTINGS.authenticator_repository.get_by_user(user=request.user)
    if not user:
        return models.AuthenticationResponse(
            authenticated=False, 
            user=None, 
            errors=[exceptions.FailedAuthentication()]
        )
    return models.AuthenticationResponse(authenticated=True, user=user, errors=[])