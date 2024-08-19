import sys
import os

def input_Chris(txt):
    try:
        if (sys.version_info[0] < 3):
            return raw_input(txt).strip()
        else:
            sys.stdout.write(txt)
            return input()
    except:
        return False

print("""  
  [#] Create By ::
Chris List Splitter
""")

if len(sys.argv) != 4:
    yList = str(input_Chris('   Your List --> : '))
    maxi = int(input_Chris('   Maximum of every list --> : '))
else:
    yList = str(sys.argv[1])
    maxi = int(sys.argv[2])

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_list_path = os.path.join(parent_dir, yList)
output_list_dir = parent_dir

def run(input_list_path, maxi):
    sites = open(input_list_path, 'r')
    number = 1
    counter = 1
    for site in sites:
        try:
            site = site.strip()
            output_file_path = os.path.join(output_list_dir, f'list-{number}.txt')
            if counter <= maxi:
                with open(output_file_path, 'a') as f:
                    f.write(site + '\n')
                counter += 1
            else:
                os.system(f"start cmd /c rsf.py ../list-{number}.txt")
                number += 1
                output_file_path = os.path.join(output_list_dir, f'list-{number}.txt')
                with open(output_file_path, 'a') as f:
                    f.write(site + '\n')
                counter = 2
        except:
            pass
    os.system(f"start cmd /c rsf.py ../list-{number}.txt")
    print('\n   ./Done')

run(input_list_path, maxi)