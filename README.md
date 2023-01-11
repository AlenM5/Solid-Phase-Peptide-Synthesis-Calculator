# Solid-Phase-Peptide-Synthesis-Calculator (v1)

Repository link: https://github.com/AlenM5/solid_phase_peptide_synthesis_calculator

This is an early stage calculator that uses Python to automate the time-consuming calculation components necessary for solid phase peptide synthesis (SPPS). 
At its current version (v1), the calculator allows calculation of the molecular weight of a desired peptide sequence, the mass of solid support resin needed for SPPS and the percentage yield of an SPPS reaction. 

To run the calculator:
1. Download the “peptide.py” script found in this repository
2. Open the script and the terminal 
3. Change the working directory to the file location of the script
4. Into the terminal, write “python peptide.py” and hit return
5. Follow the input prompt instructions shown in the terminal to receive output of calculation results

Script Notes:
- This SPPS calculator version only recognises single letter abbreviations, not three-letter abbreviations, of amino acids for a given peptide sequence. E.g it will recognise “CHECK” and not “CysHisGluCysLys”
- The input for peptide sequence is not case-sensitive and will recognise lower case letter abbreviations
- When prompted for a numerical value, only the value itself is needed (after manual conversion into the correct scale and unit stated). E.g When asked for the molar scale of the reaction in millimole an input of “0.1” will be recognised whilst an input of “0.1mmol” won’t be

Equations used:
- Amount of resin needed = (molar scale of reaction / resin loading capacity) * 1000
- Percentage yield = (actual yield of reaction / theoretical yield of reaction) * 100
