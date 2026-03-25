#==========================================
#              BOILERPLATE
# 
# Scaffolds a new algorithm entry:
#   src/<name>/
#     <name>.h       (declarations)
#     <name>.c       (implementation)
#     main.c         (demo / visualization)
#     CMakeLists.txt (build target)
#==========================================

import sys
import os
import re

#uses regex to validate the input name:
# if its valid, transforms it to be used in the header file definition
def is_name_valid(name):
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9-_]*$', name):
        print("\033[33minvalid name: only letters, numbers, underlines and hyphens are allowed!\nit must also start with a letter.\033[0m")
        exit(1)
    return name.replace('-', '_').upper()

if len(sys.argv) <= 1:
    print("\033[33mmissing argument: please provide the new algorithm's name!\033[0m")
    exit(1)

algo_name = sys.argv[1]
definition = is_name_valid(algo_name)



#create algo folder
os.makedirs("src/" + algo_name, exist_ok=True)
print(f"folder {algo_name} created successfully...")

#create empty algorithm C file
file = open(f"src/{algo_name}/{algo_name}.c", 'x')
print(f"file {algo_name}.c created successfully...")
file.close()

#create empty algorithm header file
with open(f"src/{algo_name}/{algo_name}.h", 'x') as file:
    file.write(f'#ifndef {definition}_H\n#define {definition}_H\n\n//declare functions and variables here\n\n#endif')
print(f"file {algo_name}.h created successfully...")

#create main file
with open(f"src/{algo_name}/main.c", 'x') as file:
    file.write(f'#include "{algo_name}.h"\n\nint main(void)\n{{\n     //test the algorithm here\n\n     return 0;\n}}\n')
print(f"file main.c created successfully...")

#create cmake file
with open(f"src/{algo_name}/CMakeLists.txt", 'x') as file:
    file.write(f'add_executable({algo_name} main.c {algo_name}.c)\n'
               f'target_include_directories({algo_name} PRIVATE ${{CMAKE_CURRENT_SOURCE_DIR}})\n')
print("CMake file created successfully.")



print("all done!")
