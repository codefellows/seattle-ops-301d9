# Requirements:
  # The Python module "os" must be utilized.
  # At least three variables must be declared and referenced in Python.
  # The Python function print() must be used at least three times.
  # Include execution of the following bash commands inside your Python script:
    # whoami
    # ip a
    # lshw -short
    
# Script: Ops Challenge 06
# Author: Hexx King
# Date of last revision: 09/05/23
# Purpose: Bash in Python 

import subprocess

# Define three variables
command1 = "whoami"
command2 = "ifconfig"
command3 = "system_profiler SPHardwareDataType SPNetworkDataType"

# Execute the first bash command (whoami)
result1 = subprocess.check_output(command1, shell=True, text=True)
# Print the result of the first command
print("Result of 'whoami' command:")
print(result1)

# Execute the second bash command (ip a)
result2 = subprocess.check_output(command2, shell=True, text=True)
# Print the result of the second command
print("\nResult of 'ip a' command:")
print(result2)

# Execute the third bash command (lshw -short)
result3 = subprocess.check_output(command3, shell=True, text=True)
# Print the result of the third command
print("\nResult of 'lshw -short' command:")
print(result3)
