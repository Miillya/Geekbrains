# Задание №2
# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте
# его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».

# import cProfile
import math


# Вариант 1. Перебор.
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    j = 0
    while i * i <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    if j == 1:
        return False
    else:
        return True


def main(m):
    prime_count = 0

    if m <= 0:
        return 0
    if m < 6:
        n = 12
    else:
        n = math.floor(m * math.log(m * math.log(m)) + 2)
    i = 0
    while prime_count < m:
        if is_prime(i):
            prime_count += 1
        i += 1
    return i - 1

# timeit
# 100 loops, best of 5: 61.9 usec per loop      -10
# 100 loops, best of 5: 1.6 msec per loop       -100
# 100 loops, best of 5: 49.1 msec per loop      -1000
# 100 loops, best of 5: 1.72 sec per loop       -10000

# cProfile
# 37 function calls in 0.000 seconds        -10
# 549 function calls in 0.002 seconds       -100
# 7927 function calls in 0.047 seconds      -1000
# 104737 function calls in 1.956 seconds    -10000

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    1.955    1.955 <string>:1(<module>)
# 104730    1.863    0.000    1.863    0.000 task_2.py:12(is_prime)
# 1    0.092    0.092    1.955    1.955 task_2.py:26(main)
# 1    0.000    0.000    1.956    1.956 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {built-in method math.floor}
# 2    0.000    0.000    0.000    0.000 {built-in method math.log}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант 2. «Решето Эратосфена».
def eratosthenes(m):
    if m <= 0:
        return 0
    if m < 6:
        n = 12  # 2, 3, 5, 7, 11
    else:
        n = math.floor(m * math.log(m * math.log(m)) + 2)

    sieve = [j for j in range(n)]
    sieve[1] = 0

    for k in range(2, n):
        if sieve[k] != 0:
            j = k + k
            while j < n:
                sieve[j] = 0
                j += k
    res = [i for i in sieve if i != 0]
    # print(res)
    # print(res[m-1])
    return res[m - 1]

# timeit
# 100 loops, best of 5: 21.1 usec per loop      -10
# 100 loops, best of 5: 473 usec per loop       -100
# 100 loops, best of 5: 8.69 msec per loop      -1000
# 100 loops, best of 5: 141 msec per loop       -10000

# cProfile
# 9 function calls in 0.000 seconds     -10
# 9 function calls in 0.001 seconds     -100
# 9 function calls in 0.010 seconds     -1000
# 9 function calls in 0.132 seconds     -10000

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.002    0.002    0.155    0.155 <string>:1(<module>)
# 1    0.132    0.132    0.153    0.153 task_2.py:58(eratosthenes)
# 1    0.011    0.011    0.011    0.011 task_2.py:65(<listcomp>)
# 1    0.010    0.010    0.010    0.010 task_2.py:74(<listcomp>)
# 1    0.000    0.000    0.155    0.155 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {built-in method math.floor}
# 2    0.000    0.000    0.000    0.000 {built-in method math.log}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('eratosthenes(10000)')
