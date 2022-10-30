"""``Connector`` objects are responsible communicating information
between nodes. Individual connector instances are assigned to a
single parent node and can be used to send or receive data depending
on the type of connector. ``Output`` connectors are used to send data
and ``Input`` objects are used to receive data.
"""

from __future__ import annotations

from typing import Optional, Tuple


class BaseConnector:
    """Base class for building signal/slot style connectors on top of an underlying queue"""

    def __init__(self, name: str = None) -> None:
        """Queue-like object for passing data between nodes

        By default, connector names are generated using the instances memory
        identify in hexadecimal representation.

        Args:
            name: Optional name for the connector object
        """

        # Identifying information for the instance
        self._id = hex(id(self))
        self.name = str(self._id) if name is None else name

        # The parent node
        self._node = None

        # Other connector objects connected to this instance
        self._connected_partners = []

    @property
    def parent_node(self) -> Optional:  # Todo: update this type hint
        """The parent node this connector is assigned to"""

        return self._node

    @property
    def partners(self) -> Tuple:
        """Return a tuple of connectors that are connected to this instance"""

        return tuple(self._connected_partners)

    def is_connected(self) -> bool:
        """Return whether the connector has any established connections"""

        return bool(self._connected_partners)

    def __str__(self) -> str:
        """Return the name of the parent instance"""

        return f'<{self.__class__.__name__}(name={self.name}) object at {self._id}>'