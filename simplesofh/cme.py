# simplesofh
# Copyright (C) 2023, David Arnold

from . import base

from typing import Optional
import struct


class CmeMessage(base.Message):

    def __init__(self):
        super().__init__()
        self.header_length = 4

    def _set_length(self, length: int):
        assert length >= 0
        assert length <= 0xffff
        assert len(self.buffer) >= self.header_length

        self.buffer[0:2] = struct.pack('<H', length)

    def _set_message_type(self, message_type: int):
        assert message_type >= 0
        assert message_type <= 0xff
        assert len(self.buffer) >= self.header_length

        self.buffer[2:4] = struct.pack('<H', message_type)

    def _get_length(self) -> int:
        assert len(self.buffer) >= self.header_length

        length = struct.unpack('<H', self.buffer[0:2])[0]
        return length

    def _get_message_type(self) -> int:
        assert len(self.buffer) >= self.header_length

        message_type = struct.unpack('<H', self.buffer[2:4])[0]
        return message_type


class CmeDecoder(base.Decoder):

    def __init__(self):
        super().__init__()
        self.length = 0

    def get_message(self) -> Optional[bytearray]:
        # CME SOSH has a 2-byte little-endian length

        if len(self.buffer) < 4:
            return None

        if self.length == 0:
            self.length = struct.unpack('<H', self.buffer[0:2])[0]

        if len(self.buffer) < self.length:
            return None

        assert len(self.buffer) >= self.length
        assert len(self.buffer) >= 4

        buffer = self.buffer[0:self.length]
        self.buffer = self.buffer[self.length:]
        self.length = 0

        return buffer

