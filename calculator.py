from dataclasses import dataclass
import re
import math

@dataclass
class Calculator:
    expression: str

    def sanitize(self) -> str:
        # Allow only digits, operators, decimal, brackets, and supported words
        return re.sub(r'[^0-9+\-*/().%^a-zA-Z]', '', self.expression)

    def evaluate(self) -> str:
        expr = self.sanitize()
        expr = expr.replace('^', '**')  # Replace ^ with Python power operator

        # Safe math context
        allowed = {
            'sqrt': math.sqrt,
            'cbrt': lambda x: x ** (1/3),
            'log': math.log10,
            'ln': math.log,
            'pi': math.pi,
            'e': math.e,
        }

        try:
            result = eval(expr, {"__builtins__": None}, allowed)
            return str(result)
        except Exception:
            return "Error"
