import sys
# sys.path.append("D:/Python/MakePPTX/code")
# 절대경로가 아닌 상대경로가 필요함
import code.PPTX_DataSet_Maker as pm

# def test_example():
#   assert 1
target_dir = "C:/Users/user/Downloads/Test"

f = pm.make_ppt()
f.pre_view(target_dir)