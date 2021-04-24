from myservice.utils.helpers import camelcase


def test_camelcase():
    assert camelcase("snake_to_camel_case") == "snakeToCamelCase"
