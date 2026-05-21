from typing import List, Tuple
from random import random
from math import floor
from utils.config import AMMO_COUNT, LIFE_COUNT, FIELD_WIDTH, FIELD_HEIGHT
from models.coords import Coords
from models.size import Size
from models.direction import Direction
from models.shot import Shot


from random import random
from math import floor
from models.shot import Shot
from models.direction import Direction
from utils.config import FIELD_WIDTH, FIELD_HEIGHT

class Tank:
    model = "Базовая модель"
    def __init__(
        self,
        x: int,
        y: int,
        direction: Direction,
        map_width: int,
        map_height: int,
        ammo_count: int = AMMO_COUNT,
        life_count: int = LIFE_COUNT,
        gun_angle: float = 0
    ):
        self.coords = Coords(x=x, y=y)
        self.direction = direction
        self.map = Size(width=map_width, height=map_height)
        self.ammo = ammo_count
        self.life = life_count
        self.angle = gun_angle
        self.targets = {}
    

    def is_ammo_finished(self):
        return self.ammo <= 0
    

    def is_life_finished(self):
        return self.life <= 0
    

    def decrease_ammo(self):
        if not self.is_ammo_finished():
            self.ammo -= 1
    

    def decrease_life(self):
        if not self.is_life_finished():
            self.life -= 1


    def show_stats(self):
        print(f"> {self.model} (жизнь: {self.life}, снаряды: {self.ammo})")

    
    def next(self, origin: Coords, targets: List[Coords], shots: List[Coords]) -> Tuple[Direction, Shot]:
        """
        Return next step's decision

        :param targets: List[Coords] list of target coordinates
        :return: Tuple[Direction, Shot]
        """
        if not self.is_ammo_finished() and len(targets) > 0 and floor(2 * random()) == 0:
            target_zone_size = 3
            target_index = floor(len(targets) * random())
            raw_shot_x = floor(target_zone_size * random()) + 1
            if raw_shot_x > target_zone_size:
                raw_shot_x = target_zone_size
            raw_shot_y = floor(target_zone_size * random()) + 1
            if raw_shot_y > target_zone_size:
                raw_shot_y = target_zone_size
            shot_x = targets[target_index].coords.x - int((target_zone_size - 1) / 2) + raw_shot_x
            shot_y = targets[target_index].coords.y - int((target_zone_size - 1) / 2) + raw_shot_y
            shot = Shot(x=shot_x, y=shot_y) if shot_x > 0 and shot_x <= FIELD_WIDTH and shot_y > 0 and shot_y <= FIELD_HEIGHT else None
            return (self.direction, shot)
        else:
            d = floor(4 * random())
            return (Direction(d), None)
    

    def show(self, point_character: str = "B") -> str:
        return point_character


class Berserk(Tank):
    model = "Берсерк"

    def __init__(self, x, y, direction, map_width, map_height):
        Tank.__init__(self, x, y, direction, map_width, map_height,
                      ammo_count=20, life_count=4)
        self.max_life = 4

    def is_life_finished(self):
        return self.life <= 0

    def is_ammo_finished(self):
        return self.ammo <= 0

    def _dist(self, a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)

    def next(self, origin, targets, shots):
        #  ЛЕЧЕНИЕ 
        if self.life < self.max_life:
            want_heal = False
            if self.is_ammo_finished() or not targets:
                want_heal = True
            elif self.life <= 2:
                nearest = min(targets, key=lambda t: self._dist(origin, t.coords))
                if self._dist(origin, nearest.coords) > 3:
                    want_heal = True
            else:
                # случайный шанс: чем меньше хп, тем выше вероятность
                if self.life == 3:
                    chance = 0.25   # 25%
                elif self.life == 2:
                    chance = 0.5
                elif self.life == 1:
                    chance = 0.75
                else:
                    chance = 0.0
                if random() < chance:
                    want_heal = True

            if want_heal:
                self.life = min(self.life + 1, self.max_life)
                self.healing = True
                return (Direction.Stop, None)

        #  СТРЕЛЬБА 
        if not self.is_ammo_finished() and len(targets) > 0:
            if floor(2 * random()) == 0:   # 50% шанс выстрела, как у базового
                target = targets[floor(len(targets) * random())]
                if self.life <= 2:
                    # точный выстрел (разброс 0)
                    shot_x, shot_y = target.coords.x, target.coords.y
                else:
                    # большой разброс ±2
                    dx = floor(4 * random()) - 2
                    dy = floor(4 * random()) - 2
                    shot_x = target.coords.x + dx
                    shot_y = target.coords.y + dy

                if 1 <= shot_x <= FIELD_WIDTH and 1 <= shot_y <= FIELD_HEIGHT:
                    return (self.direction, Shot(x=shot_x, y=shot_y))
                else:
                    return (self.direction, None)
            # не выстрелили - случайное движение
            d = floor(4 * random())
            return (Direction(d), None)

        #  НЕТ ПАТРОНОВ, НО ЕСТЬ ВРАГИ 
        if targets:
            nearest = min(targets, key=lambda t: self._dist(origin, t.coords))
            dx = nearest.coords.x - origin.x
            dy = nearest.coords.y - origin.y
            if abs(dx) > abs(dy):
                escape = Direction.Left if dx > 0 else Direction.Right
            else:
                escape = Direction.Up if dy > 0 else Direction.Down
            return (escape, None)

        return (Direction.Stop, None)

    def show(self, point_character="B"):
        return point_character
    
