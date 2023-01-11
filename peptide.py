print("\n") #Prints a blank line space to make output clearer

# An ANSI escape sequence is used below with "\033[1m" and "\033[0m" where any script written between the start and the end of the sequence will be in bold
print ('\033[1mSolid Phase Peptide Synthesis Calculator:  \033[0m')

print("- At it's current stage the calculator can only process single-letter code abbreviation for amino acids so please use that format instead of three-letter abbreviations")

print("\n")

#PEPTIDE WEIGHT CALCULATOR

print ('\033[1m  Peptide Molecular Weight:  \033[0m')

# Creating an amino acid dictionary that contains the molecular weight for each single letter abbreviated amino acid. The keys are the single letter abbreviations and the values are the molecular weights.
peptide_dict = {
    "A":89.0932,
    "R":174.2010,
    "N":132.1179,
    "D":133.1027,
    "C":121.1582,
    "E":147.1293,
    "Q":146.1445,
    "G":75.0641,
    "H":155.1546,
    "I":131.1729,
    "L":131.1729,
    "K":146.1876,
    "M":149.2113,
    "F":165.1891,
    "P":115.1305,
    "S":105.0926,
    "T":119.1192,
    "W":204.2252,
    "Y":181.1885,
    "V":117.1486,
}

#Creating a second dictionary where the molecular weight of water is subtracted from the amino acid molecular weights to account for amide bond formation in the peptide. This is done using a loop to assign the "key" as the same key in the original dictionary and by using the original keys to find the correlating values to alter.
molecular_weight_water = 18.01528
peptide_residues={key:peptide_dict[key] - molecular_weight_water for key in peptide_dict}

#Use an input function to obtain the peptide sequence as a string. An "upper" function is also added to convert any lower case letters to upper case.
peptide_sequence_raw=input("Input your peptide sequence and press enter(E.g CHECK): ")
peptide_sequence=peptide_sequence_raw.upper()

#Use a the "*" function to unpack the string into a list of seperate characters.
amino_acid_list=[*peptide_sequence]

#Creating an empty list of amino acid weights and then using a loop and "ammend" function to add molecular weight values to the list using the unpacked peptide sequence "amino_acid_list" as the keys for the values.
amino_acid_weights = []
for idx in amino_acid_list:
    amino_acid_weights.append(peptide_residues[idx])

# Summing the amino acid molecular weights and using the "round" function to round to 2dp. The addition of the molecular weight of water is nescessary as the amino acids found on the N-terminus and C-terminus are not bonded via an amide bond.
peptide_molecular_weight=round(sum(amino_acid_weights)+molecular_weight_water,2)

#F string used to display output of molecular weight for peptide sequence.
print(f"The molecular weight of {peptide_sequence} is {peptide_molecular_weight}g/mol!")

#RESIN LOADING CALCULATION

print("\n")
print ('\033[1m  Resin Loading:  \033[0m')

#Input functions used to get molar scale of reaction and resin loading value
mole_scale_string=input("What is the molar scale of your reaction in millimole? (Value only, E.g 0.05 or 0.1): ")

resin_loading_string=input("What is the resin loading capacity of your resin in millimole per gram? (Value only, between 0.1 - 5, E.g 0.5 or 1): ")

#Input function above gives a string output. A conversion using the "float" function is nescessary to get a numerical input value for calculations
mole_scale= float(mole_scale_string)
resin_loading= float(resin_loading_string)

#Using inputted values for calcution of mass of resin
resin_mass = (mole_scale/resin_loading)*1000
print(f"The amount of resin needed for the reaction is {resin_mass}mg!")

print("\n")

print ('\033[1m  Percentage Yield:  \033[0m')

#PERCENTAGE YIELD CALCULATION

#Using resin mass needed, resin loading value and peptide molecular weight to calculate theoretical yield
theoretical_yield = round((resin_mass*resin_loading*peptide_molecular_weight)/1000,2)
print(f"The theoretical yield of the reaction is {theoretical_yield}mg!")

#Input function for the actual yield of product obtained from synthesis
actual_yield_raw=input("What is the actual yield of peptide product obtained in milligram? (Value only, E.g Try inputting half the mass of the theorical yield): ")

#Conversion to float value followed by calculation to give percentage yield of reaction
actual_yield= float(actual_yield_raw)
percentage_yield= round((actual_yield/theoretical_yield)*100,2)

print(f"The percentage yield of the reaction is {percentage_yield}%!")

print("\n")