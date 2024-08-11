def generate_color_map_data():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    data = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            data.append(f'{i * 5 + j} | {major} | {minor}')
    return data

def format_color_map_data(data):
    return "\n".join(data)

def test_print_color_map():
  
    expected_output = format_color_map_data(generate_color_map_data())

    actual_output = print_color_map()


    assert actual_output == expected_output, (
        f"Expected output:\n{expected_output}\n\nBut got:\n{actual_output}"
    )


test_print_color_map()
print("All tests passed.")
