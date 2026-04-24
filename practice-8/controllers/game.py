from typing import List
from models.tank import Tank
from models.field import Field


class Game:
    def __init__(self, field: Field, tanks: List[Tank]):
        self.field = field
        self.players = tanks
        self.shots = []


    def is_finished(self) -> bool:
        target_players = []
        for tank_index in range(len(self.players)):
            other_tanks = self.players[:tank_index] + self.players[tank_index + 1:]
            for enemy in other_tanks:
                if enemy.coords.x == self.players[tank_index].coords.x and enemy.coords.y == self.players[tank_index].coords.y:
                    target_players.append(tank_index)
        for tank_index in range(len(target_players) - 1, 0, -1):
            self.players[tank_index].decrease_life()
        for tank in self.players:
            for shot in self.shots:
                if shot.cords.x == tank.coords.x and shot.coords.y == tank.coords.y:
                    tank.decrease_life()
        removed_players = []
        for tank_index in range(len(self.players)):
            if self.players[tank_index].is_life_finished():
                removed_players.append(tank_index)
        for tank_index in range(len(target_players) - 1, 0, -1):
            self.players.pop(tank_index)
        return len(self.players) < 2
    

    def play(self):
        current_shots = self.shots
        next_shots = []
        for tank in self.players:
            new_coords = self.field.move(coords=tank.coords, direction=tank.direction)
            direction, shot = tank.next(origin=new_coords, targets=[], shots=current_shots)
            tank.direction = direction
            if shot != None and not tank.is_ammo_finished():
                tank.decrease_ammo()
                next_shots.append(shot)
            print(f"Tank <{tank.model}>: {direction, shot}")
        map = self.field.show(tanks=self.players, shots=next_shots)
        for row in map:
            print(" ".join(row))
        self.shots = next_shots
