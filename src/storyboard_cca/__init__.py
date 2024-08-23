import logging
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # csrs not installed, likely developer mode
    __version__ = None


logger = logging.getLogger(__name__)
