player = {"name": input("Введите имя игрока: "), "health": 100, "damage": 20, "armor": 1.2}
enemy = {"name": input("Введите имя противника: "), "health": 100, "damage": 20, "armor": 1.2}


def attack(attacker, defender):
    defender["health"] -= real_damage(attacker["damage"], defender["armor"])
    print(defender["health"])


def real_damage(damage, armor):
    result = damage / armor
    print(result)
    return result


attack(player, enemy)
print(player, enemy)
