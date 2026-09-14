import os

import config
from utils.logger import log
from gui import Gui
from meetings import Meeting
from config import Config

MEETINGS_GUI = os.environ.get("MEETINGS_GUI", False)
MEETINGS_WEB = os.environ.get("MEETINGS_WEB", False)


if __name__ == "__main__":
    if MEETINGS_GUI:
        config = Config()
        config.jAPPLICATION_TYPE = "gui"
        log.info("Launching GUI")
        meeting = Meeting(config=config)
        gui = Gui(meeting=meeting)
        gui.run()

    if MEETINGS_WEB:
        config = Config()
        log.info("Running web server...")
