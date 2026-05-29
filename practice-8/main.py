from typing import List, Type
from seeders.tank_factory import generate_tank
from utils.config import FIELD_WIDTH, FIELD_HEIGHT
from models.tank import Tank, Berserk
from models.field import Field
from controllers.game import Game


APPROVED_TANK_MODELS = [
    Tank,
    Berserk
]


def init_field() -> Field:
    return Field(map_width=FIELD_WIDTH, map_height=FIELD_HEIGHT)


def select_player_models() -> List[Type[Tank]]:
    models = []
    player_count = int(input("Выберете количество игроков: "))
    print("В игре есть следующие модели танков:")
    for i in range(len(APPROVED_TANK_MODELS)):
        print(f"{i + 1}. {APPROVED_TANK_MODELS[i].model}")
    for i in range(player_count):
        model_number = int(input(f"Выберете номер модели танка #{i + 1}: "))
        while(model_number <= 0 and model_number > len(APPROVED_TANK_MODELS) + 1):
            model_number = input(f"Такой модели не существует. Выберете номер модели танка #{i + 1}: ")
        models.append(APPROVED_TANK_MODELS[model_number - 1])
    return models


def init_tanks(field: Field, tank_models: List[Type[Tank]]) -> List[Tank]:
    tanks = []
    for tank_class_index in range(len(tank_models)):
        tanks.append(generate_tank(model_class=tank_models[tank_class_index], field=field, player_index=tank_class_index + 1))
    return tanks


def run():
    battle_field = init_field()
    player_models = select_player_models()
    players = init_tanks(field=battle_field, tank_models=player_models)
    game = Game(field=battle_field, tanks=players)
    round_counter = 1
    print(">>>>>>> Игра началась! <<<<<<<\n\n")

    while(not game.is_finished(round=round_counter)):
        game.play(round=round_counter)
        round_counter += 1
    
    print("\n>>>>>>> Игра завершена! <<<<<<<")
    print("\n------- Результаты! -------\n")
    for p in players:
        p.show_stats()
    print("\n---------------------------\n")


if __name__ == "__main__":
    run()





# Есть идея для игрового процесса:
# 1. Как-либо реализовать выстрел не точкой, а вектором до этой точки
# 2. В случае, когда боеприпасы у всех танков на поле заканчиваются, объявлять победителем танк, с наибольшим кол-м очков здоровья 
# (желательно в процентах, тк, например, если у Базовой модели и у Берсерка оатслось по 4 хп, очевидно победителем должен быть Берсерк, тк у него 100% здоровья, а у Базового - 80%),
# чтобы избежать бесконечного перемещения по полю

# Касаемо моего кастомного танка: он обладает двумя режимами, при здоровье ниже и выше половины.
# Если очков здоровья 3-4, то его поведение схоже с Базовой моделью.
# Если же их 1-2, то по задумке разброс выстрела становится меньше, но честно говоря, не очень понимаю, работает это или нет.
# Самое интересное, что если танк ранен, то он может добавить себе очко здоровья. Занимает это 1 ход.