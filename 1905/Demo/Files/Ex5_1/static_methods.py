import math

class MathUtilInstance:

    def sin(self, val):
        return math.sin(val)
    
    def cos(self, val):
        return math.sin(val)
    
mui = MathUtilInstance()
print(mui.sin(1.3))
print(mui.cos(1.3))

class MathUtilStatic:
    @staticmethod
    def sin(val):
        return math.sin(val)
    @staticmethod
    def cos(val):
        return math.sin(val)
print(MathUtilStatic.sin(1.3))
print(MathUtilStatic.cos(1.3))

