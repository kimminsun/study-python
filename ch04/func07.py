#calendar 파이썬에서 달력을 볼 수 있음
import calendar
print(calendar.calendar(2017))

#0부터 월요일 6은 일요일
print(calendar.weekday(2017,12,31))

#monthrange 입력받은 달의 1일이 무슨 요일인지와 그 달이 며치라지 있는지를 튜플 형태로 리턴
print(calendar.monthrange(2017,12))

#random 난수를 발생시키는 모듈
import random
print(random.random())

print(random.randint(1,55))



def random_pop(data):
    number=random.randint(0,len(data)-1)
    return data.pop(number)

if __name__=="__main__":
    data=[1,2,3,4,5]
    while data:print(random_pop(data))


def random_pop(data):
    number=random.choice(data)
    data.remove(number)
    return number

data=[1,2,3,4,5]
random.shuffle(data)
print(data)


#webbrowser
import webbrowser
webbrowser.open("http://github.com/kimminsun")