from app import config
from app.ui import gtk


def on_activate(app) -> None:
    window = config.SETTINGS.main_ui(application=app)
    window.present()


def run() -> None:
    app = gtk.Gtk.Application(application_id=config.SETTINGS.application_id)
    app.connect("activate", on_activate)
    app.run(None)


if __name__ == "__main__":
    run()
