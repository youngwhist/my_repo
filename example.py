"""Расчёт площади и периметра прямоугольника."""


def area(width, height):
    """Возвращает площадь прямоугольника."""
    return width * height


def perimeter(width, height):
    """Возвращает периметр прямоугольника."""
    return 2 * (width + height)


if __name__ == "__main__":
    # Пример: прямоугольник 3 x 4
    print(area(3, 4))       # площадь: 12
    print(perimeter(3, 4))  # периметр: 14
