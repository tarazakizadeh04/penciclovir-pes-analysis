import os
import re

input_folder = r"C:\Users\Ahoura\Desktop\s-1369"
output_file = r"C:\Users\Ahoura\Downloads\my_code\out_Energy.txt"

skipped_files = []
processed_count = 0


def extract_number(filename):
    match = re.search(r"\d+", filename)
    return int(match.group()) if match else float('inf')


def extract_hf_energy(content):
    perfect_pattern = r"(-?\d{3}\.\d{7})"

    hf_pattern = re.compile(r"HF.*?(-?\d{3}\.\d{7})")
    match = hf_pattern.search(content)
    if match:
        return match.group(1)

    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'HF' in line and '=' in line:
            numbers_in_line = re.findall(r"-?\d+\.\d+", line)
            if numbers_in_line:
                current_number = numbers_in_line[-1]
                if re.match(perfect_pattern, current_number):
                    return current_number
                else:
                    if i + 1 < len(lines):
                        next_numbers = re.findall(r"-?\d+\.\d+", lines[i + 1])
                        if next_numbers:
                            combined = current_number + next_numbers[0]
                            combined_match = re.search(perfect_pattern, combined)
                            if combined_match:
                                return combined_match.group(1)
    return None


file_list = sorted(os.listdir(input_folder), key=extract_number)

with open(output_file, "w", encoding="utf-8") as out:
    for filename in file_list:
        filepath = os.path.join(input_folder, filename)
        if os.path.isfile(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                hf_value = extract_hf_energy(content)

                if hf_value:
                    out.write(f"{filename}: {hf_value}\n")
                    processed_count += 1
                else:
                    skipped_files.append(filename)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                skipped_files.append(filename)


print(f"Total processed files: {processed_count}")
print(f"Skipped files ({len(skipped_files)}): {skipped_files}")
print(f"All HF values saved to {output_file}")
print("Done! To quote Gaussian: Normal termination ;)")