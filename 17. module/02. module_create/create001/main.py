import CalculationDataModule

CalculationDataModule.read()

print(CalculationDataModule.data)
print(CalculationDataModule.calc())

CalculationDataModule.update(lambda x: int(x * 2), True)
print(CalculationDataModule.data)
print(CalculationDataModule.calc())

CalculationDataModule.write()
print("end.")
