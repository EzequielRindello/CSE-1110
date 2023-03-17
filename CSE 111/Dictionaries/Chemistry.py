class FormulaError(ValueError):
    """FormulaError is the type of error that the parse_formula
    function will raise if a formula is invalid.
    """


def parse_formula(formula, periodic_table_dict):
    """Convert a chemical formula for a molecule into a compound
    list that stores the quantity of atoms of each element
    in the molecule. For example, this function will convert
    "H2O" to [["H", 2], ["O", 1]] and
    "PO4H2(CH2)12CH3" to [["P", 1], ["O", 4], ["H", 29], ["C", 13]]
    """
    assert isinstance(formula, str), \
        "wrong data type for parameter formula; " \
        f"formula is a {type(formula)} but must be a string"
    assert isinstance(periodic_table_dict, dict), \
        "wrong data type for parameter periodic_table_dict; " \
        f"periodic_table_dict is a {type(periodic_table_dict)} " \
        "but must be a dictionary"

    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            start = index
            index += 1
            while index < len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elem_dict, symbol):
        return 0 if symbol not in elem_dict else elem_dict[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elem_dict = {}
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group_dict, index = parse_r(formula, index+1, level+1)
                quant, index = parse_quant(formula, index)
                for symbol in group_dict:
                    prev = get_quant(elem_dict, symbol)
                    curr = prev + group_dict[symbol] * quant
                    elem_dict[symbol] = curr
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table_dict:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table_dict:
                        index += 1
                    else:
                        raise FormulaError("invalid formula, "
                                           f"unknown element symbol: {symbol}",
                                           formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elem_dict, symbol)
                elem_dict[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    raise FormulaError("invalid formula, "
                                       "unmatched close parenthesis",
                                       formula, index)
                level -= 1
                index += 1
                break
            else:
                if ch.isdecimal():
                    # Decimal digit not preceded by an
                    # element symbol or close parenthesis
                    message = "invalid formula"
                else:
                    # Illegal character: [^()0-9a-zA-Z]
                    message = "invalid formula, illegal character"
                raise FormulaError(message, formula, index)
        if level > 0 and level >= start_level:
            raise FormulaError("invalid formula, "
                               "unmatched open parenthesis",
                               formula, start_index - 1)
        return elem_dict, index

    # Return the compound list of element symbols and
    # quantities. Each element in the compound list
    # will be a list in this form: ["symbol", quantity]
    elem_dict, _ = parse_r(formula, 0, 0)
    return list(elem_dict.items())


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    # set total molar mass to 0 to use it in iterations
    total_molar_mass = 0
    # Loop through the list of elements and the number of atoms they have
    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]
        # when the element' symbol is found/ searching in dictionary by keys(symbols)
        if symbol in periodic_table_dict:
            # need just the 'values' portion of a dictionary entry
            values = periodic_table_dict[symbol]
            atomic_mass = values[ATOMIC_MASS_INDEX]
            molar_mass = atomic_mass * quantity
        total_molar_mass += molar_mass

    # Return the total molar mass.
    return total_molar_mass


def make_periodic_table():
    periodic_table_list = {
        # [symbol, name, atomic_mass]
        "Ac": ["Actinium", 227],
        "Al": ["Aluminum", 26.9815386],
        'Sb': ['Antimony', 121.76],
        'Ar': ['Argon', 39.948],
        'As': ['Arsenic', 74.9216],
        'At': ['Astatine', 210],
        'Ba': ['Barium', 137.327],
        'Be': ['Beryllium', 9.012182],
        'Bi': ['Bismuth', 208.9804],
        'B': ['Boron', 10.811],
        'Br': ['Bromine', 79.904],
        'Cd': ['Cadmium', 112.411],
        'Ca': ['Calcium', 40.078],
        'C': ['Carbon', 12.0107],
        'Ce': ['Cerium', 140.116],
        'Cs': ['Cesium', 132.9054519],
        'Cl': ['Chlorine', 35.453],
        'Cr': ['Chromium', 51.9961],
        'Co': ['Cobalt', 58.933195],
        'Cu': ['Copper', 63.546],
        'Dy': ['Dysprosium', 162.5],
        'Er': ['Erbium', 167.259],
        'Eu': ['Europium', 151.964],
        'F': ['Fluorine', 18.9984032],
        'Fr': ['Francium', 223],
        'Gd': ['Gadolinium', 157.25],
        'Ga': ['Gallium', 69.723],
        'Ge': ['Germanium', 72.64],
        'Au': ['Gold', 196.966569],
        'Hf': ['Hafnium', 178.49],
        'He': ['Helium', 4.002602],
        'Ho': ['Holmium', 164.93032],
        'H': ['Hydrogen', 1.00794],
        'In': ['Indium', 114.818],
        'I': ['Iodine', 126.90447],
        'Ir': ['Iridium', 192.217],
        'Fe': ['Iron', 55.845],
        'Kr': ['Krypton', 83.798],
        'La': ['Lanthanum', 138.90547],
        'Pb': ['Lead', 207.2],
        'Li': ['Lithium', 6.941],
        'Lu': ['Lutetium', 174.9668],
        'Mg': ['Magnesium', 24.305],
        'Mn': ['Manganese', 54.938045],
        'Hg': ['Mercury', 200.59],
        'Mo': ['Molybdenum', 95.96],
        'Nd': ['Neodymium', 144.242],
        'Ne': ['Neon', 20.1797],
        'Np': ['Neptunium', 237],
        'Ni': ['Nickel', 58.6934],
        'Nb': ['Niobium', 92.90638],
        'N': ['Nitrogen', 14.0067],
        'Os': ['Osmium', 190.23],
        'O': ['Oxygen', 15.9994],
        'Pd': ['Palladium', 106.42],
        'P': ['Phosphorus', 30.973762],
        'Pt': ['Platinum', 195.084],
        'Pu': ['Plutonium', 244],
        'Po': ['Polonium', 209],
        'K': ['Potassium', 39.0983],
        'Pr': ['Praseodymium', 140.90765],
        'Pm': ['Promethium', 145],
        'Pa': ['Protactinium', 231.03588],
        'Ra': ['Radium', 226],
        'Rn': ['Radon', 222],
        'Re': ['Rhenium', 186.207],
        'Rh': ['Rhodium', 102.9055],
        'Rb': ['Rubidium', 85.4678],
        'Ru': ['Ruthenium', 101.07],
        'Sm': ['Samarium', 150.36],
        'Sc': ['Scandium', 44.955912],
        'Se': ['Selenium', 78.96],
        'Si': ['Silicon', 28.0855],
        'Ag': ['Silver', 107.8682],
        'Na': ['Sodium', 22.98976928],
        'Sr': ['Strontium', 87.62],
        'S': ['Sulfur', 32.065],
        'Ta': ['Tantalum', 180.94788],
        'Tc': ['Technetium', 98],
        'Te': ['Tellurium', 127.6],
        'Tb': ['Terbium', 158.92535],
        'Tl': ['Thallium', 204.3833],
        'Th': ['Thorium', 232.03806],
        'Tm': ['Thulium', 168.93421],
        'Sn': ['Tin', 118.71],
        'Ti': ['Titanium', 47.867],
        'W': ['Tungsten', 183.84],
        'U': ['Uranium', 238.02891],
        'V': ['Vanadium', 50.9415],
        'Xe': ['Xenon', 131.293],
        'Yb': ['Ytterbium', 173.054],
        'Y': ['Yttrium', 88.90585],
        'Zn': ['Zinc', 65.38],
        'Zr': ['Zirconium', 91.224],
    }
    return periodic_table_list


def main():
    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    # Also ask the user to  enter a chemical symbol to chek if it is in the table.
    print("Welcome! this calculator will help you with your problems :)")
    print("But first I must know that you understand what we are talking about")
    print("Do you know any chemical symbol?")
    while True:
        # Creates the periodic table
        periodic_table = make_periodic_table()
        symbol = input("Please enter a chemical symbol:  ")
        symbol = symbol.capitalize()
        # Check if the symbol is a key that is in the periodic_table dictionary.
        if symbol in periodic_table:
            # Find the data for the symbol that the user wants.
            valid = periodic_table[symbol]
            # Print the name and mass of the symbol.
            name = valid[NAME_INDEX]
            mass = valid[ATOMIC_MASS_INDEX]
            print("Well done ;)")
            print("The data of your chemical symbol is, ", end="")
            print(f"Name: {name} / Atomic mass: {mass} ")
            break
        else:
            print("Invalid input, please enter a valid symbol.")
    # Get a chemical formula for a molecule from the user.
    chemical_formula = input("Enter the molecular formula of the sample: ")
    # Get the mass of a chemical sample in grams from the user.
    while True:
        try:
            sample_mass = float(
                input("Enter the mass in grams of the sample: "))
            break
        except:
            print("An exception occurred. Please enter a float.")

    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    symbol_quantity_list = parse_formula(chemical_formula, periodic_table)
    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)
    # Print the molar mass.
    print(f"The molar mass is: {molar_mass:.5f}")
    # Print the number of moles.
    number_of_moles = sample_mass/molar_mass
    print(f"The number of moles is: {number_of_moles :.5f}")


if __name__ == "__main__":
    main()
