# simplesofh
# Copyright (C) 2023, David Arnold

from .fixsofh10 import V10Decoder, V10Message
from .fixsofh11 import V11Decoder, V11Message
from .cme import CmeDecoder, CmeMessage

from enum import Enum


class Variant(Enum):
    """Protocol variant."""

    # Official FIX Trading Community protocol version 1.0
    FIX_SOFH_1_0 = 1

    # Official FIX Trading Community protocol version 1.1
    FIX_SOFH_1_1 = 2

    # Proprietary CME iLink 3.0 protocol version
    CME_SOFH_3_0 = 3

def get_message(variant: Variant, **kargs):
    """Get a message configured for the specified protocol variant.

    :param variant: Protocol variant for message."""
    if variant == Variant.FIX_SOFH_1_0:
        return V10Message(**kargs)
    elif variant == Variant.FIX_SOFH_1_1:
        return V11Message(**kargs)
    elif variant == Variant.CME_SOFH_3_0:
        return CmeMessage(**kargs)
    else:
        raise ValueError(f"Unknown protocol variant: {variant}")


def get_decoder(variant: Variant, **kargs):
    """Get a protocol decoder for the specified protocol variant.

    :param variant: Protocol variant for decoder."""
    if variant == Variant.FIX_SOFH_1_0:
        return V10Decoder(**kargs)
    elif variant == Variant.FIX_SOFH_1_1:
        return V11Decoder(**kargs)
    elif variant == Variant.CME_SOFH_3_0:
        return CmeDecoder(**kargs)
    else:
        raise ValueError(f"Unknown protocol variant: {variant}")
