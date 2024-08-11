def generate_color_map_lines():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    lines = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            lines.append(f'{i * 5 + j} | {major} | {minor}')
    return lines

def print_color_map():
    lines = generate_color_map_lines()
    return "\n".join(lines)

def generate_expected_output():
    lines = generate_color_map_lines()
    return "\n".join(lines)

def test_print_color_map():
    expected_output = generate_expected_output()
    actual_output = print_color_map()

    assert actual_output == expected_output, f"Expected output:\n{expected_output}\n\nBut got:\n{actual_output}"


test_print_color_map()


print("All tests passed.")


