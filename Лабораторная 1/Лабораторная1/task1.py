# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Printer:
    def __init__(self, page_size: str, num_pages: float):
        """
        Создание и подготовка к работе объекта "принтер"

        :param page_size: Формат страницы (A4, A3, A2)
        :param num_pages: Страницы в лотке принтера

        Примеры:
        >>> printer = Printer('A4', 200)  # инициализация экземпляра класса
        """
        if not isinstance(page_size, str):
            raise TypeError("неверный формат страницы. Форрмат: ('An')")
        if page_size not in ['A3', 'A4', 'A2']:
            raise ValueError("К сожалению, мы не сможем распечатать на листе такого формата")
        self.page_size = page_size

        if not isinstance(num_pages, int):
            raise TypeError("Количество траниц должно быть int ")
        if num_pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным числом")
        self.num_pages = num_pages

    def print_pages(self, page_size: str, num_pages: int) -> int:
        """
        Функция которая уменьшает количество страниц в принтере

        :return: сколько страниц осталось

        Примеры:
        >>> printer = Printer('A4', 100)
        >>> printer.print_pages('A4', 80)
        """
        ...

    def scan_pages(self, docs: int, max_pages = 10) -> None:
        """
        сканирование документов.
        param: docs - количество документов для сканирования
        param: max_pages - ограничение на количество документов
        :raise TypeError: Если количество страниц документов превышает ограничение, то вызываем ошибку

        Примеры:
        >>> printer = Printer('A3', 10)
        >>> printer.scan_pages(200, 400)
        """
        if not isinstance(docs,  int):
            raise TypeError("Должен быть тип int ")
        if docs < 0:
            raise ValueError("количество документов не может быть меньше 0")
        if docs > max_pages:
            raise ValueError("к сожалению, документ слишком большой для сканирования")
        if not isinstance(max_pages,  int):
            raise TypeError("Должен быть тип int ")
        if max_pages < 0:
            raise ValueError("ограничение не может быть меньше 0")
        ...

class Alien:
    def __init__(self, health: int, speed: int, power: int):
        """
        Создание и подготовка к работе объекта "пришелец"

        :param health: Здоровье пришельца
        :param speed: скорость пришельца
        :param speed: сила пришельца

        Примеры:
        >>> alien = Alien(90, 80, 20)  # инициализация экземпляра класса
        """
        if not isinstance(health, int):
            raise TypeError("Здоровье пришельца указывать числами")
        if health > 100 or health < 0:
            raise ValueError("Здоровье пришельца требуется указывать в промежутке от 0 до 100")
        self.health = health

        if not isinstance(speed, int):
            raise TypeError("Скорость пришельца указывать числами")
        if speed > 100 or speed < 0:
            raise ValueError("Скорость пришельца требуется указывать в промежутке от 0 до 100")
        self.speed = speed

        if not isinstance(power, int):
            raise TypeError("Силу пришельца указывать числами")
        if power > 100 or power < 0:
            raise ValueError("Силу пришельца требуется указывать в промежутке от 0 до 100")
        self.power = power


    def hunt(self, speed_prey: int, power_prey: int) -> bool:
        """
        Функция которая позволяет понять, сможет ли пришелец поймать добычу
        :param speed_prey: Здоровье добычи
        :param power_prey: Сила добычи
        :return: True, False

        Примеры:
        >>> alien = Alien(90, 90 , 90)
        >>> alien.hunt(30, 60)
        True
        """
        if not isinstance(speed_prey, int):
            raise TypeError("Скорость добычи  указывать числами")
        if speed_prey > 100 or speed_prey < 0:
            raise ValueError("скорость добычи требуется указывать в промежутке от 0 до 100")
        self.speed_prey = speed_prey

        if not isinstance(power_prey, int):
            raise TypeError("Cила добычи  указывать числами")
        if power_prey > 100 or power_prey < 0:
            raise ValueError("Cила добычи требуется указывать в промежутке от 0 до 100")
        self.power_prey = power_prey

        if self.speed_prey >= self.speed:
            return False
        elif self.power_prey >= self.power:
            return False

        return True

    def healing(self, add_health: int) -> int:
        """
        Функция которая позволяет понять, сможет ли пришелец поймать добычу
        :param add_health: Сколько здоровья прибавить пришельцу
        :return: сколько здоровья сейчас у пришельца
        Примеры:
        >>> alien = Alien(90, 90 , 90)
        >>> alien.healing(5)
        95
        """
        if not isinstance(add_health, int):
            raise TypeError("Прибавляемое здоровье указывать числами")
        if add_health > 100 :
            raise ValueError("Пришелец здоров")
        if add_health < 0:
            raise ValueError("Пришелец мертв")
        self.add_health = add_health
        return self.health + self.add_health

class Fridge:
    def __init__(self, temp: int, capacity: int, weight: int):
        """
        Создание и подготовка к работе объекта "холодильник"

        :param temp: температура внитри холодильника
        :param capacity: вместимость холодильника ( вмещает определенное количество продуктов)
        :param weight: вес холодильника

        Примеры:
        >>> fridge = Fridge(3, 80, 20)  # инициализация экземпляра класса
        """
        if not isinstance(temp, int):
            raise TypeError("Температуру указывать числами")
        if temp > 8 or temp < 2:
            raise ValueError("Температура внутри холодильника от 2 до 8 градусов")
        self.temp = temp

        if not isinstance(capacity, int):
            raise TypeError("Вместимость указывать числами")

        self.capacity = capacity

        if not isinstance(weight, int):
            raise TypeError("вес указывать числами")
        if weight > 100 or weight < 2:
            raise ValueError("Нет таких холодильников")
        self.weight = weight
    def accommodate(self, products: list) -> bool:
        """
        Функция которая позволяет понять, помещаются ли продукты в холодильник
        :param *args: продукты
        :return: помещается или нет
        Примеры:
        >>> fridge = Fridge(3, 3 , 90)
        >>> fridge.accommodate(['колбаса', 'сыр'])
        True
        """
        if not isinstance(products, list):
            raise TypeError("указывать в списке")

        self.products = products
        if len(self.products) <= self.capacity:
            return True
        return False
    def set_initial_temperature(self) -> int:
        """
        Функция возвращает начальную настройку температуры

        Примеры:
        >>> fridge = Fridge(3, 3 , 90)
        >>> fridge.set_initial_temperature()
        2
        """
        return 2
    def cost_of_delivery(self, distance: int) -> str:
        """
        Функция возвращает стоимость доставки холодильника по формуле: вес*расстояние*10рублей

        Примеры:
        >>> fridge = Fridge(3, 3 , 90)
        >>> fridge.cost_of_delivery(13)
        'стоимость доставки 11700 рублей'
        """
        if not isinstance(distance, int):
            raise TypeError("расстояние указывать в числах (км)")
        if distance <0:
            raise ValueError('должны быть целые числа')
        self.distance = distance
        if distance == 0:
            return (f'стоимость доставки {self.weight* 10} рублей')
        return (f'стоимость доставки {self.distance* self.weight* 10} рублей')







if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
