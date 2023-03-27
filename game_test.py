import random
import os
import hello


mon_max_hp = random.randrange(10, 100)
mon_power = random.randrange(10, 50)
pla_max_hp = random.randrange(50, 100)
pla_power = random.randrange(10, 30)
pla_max_mp = 10


player = hello.Player("Default", pla_max_hp, pla_power, pla_max_mp)
player.name = str(input("플레이어의 이름을 지정해 주세요 : "))

os.system('clear')
monster = hello.Monster("Monster", mon_max_hp, mon_power)


def game_start():
    os.system('clear')
    print("")
    print("----------@@@입장@@@----------")
    player.show_status()
    monster.show_status()
    flag = 1
    while flag == True:
        print("")
        print("----------전장----------")

        skill = input("스킬을 선택해주세요.(마법공격(m)/일반공격(d)) : ")
        if skill == "m" or "마법공격":
            player.attack_mp(monster)
        else:
            player.attack(monster)

        monster.attack(player)
        # os.system('clear')
        print("")
        print("----------상태체크----------")
        player.show_status()
        monster.show_status()

        if (player.hp <= 0) or (monster.hp <= 0):
            flag = 0
            break

    print("")
    print("----------###결투결과###----------")
    if player.hp > monster.hp:
        print("승리했습니다!")
    elif player.hp < monster.hp:
        print("패배했습니다!")
    else:
        print("비겼습니다.")
        input("다시 도전하시겠습니까? : (y/n)")


game_start()
