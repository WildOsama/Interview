Use the attached files in data.zip to write a short program in your programming language of choice (bash, python,...) that computes and outputs the exfoliation energies of 2D Fe2O3 (hematene) from them (i) for a non-relaxed (static) slab, (ii) when relaxing the ions (relaxed_ions) and (iii) when relaxing both ions and cell (relaxed_ions_and_cell).
Hints: You can find the definition of the exfoliation energy in the Methods section of the attached publication “Friedrich_NanoLett_2022.pdf”.
The energy of the 2D slab can be obtained from the OSZICAR file with the appropriate name as the entry following “E0=“ (last line).
The energy of the bulk system can be retrieved from “OSZICAR.Fe2O3_bulk.xz” as the entry following “E0=“.
The in-plane surface area of the 2D system can be obtained from the Bravais matrix at the top (lines 3 to 5) in file “POSCAR.Fe2O3_2D_slab.xz”.
Please put appropriate comments into your code and provide the necessary instructions for using it if necessary. I will not fix the code if it doesn’t work.
You can check your results from the values in the tables at the end of the Supporting Information “Friedrich_NanoLett_2022_SI” when comparing to results from PBE+U.
