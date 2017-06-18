#sys 인터프린터가 제공하는 변수들과 함수들을 직접 제어할 수 있게 해주는 몯ㄹ
#명령행에서 인수 전달하기 - sys.argv

import sys
print(sys.argv)


#pickle 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈

import pickle
f=open("test.txt",'wb')
data={1:'python',2:'you need'}
pickle.dump(data,f)
f.close()


#OS 모듈 환경 변수나 디렉터리,파일 등의 OS자원을 제어할 수 있게 해주는 모듈

import os
os.environ

#shutil 파일ㅇ르 복사해 주는 파이썬 모듈

#glob 특정 디렉터리에 있는 파일 이름 모두를 알아야 할 때 사용

#tempfile 파일을 임시로 만들어서 사용할 때 유용한 모듈

#time 시간에 관련된
import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())


print(time.strftime('%x',time.localtime(time.time())))
print(time.strftime('%c',time.localtime(time.time())))

#sleep 주롤 루프 안에서 많이 사용 일정한 시간 간격을 두고 루프를 실행 할 수 있음
for i in range(10):
    print(i)
    time.sleep(1)

#calendar 파이썬에서 달력을 볼 수 있음
import calendar
print(calendar.calendar(2017))
