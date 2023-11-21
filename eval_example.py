import math

class ExcelFunctions:
    @staticmethod
    def sum(*args):
        return sum(args)
    
    @staticmethod
    def average(*args):
        return sum(args) / len(args)
    
    @staticmethod
    def max(*args):
        return max(args)
    
    @staticmethod
    def min(*args):
        return min(args)
    
    @staticmethod
    def sqrt(number):
        return math.sqrt(number)

def evaluate_excel_function(expression):
    # Reemplaza las funciones de Excel con los métodos correspondientes de la clase ExcelFunctions
    expression = expression.replace("SUM", "ExcelFunctions.sum")
    expression = expression.replace("AVERAGE", "ExcelFunctions.average")
    expression = expression.replace("MAX", "ExcelFunctions.max")
    expression = expression.replace("MIN", "ExcelFunctions.min")
    expression = expression.replace("SQRT", "ExcelFunctions.sqrt")
    
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print("Error al evaluar la expresión:", e)

# Ejemplo de uso
expression = "SUM(1, 2, 3, 4, 5)"
result = evaluate_excel_function(expression)
print(result)  # Output: 15

expression = "AVERAGE(1, 2, 3, 4, 5)"
result = evaluate_excel_function(expression)
print(result)  # Output: 3.0

expression = "MAX(1, 2, 3, 4, 5)"
result = evaluate_excel_function(expression)
print(result)  # Output: 5

expression = "MIN(1, 2, 3, 4, 5)"
result = evaluate_excel_function(expression)
print(result)  # Output: 1

expression = "SQRT(16)"
result = evaluate_excel_function(expression)
print(result)  # Output: 4.0
