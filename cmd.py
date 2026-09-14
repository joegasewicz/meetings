import os

import config
from utils.logger import log
from gui import Gui
from meetings import IssueTracker
from config import Config

MEETINGS_GUI = os.environ.get("MEETINGS_GUI", False)
MEETINGS_WEB = os.environ.get("MEETINGS_WEB", False)


if __name__ == "__main__":
    if MEETINGS_GUI:
        config = Config()
        config.APPLICATION_TYPE = "gui"
        log.info("Launching GUI")
        issue_tracker = IssueTracker(config=config)
        gui = Gui(issue_tracker=issue_tracker)
        gui.run()

    if MEETINGS_WEB:
        config = Config()
        log.info("Running web server...")
