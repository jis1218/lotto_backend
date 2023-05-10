from dataclasses import dataclass


@dataclass
class NearestStoreDto:
    store_name: str
    address: str
    longitude: str
    latitude: str
    distance: str
    first_lottery: int
    second_lottery: int
