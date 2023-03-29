import random
import os
import hello

# 캐릭터
pla_max_hp = random.randrange(50, 100)
pla_power = random.randrange(10, 30)
pla_max_mp = 10
global player
global monster
player = hello.Character("Default", pla_max_hp, pla_power)
monster = hello.Character("MON", pla_max_hp, pla_power)


# 게임 시작
def game_start():
    os.system('clear')
    print("")
    player.name = str(input("플레이어의 이름을 지정해 주세요 : "))
    os.system('clear')

    print("")
    print("----------@@@입장@@@----------")


# 전투
def battle_field():
    while True:
        player.show_status()
        monster.show_status()
        print("\n----------전장----------")

        skill = input("스킬을 선택해주세요.(마법공격(m)/일반공격(d)) : ")
        if (skill == "d") or (skill == "일반공격"):
            player.attack(other=monster)
        else:
            continue
        monster.attack(other=player)

        if (player.hp <= 0) or (monster.hp <= 0):
            break


game_start()
# 승부를 출력하는 함수 없이 아래처럼 while 반복문으로 재도전 가능!
while True:
    os.system('clear')
    battle_field()
    print("\n----------###결투결과###----------")
    if player.hp > monster.hp:
        print("승리했습니다!")

    elif player.hp < monster.hp:
        print("패배했습니다!")

    else:
        print("비겼습니다.")

    respon = input("다시 도전하시겠습니까? : (y/n)")
    if respon == "n":
        break
print("바이바이~")
