from src.utils import read_json


def test_read_json() -> None:
    test_file = "data\\products.json"
    data = read_json(test_file)

    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["description"] == (
        "Смартфоны, как средство не только коммуникации," " но и получение дополнительных функций для удобства жизни"
    )
    assert data[0]["name"] == "Смартфоны"
