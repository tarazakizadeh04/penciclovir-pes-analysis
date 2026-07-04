import os
import re

input_folder = r"C:\Users\Ahoura\Desktop\s-1369"
output_file = r'C:\Users\Ahoura\Downloads\my_code\D24.txt'

D23_pattern = re.compile(r"D24\s+(-?\d+\.\d+)")  
skipped_files = []
processed_count = 0

def extract_number(filename):
    match = re.search(r"\d+", filename)
    if match:
        return int(match.group())  
    else: return 0

file_list = sorted(os.listdir(input_folder), key=extract_number)

with open(output_file, "w", encoding="utf-8") as out:
    for filename in file_list:
        filepath = os.path.join(input_folder, filename)
        if os.path.isfile(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                    match = D23_pattern.search(content)  
                    if match:
                        extracted_value = match.group(1)
                        out.write(f"{filename}: {extracted_value}\n")
                        processed_count += 1
                    else:
                        skipped_files.append(filename)

                print(f"{filename}: match={match.group(1) if match else 'No match found'}") 
            
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                skipped_files.append(filename)

print(f"Total processed files: {processed_count}")
print(f"Skipped files ({len(skipped_files)}): {skipped_files}")
print(f"All extracted values saved to {output_file}")
print("Done! To quote Gaussian: Normal termination ;)")
