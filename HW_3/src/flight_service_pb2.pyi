import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FlightStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[FlightStatus]
    SCHEDULED: _ClassVar[FlightStatus]
    DEPARTED: _ClassVar[FlightStatus]
    COMPLETED: _ClassVar[FlightStatus]
    CANCELLED: _ClassVar[FlightStatus]
UNSPECIFIED: FlightStatus
SCHEDULED: FlightStatus
DEPARTED: FlightStatus
COMPLETED: FlightStatus
CANCELLED: FlightStatus

class TReqGetFlight(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class TRspGetFlight(_message.Message):
    __slots__ = ("id", "origin", "destination", "scheduled_departure_time", "scheduled_arrival_time", "flight_code", "carrier", "total_seats", "available_seats", "seat_price", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_DEPARTURE_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_ARRIVAL_TIME_FIELD_NUMBER: _ClassVar[int]
    FLIGHT_CODE_FIELD_NUMBER: _ClassVar[int]
    CARRIER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SEATS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_SEATS_FIELD_NUMBER: _ClassVar[int]
    SEAT_PRICE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    origin: str
    destination: str
    scheduled_departure_time: _timestamp_pb2.Timestamp
    scheduled_arrival_time: _timestamp_pb2.Timestamp
    flight_code: str
    carrier: str
    total_seats: int
    available_seats: int
    seat_price: int
    status: FlightStatus
    def __init__(self, id: _Optional[str] = ..., origin: _Optional[str] = ..., destination: _Optional[str] = ..., scheduled_departure_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., scheduled_arrival_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., flight_code: _Optional[str] = ..., carrier: _Optional[str] = ..., total_seats: _Optional[int] = ..., available_seats: _Optional[int] = ..., seat_price: _Optional[int] = ..., status: _Optional[_Union[FlightStatus, str]] = ...) -> None: ...

class TReqSearchFlights(_message.Message):
    __slots__ = ("origin", "destination", "date")
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    origin: str
    destination: str
    date: str
    def __init__(self, origin: _Optional[str] = ..., destination: _Optional[str] = ..., date: _Optional[str] = ...) -> None: ...

class TRspSearchFlights(_message.Message):
    __slots__ = ("flights",)
    FLIGHTS_FIELD_NUMBER: _ClassVar[int]
    flights: _containers.RepeatedCompositeFieldContainer[TRspGetFlight]
    def __init__(self, flights: _Optional[_Iterable[_Union[TRspGetFlight, _Mapping]]] = ...) -> None: ...

class TReqReserveSeats(_message.Message):
    __slots__ = ("flight_id", "booking_id", "seat_count")
    FLIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    SEAT_COUNT_FIELD_NUMBER: _ClassVar[int]
    flight_id: str
    booking_id: str
    seat_count: int
    def __init__(self, flight_id: _Optional[str] = ..., booking_id: _Optional[str] = ..., seat_count: _Optional[int] = ...) -> None: ...

class TRspReserveSeats(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TReqReleaseReservation(_message.Message):
    __slots__ = ("booking_id",)
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    booking_id: str
    def __init__(self, booking_id: _Optional[str] = ...) -> None: ...

class TRspReleaseReservation(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
