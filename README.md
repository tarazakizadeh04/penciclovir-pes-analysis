# Penciclovir PES & Spectral Analysis

This repository contains the Python scripts I developed for my Bachelor's thesis in physics at Tabriz University of Technology (Sahand). This project was also written up and submitted as a conference paper.

In this project, I studied the conformational behavior of penciclovir, which is an antiviral drug molecule. My main goal was to see how rotating two hydroxymethyl side groups changes the molecule's potential energy surface (PES), dipole moment, and IR spectrum. To do this, I changed two dihedral angles (D23 and D24) using 36 steps of 10 degrees. This scan generated 1369 different structures.

I did all the quantum chemical calculations with Gaussian 09 software, using the Hartree–Fock method and the STO-2G basis set. After that, I used these Python scripts to read the raw output files and plot the 3D surfaces.

---

## Scripts & Workflow

Here is how I designed the technical steps to process the data, from generating the inputs to making the final plots:

### 1. Preparing Structures & Matrix
* **`build_matrix.py`**: This script reads a file that has the internal coordinates table. I took this table from the Gaussian section called *"Summary of the optimized potential energy surface scan"*. 
    > *Note:* Before running this script, I had to clean the raw Gaussian table using Cygwin to remove the eigenvalues and row numbers.

### 2. Making Inputs & Running Gaussian
* **`generate_gaussian_inputs.py`**: This script takes the matrix from the previous step and automatically creates individual input files for Gaussian.
    * *The 1370 Structure Trick:* The script processes the structures in groups of 5. Because 1369 is not divisible by 5, the last 4 structures would normally be lost. To fix this, I added a 1370th dummy structure with all-zero coordinates. This allowed the script to save the final 4 structures safely.
    * *Splitting Files:* The script puts everything into one big file. Then, I used Cygwin/Linux commands to split this large file every 133 lines into small input files (`.gjf`). After that, I ran all 1369 inputs together using a bash script to do the Gaussian 09 calculations.

### 3. Extracting the Data
* **`extract_energy.py`**: This script searches through all 1369 Gaussian output files and uses a specific text pattern to find and list the final HF energy for each conformer.
* **`Extract_dipole.py` & `Calculate_dipole_value.py`**: `Extract_dipole.py` extracts the three raw parts ($x, y, z$) of the dipole moment for each structure. Then, `Calculate_dipole_value.py` uses those parts to calculate the total dipole moment value.
* **`extract_dihedral_D23.py`**: This script extracts the actual dihedral angles from the outputs. 
    > *Note:* If you want to find the D24 angle instead of D23, you can easily change the search pattern (regex) inside the code like this:  
    > `D24_pattern = re.compile(r"D24\s+(-?\d+\.\d+)")`

### 4. Cleaning Data with Cygwin
* **Data Filtering:** The text files created by the Python scripts include labels (for example: `penciclovir1: 8.2186655`). Before making the plots or calculations, I used Cygwin command-line tools to delete the structure names from the start of each line. This left only the clean numbers (like `8.2186655`) for the energy and dipole files.

### 5. Final 3D Plots
* **`plot_energy_surface.py`**: This script takes the clean energy numbers and plots them against the D23 and D24 dihedral angles to make the 3D Potential Energy Surface (PES).
* **`plot_dipole_surface.py`**: This script takes the calculated dipole values and plots them against the D23 and D24 angles to show the 3D dipole moment surface.

---

## What I Found

* **Potential Energy Surface (PES):** The 3D plot showed a few low-energy regions. I found exactly **one stable conformer (Structure 1345)** and **one transition state (Structure 944)**. The transition state had a higher energy and showed one imaginary frequency.
* **Dipole Moment & Charge:** Rotating the polar hydroxymethyl groups together changes how the electrical charge is distributed in the molecule. This alters both the size and direction of the electric dipole moment, showing that the electronic properties are sensitive to the molecular shape.
* **IR Spectra Analysis:** I compared the calculated infrared spectra of the stable conformer (1345) and the transition state (944):
    * The main stretching vibrations for **O–H, N–H, and C–H** bonds appear in very similar frequency areas in both structures. This means the basic chemical identity of the molecule does not change.
    * However, the **fingerprint region** is very sensitive to these shape changes. It showed clear differences in peak intensities and small frequency shifts because the vibrations inside the molecule changed.

---

## Conference Paper

I presented this research as a conference paper at the 7th Iranian Computational Physics Conference at Shahid Beheshti University (February 2, 2026).

> T. Zakizadeh, S. H. R. Shojaei, *Theoretical investigation of the effect of conformational changes on the potential energy surface and spectral properties of penciclovir*, Tabriz University of Technology (Sahand), 2026.

[View the full paper here](https://drive.google.com/drive/folders/1ONmrn7_JsXWvc1-YvDhtE7cWQpQUelWZ)
