"""
    Напишите программу для
    проверки истинности утверждения
    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
    для всех значений предикат.
"""

print(not(0 or 0 or 0) == (not(0) and not(0) and not(0)))
print(not(0 or 0 or 1) == (not(0) and not(0) and not(1)))
print(not(0 or 1 or 0) == (not(0) and not(1) and not(0)))
print(not(0 or 1 or 1) == (not(0) and not(1) and not(1)))
print(not(1 or 1 or 1) == (not(1) and not(1) and not(1)))
print(not(1 or 0 or 1) == (not(1) and not(0) and not(1)))
print(not(1 or 0 or 0) == (not(1) and not(0) and not(0)))
print(not(1 or 1 or 0) == (not(1) and not(1) and not(0)))
