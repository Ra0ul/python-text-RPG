# 클래스 정리 파일#

import random


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power):
        self.name = name  # 이름
        self.max_hp = hp  # MAX_HP
        self.hp = hp  # 현재 HP
        self.power = power  # 파워

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)  # 랜덤 데미지 주기
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Player(Character):
    """
    플레이어 생성 서브 클래스
    """

    def __init__(self, name, hp, power):
        self.attribute = "player"
        super().__init__(name, hp, power)


class Monster(Character):
    """
    몬스터 생성 서브 클래스
    """

    def __init__(self, name, hp, power):
        self.attribute = "monster"
        super().__init__(name, hp, power)
