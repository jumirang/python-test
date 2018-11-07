# 디렉터리 다루기
import os
import glob

# print(os.getcwd()) # 현재 디렉터리
# print(os.listdir(os.getcwd())) # 현재 경로의 파일 및 디렉터리를 문자열 리스트로
# print(os.path.isdir("week4"))
# print(os.path.isfile("fileTest.py"))
# # os.mkdir("my")
# print(os.path.join(os.getcwd(), "my")) # 경로 join
# os.system('ls') # ls 커맨드 명령어 수행
# os.system('notepad')
# s = os.popen("ls").read() # 커맨드 실행에 대한 파일객체
# print(s)

# glob 파일을 필터링
print(glob.glob('*.py')) # 결과: ['fileTest.py', 'directoryTest.py']
print(glob.glob('[abc]*.py')) # a or b or c로 시작하는 파일 필터링
