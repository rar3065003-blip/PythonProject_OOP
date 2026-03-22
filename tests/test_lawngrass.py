import pytest

from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


def test_lawngrass_init(lawngrass_1: LawnGrass) -> None:
    assert lawngrass_1.name == "Газонная трава"
    assert lawngrass_1.description == "Элитная трава для газона"
    assert lawngrass_1.price == 500.0
    assert lawngrass_1.quantity == 20
    assert lawngrass_1.country == "Россия"
    assert lawngrass_1.germination_period == "7 дней"
    assert lawngrass_1.color == "Зеленый"


def test_lawngrass_add(lawngrass_1: LawnGrass, lawngrass_2: LawnGrass) -> None:
    assert lawngrass_1 + lawngrass_2 == 16750.0


def test_lawngrass_wrong_add(smartphone_1: Smartphone, lawngrass_1: LawnGrass) -> None:
    with pytest.raises(TypeError):
        assert smartphone_1 + lawngrass_1


def test_demo_work_print(lawngrass_1: LawnGrass) -> None:
    assert str(lawngrass_1) == (
        "Газонная трава, 500.0 руб. Остаток: 20 шт. Страна: Россия, Срок прорастания: " "7 дней, Цвет: Зеленый"
    )
