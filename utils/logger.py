import logging


stream_handler = logging.StreamHandler()

log = logging.getLogger(__name__)
log.addHandler(stream_handler)
log.setLevel(logging.INFO)

formatter = logging.Formatter(
    "[Meetings]: {message}",
    style="{",
)
stream_handler.setFormatter(formatter)