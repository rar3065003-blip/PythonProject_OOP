import pytest

from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


def test_smartphone_init(smartphone_1: Smartphone) -> None:
    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_1.price == 180000.0
    assert smartphone_1.quantity == 5
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"


def test_smartphone_add(smartphone_1: Smartphone, smartphone_2: Smartphone) -> None:
    assert smartphone_1 + smartphone_2 == 2580000.0


def test_smartphone_wrong_add(smartphone_1: Smartphone, lawngrass_1: LawnGrass) -> None:
    with pytest.raises(TypeError):
        assert smartphone_1 + lawngrass_1


def test_demo_work_print(smartphone_1: Smartphone) -> None:
    assert str(smartphone_1) == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт. Модель: S23 Ultra, " "Память: 256GB, Цвет: Серый"
    )
