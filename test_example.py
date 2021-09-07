import sys
sys.path.append("D:/Python/MakePPTX/code")
# 절대경로가 아닌 상대경로가 필요함
from .code import PPTX_DataSet_Maker

def test_example():
  assert 1
target_dir = "C:/Users/user/Downloads/Test"
def pre_view(target_dir) :
  assert pre_view(target_dir)