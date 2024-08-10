from typing import Type
from app.ui import authenticator, gtk

from app.domain import ports
from app.infra import authentication_repository


class Settings:
    name_application: str = "authenticator"
    application_id: str = "com.%s.app" % name_application

    main_ui: Type[gtk.Gtk.ApplicationWindow] = authenticator.AuthenticatorWindow

    authenticator_repository: ports.AuthenticationFinderRepositoryPort = authentication_repository.AuthenticationFinderAdapter()


SETTINGS = Settings()