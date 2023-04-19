# simplesofh
# Copyright (C) 2023, David Arnold

from . import base

from typing import Optional
import struct


class V11Message(base.Message):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.header_length = 6
        # FIXME: check for endian-ness flag
        self.endian = ">"

    def _set_length(self, length: int):
        assert length >= 0
        assert length <= 0xffffffff
        assert len(self.buffer) >= self.header_length

        self.buffer[0:4] = struct.pack(f'{self.endian}L', length)

    def _set_message_type(self, message_type: int):
        assert message_type >= 0
        assert message_type <= 0xffff
        assert len(self.buffer) >= self.header_length

        self.buffer[4:6] = struct.pack(f'{self.endian}H', message_type)

    def _get_length(self) -> int:
        assert len(self.buffer) >= self.header_length

        length = struct.unpack(f'{self.endian}L', self.buffer[0:4])[0]
        return length

    def _get_message_type(self) -> int:
        assert len(self.buffer) >= self.header_length

        message_type = struct.unpack(f'{self.endian}H', self.buffer[4:6])[0]
        return message_type


class V11Decoder(base.Decoder):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.length = 0
        # FIXME: set endian-ness flag from keywords flag
        self.endian = ">"

    def get_message(self) -> Optional[bytearray]:
        # FIX SOSH v1.0 has a 4 byte big-endian length at offset zero.

        if len(self.buffer) < 6:
            return None

        if self.length == 0:
            self.length = struct.unpack(f'{self.endian}L', self.buffer[0:4])[0]

        if len(self.buffer) < self.length:
            return None

        assert len(self.buffer) >= self.length
        assert len(self.buffer) >= 6

        buffer = self.buffer[0:self.length]
        self.buffer = self.buffer[self.length:]
        self.length = 0

        return buffer

