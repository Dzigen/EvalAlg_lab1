###
# Author: Menschikov Mikhail
# Date: 21.02.2024

import taichi as ti
import numpy as np
ti.init(arch=ti.cpu)

@ti.kernel
def kmp(sequence: ti.types.ndarray(), pattern: ti.types.ndarray()) -> ti.i32:
    # Алгоритм Кнута-Мориса-Пратта поиска подстроки в строке.
    # Разбор: https://www.youtube.com/watch?v=7g-WEBj3igk .
    #
    # Сложность алгоритма: O(n+m), где 
    # n - длина строки pattern;
    # m - длина строки sequence.

    # Первый этап: формирование массива pi
    print(pattern.shape)
    pi = [0] * pattern.shape[0]
    i, j = 1, 0 
    while i < pattern.shape[0]:
        if pattern[i] == pattern[j]:
            pi[i] = j+1
            i+= 1
            j+= 1
        elif j == 0:
            pi[i] = 0
            i+= 1
        else:
            j = pi[j-1]

    # Второй этап: поиск образа pattern в строке sequence
    k, l = 0, 0
    n, m = pattern.shape[0], sequence.shape[0]
    flag = 0
    while k < m:
        if sequence[k] == pattern[l]:
            k += 1
            l += 1
            if l == n:
                # Подстрока найдена
                flag = 1
                break
        elif l == 0:
            k += 1
        else:
            l = pi[l-1]

    return 1 if flag else 0
    

#sequence = np.array([1,2,3,4,5,6,7,8])
#pattern = np.array([2,3,4,4])

#print(kmp(sequence, pattern))