from django.core.exceptions import ValidationError

MIN_PRICE_VALUE = 0
ERROR_MIN_PRICE = f'Цена не должна быть меньше {MIN_PRICE_VALUE}'


def validate_min_price(value):
    if value < MIN_PRICE_VALUE:
        raise ValidationError(
            ERROR_MIN_PRICE
        )
    return value
