from models.size import Size
from models.coords import Coords
from models.direction import Direction


class Field:
    def __init__(
        self,
        map_width: int,
        map_height: int,
    ):
        self.size = Size(width=map_width, height=map_height)


    def move(self, coords: Coords, direction: Direction) -> Coords:
        if coords.x == 1 and direction == Direction.Left:
            return coords
        elif coords.x == self.size.width and direction == Direction.Right:
            return coords
        elif coords.y == 1 and direction == Direction.Up:
            return coords
        elif coords.y == self.size.height and direction == Direction.Down:
            return coords
        elif direction == Direction.Left:
            coords.x -= 1
        elif direction == Direction.Right:
            coords.x += 1
        elif direction == Direction.Up:
            coords.y -= 1
        elif direction == Direction.Down:
            coords.y += 1
        return coords
