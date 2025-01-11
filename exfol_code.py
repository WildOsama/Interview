from typing import Tuple

import numpy as np

# Job files for energies and in-plane surface area:
IONS_FILE = "OSZICAR.Fe2O3_2D_slab_relaxed_ions"
STATIC_FILE = "OSZICAR.Fe2O3_2D_slab_static"
IONS_CELL_FILE = "OSZICAR.Fe2O3_2D_slab_relaxed_ions_and_cell"
BULK_FILE = "OSZICAR.Fe2O3_bulk"
MATRIX_FILE = "POSCAR.Fe2O3_2D_slab"

def final_calculation(
    ions_filename: str,
    static_filename: str,
    ions_cell_filename: str,
    bulk_filename: str,
    matrix_filename: str,
) -> Tuple[float, float, float]:
    
    """Main function for calculations of energies. 
    
    This function consists the following steps:
        1. Extraction energies from VASP OSZICAR files;
        2. Extraction Bravais matrix and calculation in-plane surface area of the 2D system;
        3. Calculation Exfoliation Energies for ions, static and ions_cell cases.
        
    """

    print("Extract energy from files")
    ions = extract_energy(ions_filename)
    static = extract_energy(static_filename)
    ions_cell = extract_energy(ions_cell_filename)
    bulk = extract_energy(bulk_filename)

    print('Extract Bravais matrix from POSCAR, calculate in-plane surface area')
    surface = calc_surface_area(matrix_filename)

    print('Calculate Exfoliation Energies')
    ions_res = exfol_energy(ions, bulk, surface)
    static_res = exfol_energy(static, bulk, surface)
    ions_cell_res = exfol_energy(ions_cell, bulk, surface)

    return static_res, ions_res, ions_cell_res


### Additional functions ###


def extract_energy(filename: str) -> float:
    """Energy extraction from OSZICAR file."""

    with open(filename, "r") as f:
        last_line = f.readlines()[-1]
        words = last_line.split()
        energy = float(words[4])

    return energy


def calc_surface_area(filename: str) -> float:
    """Vectors extraction and calculation the surface area of Fe2O3."""

    lat_mat = np.zeros((3, 3))
    with open(filename, "r") as f:
        lines = f.readlines()
        for component in range(3):
            lat_mat[component, :] = list(
                map(float, lines[2 + component].strip().split())
            )
    v1 = lat_mat[0, :]
    v2 = lat_mat[1, :]
    surface_area = np.linalg.norm(np.cross(v1, v2))

    return surface_area


def exfol_energy(slab: float, bulk: float, surface: float) -> float:
    """Calculation of Exfoliation Energy."""

    return (slab - bulk) / surface


# Start the calculation of Exfoliation Energies for Fe2O3:
if __name__ == "__main__":
    static_res, ions_res, ions_cell_res = final_calculation(
        IONS_FILE, STATIC_FILE, IONS_CELL_FILE, BULK_FILE, MATRIX_FILE
    )
    print("### Exfoliation Energies for Fe2O3 (Method: PBE+U) ###")
    print(
        f"static = {static_res:.3f} eV/A; ions = {ions_res:.3f} eV/A; ions_cell = {ions_cell_res:.3f} eV/A."
    )
