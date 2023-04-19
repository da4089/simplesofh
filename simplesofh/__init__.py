# simplesofh
# Copyright (C) 2023, David Arnold


# Define codec classes for each variant, plus a common base class
# Try to use bytearray / memoryview where possible
# Factory functions for encoder and decoder, with enums for variants?

FIX_SOFH_1_0 = 1
FIX_SOFH_1_1 = 2
CME_SOFH_3.0 = 3


def get_message(variant, **kargs):
    pass


def get_decoder(variant):
    pass
