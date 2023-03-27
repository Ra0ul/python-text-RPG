import random
import os
import hello

# 캐릭터 소환
mon_max_hp = random.randrange(10, 100)
mon_power = random.randrange(10, 50)
pla_max_hp = random.randrange(50, 100)
pla_power = random.randrange(10, 30)
pla_max_mp = 10
player = hello.Player("Default", pla_max_hp, pla_power, pla_max_mp)
monster = hello.Monster("Monster", mon_max_hp, mon_power)

# 캐릭터 이름 정하기
player.name = str(input("플레이어의 이름을 지정해 주세요 : "))
os.system('clear')


def game_start():
    print("")
    print("----------@@@입장@@@----------")
    player.show_status()
    monster.show_status()
    # flag = True
    while True:
        print("")
        print("----------전장----------")

        skill = input("스킬을 선택해주세요.(마법공격(m)/일반공격(d)) : ")
        # 조건문을 잘못써서 문제 발생....
        if (skill == "d") or (skill == "일반공격"):
            player.attack(monster)

        else:
            player.attack_mp(monster)
            # print("햅삐햅삐~~~~~~~")
            # print(skill)
        monster.attack(player)
        # os.system('clear')
        print("")
        print("----------상태체크----------")
        player.show_status()
        monster.show_status()

        if (player.hp <= 0) or (monster.hp <= 0):
            # flag = not flag
            break


game_start()

print("")
print("----------###결투결과###----------")
if player.hp > monster.hp:
    print("승리했습니다!")
    # respon = input("새 게임으로 다시 도전하시겠습니까? : (y/n)")
    # if respon == "y":
    #     game_start()
    # else:
    #     pass
elif player.hp < monster.hp:
    print("패배했습니다!")
    # input("새 게임으로 다시 도전하시겠습니까? : (y/n)")
    # respon = input("새 게임으로 다시 도전하시겠습니까? : (y/n)")
    # if respon == "y":
    #     game_start()
    # else:
    #     pass
else:
    print("비겼습니다.")
    respon = input("다시 도전하시겠습니까? : (y/n)")
    if respon == "y":
        game_start()
    else:
        pass
