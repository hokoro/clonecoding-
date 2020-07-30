#사전 자료형의 정렬
score = {}
score['나동빈'] = 78
score['이태일'] = 99
score['박한울'] = 85
#키를 오름차순으로 정렬하기
print(sorted(score))
#키를 내림차순으로 정렬하기
print(sorted(score,reverse=True))
#값들을 오름차순으로 정렬하기
print(sorted(score.values()))
