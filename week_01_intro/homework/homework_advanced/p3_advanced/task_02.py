"""
ДЗ презентации 3, повышенный уровень, задача 2.
Время: 25–35 минут.

Тема: O(n) поиск min и max.

Условие:
    Реализуйте функцию min_max(nums) -> (min_val, max_val)
    за O(n).

Пример:
    In: [3, 1, 4, 1, 5, 9, 2, 6]
    Out: (1, 9)
"""

def min_max(nums: list) -> tuple:
    """Найти минимум и максимум списка за один проход, O(n)."""
    min = nums[0]
    max = nums[0]
    for x in nums:
        if x < min:
            min = x
        if x > max:
            max = x
    return (min, max)
            

if __name__ == "__main__":
    assert min_max([3, 1, 4, 1, 5, 9, 2, 6]) == (1, 9)
    assert min_max([7]) == (7, 7)
    assert min_max([-5, -1, -10]) == (-10, -1)
    print("task_02 (p3 advanced): тесты пройдены")
