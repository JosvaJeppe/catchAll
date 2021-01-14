

print("""
###############################################
This program will allow the user to enter a USA
state name, and it will return the populations
###############################################
""")

inFileName = "USA_POP.csv"

try:
    inFile = open(inFileName, "r")
except:
    print("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Trouble opening input file: {}
Program is ending
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""".format(inFileName))
    exit()

print("")

line = inFile.readline()
population_data = dict()

while line != "":
    line = line.strip()
    parts = line.split(',')
    population_data[parts[0]] = eval(parts[1])
    line = inFile.readline()

statePrompt = """
Please enter the name of a USA state.
Capitalize the first letter.
For instance ---> Mississippi
OR hit 'enter' key to quit
---> """

state = input(statePrompt)

while state != '':

    if state in population_data.keys():
        print("\n The population of {} is {}\n\n".format(state, population_data[state]))
    else:
        print("\nSorry {} is not a US state!\n".format(state))

    print("#################################")
    state = input(statePrompt)

print('############\nGood bye!\n#############')