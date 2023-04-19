# simplesofh
# Copyright (C) 2023, David Arnold

from typing import Optional


class Message:
    """Base class for decoded messages."""

    def __init__(self, **kargs):
        self.buffer = bytearray()
        self.header_length = 0

    def _set_length(self, length: int):
        raise NotImplementedError("Should be overridden")

    def _set_message_type(self, message_type: int):
        raise NotImplementedError("Should be overridden")

    def _get_length(self) -> int:
        raise NotImplementedError("Should be overridden")

    def _get_message_type(self) -> int:
        raise NotImplementedError("Should be overridden")

    # Public API

    def payload_length(self) -> int:
        return len(self.buffer) - self.header_length

    def message_type(self) -> int:
        return self._get_message_type()

    def payload(self) -> bytearray:
        return self.buffer[self.header_length:]

    def set_payload(self, message_type: int, buffer: [bytes | bytearray | memoryview]) -> None:
        self.buffer = bytearray(self.header_length + len(buffer))
        self._set_length(len(buffer) + self.header_length)
        self._set_message_type(message_type)
        self.buffer[self.header_length:self.header_length + len(buffer)] = buffer
        return

    def encode(self) -> Optional[bytearray]:
        return self.buffer


class Decoder:
    """SOFH decoder base class."""

    def __init__(self, **kargs):
        self.buffer = bytearray()

    def append_bytes(self, buffer: [bytes | bytearray | memoryview]):
        """Process a buffer of received data.

        :param buffer: Buffer of received data."""

        self.buffer.extend(buffer)

    def get_message(self) -> Optional[Message]:
        raise NotImplementedError("Should be overridden")

