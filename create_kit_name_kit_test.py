import sender_stand_request
import data



def positive_assert(kit_body):
    response = sender_stand_request.create_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body

def negative_assert_code_400(kit_body):
    response = sender_stand_request.create_kit(kit_body)
    assert response.status_code == 400

#prueba 1
def test_create_kit_with_name_length_1_should_return_status_201_and_correct_name():
    positive_assert(data.one_letter)

#prueba 2
def test_create_kit_with_name_length_511_should_return_status_201_and_correct_name():
    positive_assert(data.max_length_name)

#prueba 3
def test_create_kit_with_empty_name_should_return_status_400():
    negative_assert_code_400(data.empty_string)

#prueba 4
def test_create_kit_with_name_length_512_should_return_status_400():
    negative_assert_code_400(data.too_long_name)

#prueba 5
def test_create_kit_with_name_including_special_characters_should_return_status_201_and_correct_name():
    positive_assert(data.special_characters)

#prueba 6
def test_create_kit_with_name_including_spaces_should_return_status_201_and_correct_name():
    positive_assert(data.spaces_name)

#prueba 7
def test_create_kit_with_name_including_numbers_should_return_status_201_and_correct_name():
    positive_assert(data.numbers_string)

#prueba 8
def test_create_kit_with_no_name_parameter_should_return_status_400():
    negative_assert_code_400(data.none_value)

#prueba 9
def test_create_kit_with_name_as_number_should_return_status_400():
    negative_assert_code_400(data.numeric_value)