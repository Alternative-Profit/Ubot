__all__ = ['Restart']

from loader.Ubot.api import restart
from Ubot import logging
from ...ext import RawClient

_LOG = logging.getLogger(__name__)


class Restart(RawClient):  # pylint: disable=missing-class-docstring
    @staticmethod
    async def restart(hard: bool = False, **_) -> None:
        """ Restart the Ubot """
        _LOG.info(f"Restarting Ubot [{'HARD' if hard else 'SOFT'}]")
        restart(hard)