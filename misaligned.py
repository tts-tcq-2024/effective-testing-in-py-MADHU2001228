
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    
    # Print header
    print(f'Index | Major Color | Minor Color')
    print('-' * 30)  # Print a separator line
    
    # Print each color combination with proper formatting
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            index = i * len(minor_colors) + j
            print(f'{index: <5} | {major: <11} | {minor: <10}')
    
    return len(major_colors) * len(minor_colors)

result = print_color_map()
assert(result == 25)
print("All is well (maybe!)\n")

