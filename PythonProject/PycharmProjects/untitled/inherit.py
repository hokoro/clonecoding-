# 상속 : 특정한 클래스는 다른 클래스의 멤버 변수와 메소드를 물려 받으면서 작성하는 방법
# 부모와 자식 관계 가 존재
# 자식클래스는 부모 클래스를 상속 받은 클래스
class Unit:
    def __init__(self,name,power):
        self.name = name
        self.power = power
    def __del__(self):
        print("Unit 이 소멸되었습니다")
    def attack(self):
        print(self.name,"이 공격을 수행합니다. [전투력 :",self.power,"]")
class Monster(Unit):
    def __init__(self,name,power,type):
        self.name = name
        self.power = power
        self.type = type
    def show_info(self):
        print("몬스터 이름 :" ,self.name,"몬스터 종류 :",self.type)
    def __del__(self):
        print(self.type,"의 몬스터가 소멸되었습니다")
unit = Unit("홍길동",375)
unit.attack()

monster = Monster("슬라임",10,"초급")
monster.show_info()
monster.attack()
