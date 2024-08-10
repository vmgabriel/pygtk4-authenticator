from typing import Any

from app.ui import gtk, home, dialog
from app.ui.components import title, component
from app.ui.components.forms import input, password
from app.ui.components.buttons import ok_cancel_box

from app.domain import models
from app.services import authenticate


class AuthenticatorWindow(gtk.Gtk.ApplicationWindow):
    def __init__(self, **kargs: Any):
        super().__init__(
            **kargs,
            title="Authenticate",
        )

        # box
        main_box = gtk.Gtk.Box(
            spacing=6,
            orientation=gtk.Gtk.Orientation.VERTICAL,
        )
        self.set_child(main_box)
        self.set_resizable(False)

        margin_title = component.Margins(top=20, bottom=20)
        current_title = title.Title(title="Autenticacion", margins=margin_title)
        current_title.build(main_box=main_box)

        self.user_field = input.InputForm(label="Ingrese Usuario")
        self.user_field.build(main_box=main_box)

        self.pass_field = password.PasswordForm(label="Ingrese Contraseña")
        self.pass_field.build(main_box=main_box)

        box_buttons = ok_cancel_box.OkCancelButtonsBox(callback=self.button_clicked)
        box_buttons.build(main_box=main_box)

    def button_clicked(self, button_event_clicked) -> None:
        if button_event_clicked == "ACCEPT":
            authenticated_response = authenticate.authenticate(
                request=models.AuthenticationRequest.create(
                    user=self.user_field.value, 
                    password=self.pass_field.value,
                )
            )
            if authenticated_response.authenticated:
                home_window = home.HomeWindow(application=self.get_application())
                home_window.present()
                self.close()
            else:
                popup = dialog.DialogWindow(
                    application=self.get_application(), 
                    title="Autenticacion Fallida", message=authenticated_response.errors[0].message
                )
                popup.present()

        if button_event_clicked == "CANCEL":
            self.user_field.clear()
            self.pass_field.clear()
            self.user_field.focus()