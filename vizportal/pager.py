from vizportal.viz_portal_call import VizPortalCall
from vizportal.payload import PayloadBuilder
from tableauserverclient import Server
from typing import Dict
from collections.abc import Iterator


class VizportalPager(VizPortalCall):
    """A class that handles pagination for the Vizportal API.
    This class can be used as an iterator to get all of the results from a request.

    ...

    Attributes
    ----------
        server (Server): The Tableau Server object.
        payload (PayloadBuilder | Dict): The payload for the request.
        max_pages (int): The maximum number of pages to return.

    Methods
    -------
        __iter__() -> Iterator[Dict]
            Returns an iterator for the class.
    """

    def __init__(
        self, server: Server, payload: PayloadBuilder | Dict, max_pages: int = None
    ):
        super().__init__(server)
        self.payload = self._payload_builder(payload)
        self.max_pages = max_pages
        self._start_index = None
        self._max_items = None
        self._pages_returned = None

    def __iter__(self) -> Iterator[Dict]:
        response = self._get_response()
        if self._pages_returned is None:
            self._pages_returned = 1
        yield response["result"]

        # Ensure we don't get stuck in an infinite loop
        if self.max_items == 0:
            return
        
        while response.get("result", {}).get("moreItems"):
            if self.max_pages is not None and self._pages_returned >= self.max_pages:
                break
            self.start_index += self.max_items
            response = self._get_response()
            self._pages_returned += 1
            yield response["result"]

        return

    @property
    def pages_returned(self) -> int:
        "Returns the number of pages returned from the iterator."
        if self._pages_returned is None:
            raise Exception("The iterator has not been called yet.")
        return self._pages_returned

    @property
    def start_index(self) -> int:
        "Returns the start index"
        if self._start_index is None:
            self._start_index = self.payload["params"]["page"]["startIndex"]
        return self._start_index

    @start_index.setter
    def start_index(self, value: int):
        "Sets the start index"
        self._start_index = value

    @property
    def max_items(self) -> int:
        "Returns the max items"
        if self._max_items is None:
            self._max_items = self.payload["params"]["page"]["maxItems"]
        return self._max_items

    @max_items.setter
    def max_items(self, value: int):
        "Sets the max items"
        self._max_items = value

    def _get_response(self) -> Dict:
        "Sets the startIndex and returns the response"
        self.payload["params"]["page"]["startIndex"] = self.start_index
        response = self.make_request(self.payload)
        return response
