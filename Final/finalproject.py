import sympy as sp

# Введение уравнения
x = sp.Symbol('x')
expr = sp.sin(x)**2-sp.cos(x)**2
expr

# Решение производной
expr_diff = sp.diff(expr)
expr_diff

# Определить корни
expr_solve = sp.solve(expr)
expr_solve

# Найти интервалы на которых функция возрастает
rise_exp = sp.solve(expr_diff > 0)
rise_exp

# Найти интервалы, на которых функция убывает
fall_exp = sp.solve(expr_diff < 0)
fall_exp

# Построить график
graph = sp.plot(expr)

# Вычислить вершину
peak_exp = sp.solve(expr_diff)
peak_exp

# Определить промежутки, на котором f > 0
peak_exp_origin = sp.solve(expr > 0)
peak_exp_origin

# Определить промежутки, на котором f < 0
fall_exp_origin = sp.solve(expr < 0)
fall_exp_origin
