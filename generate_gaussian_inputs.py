import numpy as np

x = "# hf/STO-2G"
y = """
0 1
 H              
 H                  1            B1
 N                  2            B2    1            A1
 C                  3            B3    2            A2    1            D1    
 N                  4            B4    3            A3    2            D2   
 H                  5            B5    4            A4    3            D3   
 C                  5            B6    4            A5    3            D4    
 O                  7            B7    5            A6    4            D5   
 C                  7            B8    5            A7    4            D6    
 C                  9            B9    7            A8    5            D7    
 N                  4           B10    3            A9    2            D8    
 N                  9           B11    7           A10    5            D9    
 C                 12           B12    9           A11    7           D10    
 H                 13           B13   12           A12    9           D11   
 N                 10           B14    9           A13    7           D12    
 C                 15           B15   10           A14    9           D13    
 H                 16           B16   15           A15   10           D14   
 H                 16           B17   15           A16   10           D15   
 C                 16           B18   15           A17   10           D16    
 H                 19           B19   16           A18   15           D17   
 H                 19           B20   16           A19   15           D18   
 C                 19           B21   16           A20   15           D19    
 H                 22           B22   19           A21   16           D20   
 C                 22           B23   19           A22   16           D21    
 C                 22           B24   19           A23   16           D22    
 O                 24           B25   22           A24   19           D23    
 O                 25           B26   22           A25   19           D24    
 H                 24           B27   22           A26   19           D25    
 H                 25           B28   22           A27   19           D26    
 H                 25           B29   22           A28   19           D27    
 H                 24           B30   22           A29   19           D28    
 H                 27           B31   25           A30   22           D29    
 H                 26           B32   24           A31   22           D30
"""

in_f = r"C:\Users\Ahoura\Downloads\my_code\2nd_matrix.csv"
out_f = r"C:\Users\Ahoura\Downloads\my_code\gaussian_files.csv"


M = []
with open(in_f, 'r') as f:
    for r in f:
        cl_r = r.replace('[', '').replace(']', '').strip().split(',')  
        M.append([float(v) for v in cl_r if v]) 
M = np.array(M)

with open(out_f, 'w') as f_out:
    b_count = M.shape[0] // 93 

    for b_idx in range(b_count): 
        for c_idx in range(M.shape[1]):
            t_strc = f"Test on Penciclovir structure number {b_idx * M.shape[1] + c_idx + 1}"

            
            f_out.write(x + "\n\n")
            f_out.write(t_strc + "\n\n" )
            f_out.write(y.strip() + "\n\n")

            s_r = b_idx * 93
            e_r = s_r + 93

            for i, r_idx in enumerate(range(s_r, e_r)):
                if i < 32: 
                    f_out.write(f"B{i + 1} {M[r_idx, c_idx]:.8f}\n")
                elif i < 63: 
                    f_out.write(f"A{i - 31} {M[r_idx, c_idx]:.8f}\n")
                else:  
                    f_out.write(f"D{i - 62} {M[r_idx, c_idx]:.8f}\n")

            
            f_out.write("\n")
