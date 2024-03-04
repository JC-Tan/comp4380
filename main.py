import os
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_sort(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

def replace(line):
    bus_dict = {"/": "-", "BLUE": "1000", "S401" : "1401", "S402" : "1402", "S404" : "1404",
        "S405" : "1405", "S406" : "1406", "S408" : "1408", "S409" : "1409", "S410" : "1410",
        "S412" : "1412", "S413" : "1413", "S414" : "1414", "S416" : "1416", "S417" : "1417",
        "S418" : "1418", "S419" : "1419", "S420" : "1420", "S421" : "1421", "S422" : "1422", 
        "S425" : "1425", "S426" : "1426", "S427" : "1427", "S428" : "1428", "S429" : "1429",
        "S430" : "1430", "S431" : "1431", "S432" : "1432", "S433" : "1433", "S435" : "1435",
        "S436" : "1436", "S437" : "1437", "S438" : "1438", "S439" : "1439", "S440" : "1440",
        "S441" : "1441", "S442" : "1442", "S443" : "1443", "W203" : "1203", "W205" : "1205",
        "W240" : "1240", "I310" : "1310", "I309" : "1309", "S434" : "1434",
        }
    bus_dict = dict((re.escape(k), v) for k, v in bus_dict.items())
    pattern = re.compile("|".join(bus_dict.keys()))
    return pattern.sub(lambda m: bus_dict[re.escape(m.group(0))], line)

def split(filename, output_name):
    NUM_LINES = 150000
    dir_name = f'{output_name}'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(filename, 'r') as inFile:
        file_count = 0
        pathname = os.path.join(dir_name, f'{output_name}_{file_count}.txt')
        outFile = open(pathname, 'w')
        count = 0
        for line in inFile:
            outFile.write(replace(line))
            count -= -1
            if count >= NUM_LINES:
                outFile.close()
                file_count -= -1
                count = 0
                pathname = os.path.join(dir_name, f'{output_name}_{file_count}.txt')
                outFile = open(pathname, 'w')
        inFile.close()
            

def merge(dir_name):
    while not os.path.exists(dir_name):
        dir_name = input('Enter the correct dir name: ')
    arr = os.listdir(dir_name)
    arr.sort(key=natural_sort)
    print('Merging...\n')
    with open(f'{dir_name}.txt', 'w') as outFile:
        for file in arr:
            pathname = os.path.join(dir_name, file)
            with open(pathname, 'r') as inFile:
                for line in inFile:
                    if line != '\n':
                        outFile.write(line)
                inFile.close()
        outFile.close()


def main():
    cmd = input("Press:\n- 1 for split\n- 2 for merge\n")
    if cmd == '1':
        filename = input("Enter the filename (don't mess it up there's no error checking here): ")
        print('Splitting...')
        split(filename, filename[0:len(filename) - 4])
    elif cmd == '2':
        dir_name = input("Enter the directory name: ")
        merge(dir_name)
    print('Done.')

main()