__all__ = ['get_collection']

from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticDatabase, AgnosticCollection

from Ubot import config

_DATABASE: AgnosticDatabase = AsyncIOMotorClient(config.DB_URI)["Ubot"]


def get_collection(name: str) -> AgnosticCollection:
    """ Create or Get Collection from your database """
    return _DATABASE[name]