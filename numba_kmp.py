###
# Author: Menschikov Mikhail
# Date: 21.02.2024

from numba import njit

@njit
def kmp(sequence, pattern):
    # Алгоритм Кнута-Мориса-Пратта поиска подстроки в строке.
    # Разбор: https://www.youtube.com/watch?v=7g-WEBj3igk .
    #
    # Сложность алгоритма: O(n+m), где 
    # n - длина строки pattern;
    # m - длина строки sequence.

    # Первый этап: формирование массива pi
    pi = [0] * len(pattern)
    i, j = 1, 0 
    while i < len(pattern):
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
    n, m = len(pattern), len(sequence)
    while k < m:
        if sequence[k] == pattern[l]:
            k += 1
            l += 1
            if l == n:
                return "Образ найден"
        elif l == 0:
            k += 1
            if k == m:
                return "Образ отсутствует"
        else:
            l = pi[l-1]

#sequence = np.array([1,2,3,4,5,6,7,8])
#pattern = np.array([2,3,4,4])

#print(kmp(sequence, pattern))