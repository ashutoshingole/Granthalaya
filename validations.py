def validate_alpha_only_string(test_string):
    test_string = test_string.replace(" ", "")
    return test_string.isalpha()


def validate_num_only_string(test_string):
    return test_string.isdigit()
