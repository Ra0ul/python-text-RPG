import random
import os
import hello

# 캐릭터
mon_max_hp = random.randrange(10, 100)
mon_power = random.randrange(10, 50)
pla_max_hp = random.randrange(50, 100)
pla_power = random.randrange(10, 30)
pla_max_mp = 10
player = hello.Player("Default", pla_max_hp, pla_power, pla_max_mp)
monster = hello.Monster("Default", mon_max_hp, mon_power)


# 게임 시작
def game_start():
    os.system('clear')
    print("")
    player.name = str(input("플레이어의 이름을 지정해 주세요 : "))
    os.system('clear')

    print("")
    print("----------@@@입장@@@----------")


# def title():
#     count = 0
#     while True:
#         os.system('clear')
#         player.show_status()
#         monster.show_status()
#         print("")
#         print("----------전장----------")
#         count += 1

#         if flag:
#             flag = False
#         else:
#             True


# 전투
def battle_field():
    while True:
        player.show_status()
        monster.show_status()
        print("")
        print("----------전장----------")

        skill = input("스킬을 선택해주세요.(마법공격(m)/일반공격(d)) : ")
        if (skill == "d") or (skill == "일반공격"):
            player.attack(monster)
        else:
            player.attack_mp(monster)
        monster.attack(player)

        if (player.hp <= 0) or (monster.hp <= 0):
            break


# 승부
def game_sorce():
    print("")
    print("----------###결투결과###----------")
    if player.hp > monster.hp:
        print("승리했습니다!")

    elif player.hp < monster.hp:
        print("패배했습니다!")

    else:
        print("비겼습니다.")
        respon = input("다시 도전하시겠습니까? : (y/n)")
        if respon == "y":
            # battle_field()
            pass
        else:
            pass


game_start()
battle_field()

game_sorce()
