# CalculationDataClassモジュール内のCCalcDataクラスを読み込む
from CalculationDataClass import CCalcData
### 他のimport方法
# CalculationDataClassモジュール内の全クラスを読み込む
# from CalculationDataClass import *

# CalculationDataClassモジュール内のA, Bクラスを読み込む
# from CalculationDataClass import A, B

obj = CCalcData("sample.txt")
obj.read()

print(obj.data)
print(obj.calc())

obj.update(lambda x: int(x * 2), True)
print(obj.data)

print(obj.calc())

obj.write()

print("end.")
