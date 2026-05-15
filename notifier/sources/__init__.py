from ..source import Source
from .avalon import AvalonSource
from .karti import KartiSource
from .kupikarta import KupiKartaSource
from .mktickets import MkTicketsSource
from .ticketx import TicketXSource
from .wayin import WayInSource

ALL_SOURCES: list[Source] = [
    AvalonSource(),
    KupiKartaSource(),
    KartiSource(),
    MkTicketsSource(),
    TicketXSource(),
    WayInSource(),
]

__all__ = [
    "ALL_SOURCES",
    "AvalonSource",
    "KartiSource",
    "KupiKartaSource",
    "MkTicketsSource",
    "TicketXSource",
    "WayInSource",
]
