from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Races(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DARK: _ClassVar[Races]
    LIGHT: _ClassVar[Races]

class Hand(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RIGHT: _ClassVar[Hand]
    LEFT: _ClassVar[Hand]
DARK: Races
LIGHT: Races
RIGHT: Hand
LEFT: Hand

class HandRequest(_message.Message):
    __slots__ = ("count", "race", "hand")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    RACE_FIELD_NUMBER: _ClassVar[int]
    HAND_FIELD_NUMBER: _ClassVar[int]
    count: int
    race: Races
    hand: Hand
    def __init__(self, count: _Optional[int] = ..., race: _Optional[_Union[Races, str]] = ..., hand: _Optional[_Union[Hand, str]] = ...) -> None: ...

class HandReply(_message.Message):
    __slots__ = ("FileName", "FileBytes")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILEBYTES_FIELD_NUMBER: _ClassVar[int]
    FileName: str
    FileBytes: bytes
    def __init__(self, FileName: _Optional[str] = ..., FileBytes: _Optional[bytes] = ...) -> None: ...
