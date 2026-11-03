"""Расчёт площади и периметра прямоугольника."""


def check_sides(width, height):
    """Проверяет, что стороны неотрицательные."""
    if width < 0 or height < 0:
        raise ValueError("Стороны не могут быть отрицательными")


def area(width, height):
    """Возвращает площадь прямоугольника."""
    check_sides(width, height)
    return width * height


def perimeter(width, height):
    """Возвращает периметр прямоугольника."""
    check_sides(width, height)
    return 2 * (width + height)


if __name__ == "__main__":
    # Пример: прямоугольник 3 x 4
    print(area(3, 4))       # площадь: 12
    print(perimeter(3, 4))  # периметр: 14
