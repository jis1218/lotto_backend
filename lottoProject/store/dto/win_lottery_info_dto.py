from dataclasses import dataclass


@dataclass
class WinLotteryInfoDto:
    round: int
    store_name: str
    address: str
    select_type: str
    first_lottery_sum: int
    second_lottery_sum: int
    active: bool
