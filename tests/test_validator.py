from hexlet_code.validator.validator import Validator


def test_validator():
    v = Validator()

    schema = v.string()
    schema2 = v.string()  # schema != schema2

    assert schema != schema2
    assert schema.is_valid('') == True  # True

    assert schema.is_valid(None) == True  # True

    assert schema.is_valid('what does the fox say')  # True

    schema.required()

    assert schema2.is_valid('') == True  # True
    assert schema.is_valid(None) == False  # False
    assert schema.is_valid('') == False
    assert schema.is_valid('hexlet') == True  # True

    assert schema.contains('what').is_valid('what does the fox say') == True
    assert schema.contains('whatthe').is_valid('what does the fox say')  == False

    assert v.string().min_len(10).min_len(4).is_valid('Hexlet') == True
