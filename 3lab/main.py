class Journal:
    def __init__(self):
        self.log = []
        
    def evaluate(self, expr: str):
        expr = expr.replace(" ", "") 
        result = self._eval(expr)
        return result

    def _eval(self, expr: str):
        self.log.append(f"Начинаем вычислять: {expr}")
        if self._is_wrapped(expr):
            return self._eval(expr[1:-1])

        pos = self._find_main_operator(expr, ['+', '-'])
        if pos != -1:
            left = expr[:pos]
            op = expr[pos]
            right = expr[pos+1:]
            left_val = self._eval(left)
            right_val = self._eval(right)
            result = left_val + right_val if op == '+' else left_val - right_val
            self.log.append(f"{left} {op} {right} = {result}")
            return result

        pos = self._find_main_operator(expr, ['*', '/'])
        if pos != -1:
            left = expr[:pos]
            op = expr[pos]
            right = expr[pos+1:]
            left_val = self._eval(left)
            right_val = self._eval(right)
            result = left_val * right_val if op == '*' else left_val / right_val
            self.log.append(f"{left} {op} {right} = {result}")
            return result

        value = float(expr)
        self.log.append(f"Число: {value}")
        return value

    def _is_wrapped(self, expr: str):
        if not (expr.startswith("(") and expr.endswith(")")):
            return False

        depth = 0
        for i in range(len(expr)):
            if expr[i] == '(':
                depth += 1
            elif expr[i] == ')':
                depth -= 1

            if depth == 0 and i < len(expr) - 1:
                return False
        return True

    def _find_main_operator(self, expr: str, operators):
        depth = 0
        for i in range(len(expr) - 1, -1, -1): 
            c = expr[i]
            if c == ')': depth += 1
            elif c == '(': depth -= 1
            elif depth == 0 and c in operators:
                return i
        return -1

#Пример использования
evaluator = Journal()
expression = '2 + (3 * (4 - 1))'
result = evaluator.evaluate(expression)
print("Результат:", result)
print("\nЖурнал вызовов:")
for entry in evaluator.log:
    print(entry)


