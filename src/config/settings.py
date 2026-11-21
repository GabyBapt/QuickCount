from PySide6.QtCore import QSettings

DEFAULT_SETTINGS = {
    "mode": int(0),
    "range": (0, 40),
    "time": 3.0,
}

class TrainingSettings(QSettings):
    def __init__(self):
        super().__init__()
        for key, value in DEFAULT_SETTINGS.items():
            if self.value(key) is None:
                self.setValue(key, value)

settings = TrainingSettings()
        