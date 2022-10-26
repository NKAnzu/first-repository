files = input().split()
print(list(map(lambda x:'00'+x if len(x.split(".")[0])==1 else '0'+x if len(x.split(".")[0])==2 else x  , list(map(str, files)))))
#파일 이름이 숫자 3개 , 앞에 0이 들어가는 형식 출력되게 만들어라
