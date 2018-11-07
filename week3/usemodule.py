# python -m py_compile aa.py ==> aa.pyc
# import mymodule # py(소스레벨까지보여줌), pyc(컴파일한형태), pyd
#
# rst = mymodule.hap(10, 20)
# print(rst)
# rst = mymodule.gop(10, 20)
# print(rst)

# 파이썬 path와 모듈
# import sys
# sys.path.append('/Users/minseok/PycharmProjects/pythonTest/Test') # path 추가
# print(sys.path)

# from mymodule import hap, gop
from mymodule import *      # 모든 함수를 사용하겠다
rst = hap(10, 20)
print(rst)
rst = gop(10, 20)
print(rst)
