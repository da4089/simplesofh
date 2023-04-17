# simplesofh
A pure-Python implementation of the FIX Trading Community's SOFH
framing protocol.

## SOFH v1.0
Currently a "draft standard", SOFH v1.0 specifies
- a 6 octet header, comprised of
- 4 octets for length, 32 bit unsigned big-endian integer
- 2 octets for message type, 16 bit unsigned big-endian integer
  Various message type values defined by the protocol, including 255
  "private use" values from 1 to 255 decimal.

## SOGH v1.1
Currently a "release candidate 1", SOFH v1.1 specifies:
- a 6 octet header, comprised of
- 4 octets for length, 32 bit unsigned integer
- 2 octets for message type, 16 bit unsigned integer
- Various message type values defined by the protocol, adding SBE v2.0
  and removing BSON from SOFH v1.0.
- Note that both fields are now able to be either big or little
  endian, subject to "counterparty agreement".  There is no indication
  in the header itself which representation is used.

## CME iLink 3 "SOFH"
CME's iLink3 binary order entry protocol uses a framing protocol that
it calls SOFH, which is however incompatible with both v1.0 and v1.1
of the formal specification.

CME iLink SOFH
- a 4 octet header, comprised of
- 2 octets for length, 16 bit unsigned little-endian integer
- 2 octets for message type, 16 bit unsigned little-endian integer
- The message type for CME SBE v1.0 must be a little-endian value of
  0xCAFE.
  - Note that this value is outside the specified "private use" range
    from the FIX standards.
