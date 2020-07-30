# class : 반복되는 불필요한 소스코드를 최소화 하면서
#    현실 세계 의 사물을 프로그래밍 상에서
#   쉽게 표현 할수 있도록 해주는 프로그래밍 기술
# 인스턴스 : 클래스로 정의된 객체를 프로그래밍 상에
# 클래스의 멤버 : 클래스 내부에 포함되는 변수
# 클래스 의 함수 : 클래스 내부에 포함되는 함수 , 메소드 라고 부른다

class Car:
    #클래스의 생성자
    def __init__(self,name,color):
        self.name = name
        self.color = color
    #클래스의 소멸자 # 프로그램이 종료되면 그즉시 종료
    def __del__(self):
        print("인스턴스를 소멸시킵니다 ")
    #클래스의 메소드,#모든 클래스의 매개변수 self 를 사용한다
    def show_info(self):
        print("이름:", self.name,"/색상:" , self.color)
    # Setter 메소드
    def set_name(self,name):
        self.name = name


car1 = Car("소나타", "빨간색")
car1.show_info()

car2 = Car("아반뗴","검은색")
car2.show_info()

print(car1.name,"을 구매 했습니다 ")
car1.set_name("아반떼")
car1.show_info()
del car1
del car2
