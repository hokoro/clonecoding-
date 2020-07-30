#미리 작성된 함수 코드를 모아 놓은 파이썬 파일

import lib  #lib 파이썬 파일의 함수를 사용하겠다고 정의
#from lib import add  #lib 에 있는 add 함수만 사용하겠다고 정으
import lib as t #lib 의 제목을 t 로 변경하고 사용함

print(lib.add(10,5))
print(lib.subtract(10,5))
print(t.add(10,5))
