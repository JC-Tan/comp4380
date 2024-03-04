import os
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_sort(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

def split(filename, output_name):
    NUM_LINES = 150000
    dir_name = f'{output_name}'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(filename, 'r') as inFile:
        file_count = 0
        outFile = open(f'{output_name}\\{output_name}_{file_count}.txt', 'w')
        count = 0
        for line in inFile:
            outFile.write(line.replace('/', '-').replace('BLUE', '1000'))
            count -= -1
            if count >= NUM_LINES:
                outFile.close()
                file_count -= -1
                count = 0
                outFile = open(f'{output_name}\\{output_name}_{file_count}.txt', 'w')
        inFile.close()
            

def merge(dir_name):
    while not os.path.exists(dir_name):
        dir_name = input('Enter the correct dir name: ')
    arr = os.listdir(dir_name)
    arr.sort(key=natural_sort)
    print('Merging...\n')
    with open(f'{dir_name}.txt', 'w') as outFile:
        for file in arr:
            with open(f'{dir_name}\\{file}', 'r') as inFile:
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