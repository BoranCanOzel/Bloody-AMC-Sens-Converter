import webbrowser
from datetime import datetime

print("Universal AMC Sens Converter Made by PythonP Software.")
webbrowser.open('http://pythonp.xyz')  # Open the website


def apply_multipliers_to_movements(input_file_name, original_sens, new_sens):

    if not input_file_name.lower().endswith('.amc'):
        input_file_name += '.amc'

    x_multiplier = y_multiplier = original_sens / new_sens
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_name = f"{input_file_name.rsplit('.', 1)[0]}_modded_{current_time}.amc"

    try:
        with open(input_file_name, 'r', encoding='utf-16-le') as f:
            lines = f.readlines()
    except UnicodeError:
        print("Failed to open the file with UTF-16 LE encoding. Trying without specifying encoding...")
        with open(input_file_name, 'r') as f:
            lines = f.readlines()

    modified_lines = []
    for line in lines:
        if line.strip().startswith("MoveR"):
            parts = line.strip().split(" ")
            x, y = int(parts[1]), int(parts[2])
            modified_x = round(x * x_multiplier)
            modified_y = round(y * y_multiplier)
            modified_line = f"MoveR {modified_x} {modified_y}\n"
            modified_lines.append(modified_line)
        else:
            modified_lines.append(line)

    with open(output_file_name, 'w', encoding='UTF-16') as f:
        f.writelines(modified_lines)

    print(f"Modified file saved as: {output_file_name}")


input_file = input("Enter the name of your .amc file (without extension): ")
original_sens = float(input("What sensitivity was this script made for? "))
new_sens = float(input("What sensitivity do you want to convert it to? "))

apply_multipliers_to_movements(input_file, original_sens, new_sens)
