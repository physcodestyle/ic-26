from enum import Enum
from typing import Dict, Tuple


AMMO_COUNT = 20


class Direction(Enum):
    Stop = 0
    Up = 1
    Right = 2
    Down = 3
    Left = 4


class Tank:
    def __init__(
        self,
        id: str,
        x: int,
        y: int,
        direction: Direction,
        map_width: int,
        map_height: int,
        ammo_count: int = AMMO_COUNT,
        gun_angle: float = 0
    ):
        self.id = id
        self.origin = {
            "x": x,
            "y": y,
            "direction": direction,
        }
        self.map = {
            "width": map_width,
            "height": map_height,
        }
        self.ammo = ammo_count
        self.angle = gun_angle
        self.targets = {}


    def get_id(self) -> str:
        return self.id
    

    def is_ammo_finished(self):
        return self.ammo == 0

    
    def next(target_angles: Dict[str, float]) -> Tuple[Direction, float, bool]:
        """
        Return next step's decision

        :param target_angles: Dict of named target angles
        :return: Tuple[direction, gun_angle, is_shooting]
        """
        # target_movements
        # get strategy
        # return strategy Tuple
        pass
