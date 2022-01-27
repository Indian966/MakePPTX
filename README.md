# MakePPTX
불쌍한 사무직 혹은 연구원들을 위한 대용량 이미지들을 삽입한 PPT 파일 생성 프로그램

[Now testing]
Travis CI : [![Build Status](https://app.travis-ci.com/Indian966/MakePPTX.svg?branch=master)](https://app.travis-ci.com/Indian966/MakePPTX)


    개발자 : 김민규  
    연락처 : rlaalsrb4175@gmail.com
    작업일 : 2020.12.30
    최근 업데이트 : 2021.05.12
    설명 : 대용량 pptx 이미지 작업을 자동화하는 코드
    사용하기 앞서 데이터 분류 작업을 잘 해놓을 것
    D:\김민규\최은정교수님\PPT_H
    위 폴더를 참고하기 바람
    출력되는 ppt의 내용은 '환자번호 - coronal - 사진들 - transverse - 사진들'로 반복됨
    실행 시키려면 F5를 눌러서 상단에 나오는 리스트 중에 Python File클릭
    이후 수정사항 반영은 ctrl + s 로 저장

이 프로그램은 대용량의 사진 자료들을 PPT로 만들어주는 프로그램입니다.


> '상위 폴더 - 하위 폴더 - 사진자료'

이 형식의 자료 형태를 유지해 주시기 바랍니다.

![image](https://user-images.githubusercontent.com/22446076/117937691-3b0ebd80-b341-11eb-8b95-a9184440d53b.png)

------------------------------------

##  잘못된 예시 1)
하위 폴더들과 함께 자료가 있으면 안됩니다.

![image](https://user-images.githubusercontent.com/22446076/117937722-4530bc00-b341-11eb-9108-27f94a927c7d.png)


## 잘못된 예시 2)
하위 폴더 밑에 또 다른 하위 폴더가 있으면 안됩니다.

![image](https://user-images.githubusercontent.com/22446076/117937762-4cf06080-b341-11eb-99f4-c5e0ae6902cd.png)


## 잘못된 예시 3)
사진이 아닌 파일이 있으면 안됩니다.

![image](https://user-images.githubusercontent.com/22446076/117937834-5d084000-b341-11eb-8016-3304ea318183.png)

----------------------------------

# 사용법 :

![image](https://user-images.githubusercontent.com/22446076/117937907-6ee9e300-b341-11eb-9f09-d589d339b79c.png)


target directory는 만들고자 하는 자료들을 가지는  상위 폴더의 경로입니다.

위의 자료 예시를 든 사진에서는 'C:\Users\user\Downloads\Test'가 되겠습니다.

경로를 입력하고 Return을 누릅니다.

save directory는 저장하고자 하는 경로를 의미합니다.

경로를 입력하고 Return을 누르면 PPT가 만들어집니다.

저장하고자 하는 경로에 PPT가 만들어진 것을 확인하면 프로그램을 종료해주시기 바랍니다.


-----------------
## 예시)

![image](https://user-images.githubusercontent.com/22446076/117937929-7610f100-b341-11eb-875e-eb691eca3842.png)

![image](https://user-images.githubusercontent.com/22446076/117937946-79a47800-b341-11eb-9d42-b8a69527d33d.png)


-----------------------
## 결과 :
![image](https://user-images.githubusercontent.com/22446076/117937957-7dd09580-b341-11eb-8536-fc25630470e4.png)

PPT파일이 생성되었습니다.

![image](https://user-images.githubusercontent.com/22446076/117937977-81641c80-b341-11eb-815e-147f96fa0312.png)

---------------------
슬라이드의 순서는 

> '상위폴더 제목 - 1번 하위폴더 제목 - 사진 자료 - 2번 하위폴더 제목 - 사진 자료' 순서입니다.

사진의 크기는 정사각형으로 맞추어 비율이 안맞을 수 있습니다. \
제대로 동작이 되지 않는 경우엔 위의 잘못된 예시를 확인해 주시기 바랍니다.\
사진이 수백장이 넘어가는 경우 분단위의 시간이 소모될 수 있습니다.\
로그에 에러가 남지 않았다면 기다려주시기 바랍니다. \

2022.01.27 버그픽스, 프로그래스바 로그에 출력
