import numpy as np
import re  

n = []  




with open(r"C:\Users\Ahoura\Downloads\my_code\1st_matrix.csv", 'r') as f: 
    for l in f: 
        extracted = re.findall(r'-?\d+\.\d+', l.strip()) 
        n.extend(map(float, extracted))  

cols = 5 
rows = len(n) // cols  


M = np.array(n).reshape(rows, cols)  

out_f = r"C:\Users\Ahoura\Downloads\my_code\2nd_matrix.csv"
with open(out_f, 'w') as out:
    np.set_printoptions(suppress=True, precision=8, threshold=np.inf, linewidth=np.inf)
    out.write(np.array2string(M, separator=',', precision=8, suppress_small=False, formatter={'float_kind': lambda x: f'{x:.8f}'}))

print(f"Matrix has been written to {out_f} without truncation.")
