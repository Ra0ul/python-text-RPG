import random
import os
import hello


mon_max_hp = random.randrange(10, 100)
mon_power = random.randrange(10, 50)
pla_max_hp = random.randrange(50, 100)
pla_power = random.randrange(10, 30)
pla_max_mp = 100

player = hello.Player("Default", pla_max_hp, pla_power, pla_max_mp)
player.name = str(input("플레이어의 이름을 지정해 주세요 : "))

os.system('clear')
monster = hello.Monster("Monster", mon_max_hp, mon_power)
player.show_status()
monster.show_status()

skill = input("스킬을 선택해주세요.(마법공격(m)/일반공격(d)) : ")
if skill == "m" or "마법공격":
    pla_skill_option = player.attack_mp(monster)
else:
    pla_skill_option = player.attack(monster)

while True:
    pla_skill_option
    monster.attack(player)

    player.show_status()
    monster.show_status()

    if (player.hp <= 0) or (monster.hp <= 0):
        break

if player.hp > monster.hp:
    print("승리했습니다!")
elif player.hp < monster.hp:
    print("패배했습니다!")
else:
    print("비겼습니다.")
    input("다시 도전하시겠습니까? : (y/n)")
