
def generate_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map.append(f'{i * 5 + j + 1:<2} | {major:<6} | {minor}')
    return color_map

def print_color_map():
    color_map = generate_color_map()
    for entry in color_map:
        print(entry)
    return len(color_map)

result = print_color_map()
assert(result == 25)
print("All is well (maybe!)\n")



def test_generate_color_map():
    color_map = generate_color_map()
    assert(len(color_map) == 25)  
    assert(color_map[0] == "1  | White  | Blue")  
    assert(color_map[24] == "25 | Violet | Slate")  
    assert(color_map[12] == "13 | Black  | Green")  

test_generate_color_map()
print("All tests passed!")

