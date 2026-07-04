import os
import re

input_folder=r'C:\Users\Ahoura\Desktop\s-1369'
output_file = r"C:\Users\Ahoura\Downloads\my_code\out_dipole.txt"

dipole_pattern = re.compile(r"\|Dipole\s*=\s*(-?[\d\.]+),\s*(-?[\d\.]+),\s*(-?[\d\.]+)\|")

skipped_files = []
processed_count =0


def extract_number(filename):
    match = re.search(r"\d+", filename)
    return int(match.group()) if match else float('inf')

file_list = sorted(os.listdir(input_folder), key=extract_number)



with open(output_file, "w" , encoding='utf-8') as out :
    for filename in file_list:
        filepath = os.path.join(input_folder, filename)
        if os.path.isfile(filepath):
            try:
                with open(filepath, 'r' , encoding="utf-8") as f:
                    content = f.read()
                    matches= dipole_pattern.findall(content)
                    if matches:
                        for match in matches:
                            out.write(f"{filename}:{match[0]} , {match[1]} , {match[2]}\n")
                        processed_count +=1
                    else:
                        skipped_files.append(filename)
            except Exception as e:
                print(f"Error reading {filename} : {e}")
                skipped_files.append(filename)

print(f"Total processed files: {processed_count}")
print(f"Skipped files ({len(skipped_files)}): {skipped_files}")
print(f"All dipole moment values saved to {output_file}")
print("Done! To quote Gaussian: Normal termination ;)")
