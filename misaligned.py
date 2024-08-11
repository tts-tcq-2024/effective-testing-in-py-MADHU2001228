def get_color_map_data():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    data = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            data.append((i * 5 + j, major, minor))
    return data


def test_get_color_map_data():
    data = get_color_map_data()

    
    assert len(data) == 25, "Incorrect number of items"


    for index, major, minor in data:
        assert isinstance(index, int), "Index should be an integer"
        assert isinstance(major, str), "Major color should be a string"
        assert isinstance(minor, str), "Minor color should be a string"

   
    expected_major_colors = {"White", "Red", "Black", "Yellow", "Violet"}
    expected_minor_colors = {"Blue", "Orange", "Green", "Brown", "Slate"}
    actual_major_colors = set(major for _, major, _ in data)
    actual_minor_colors = set(minor for _, _, minor in data)

    assert expected_major_colors == actual_major_colors, "Major colors mismatch"
    assert expected_minor_colors == actual_minor_colors, "Minor colors mismatch"


test_get_color_map_data()
print("All tests passed.")
