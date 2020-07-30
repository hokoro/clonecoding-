#에외 처리를 사용하면 특정한 오류 구문을 해결 가능
# try except
#db 구문에서 많이 사용한다
try :
    print(3/0)
except Exception as e:
    print(e)
else:
    print("예외 없이 성공적으로 프로그램이 실행 되었습니다")
finally:
    print("예외 처리를 마칩니다")