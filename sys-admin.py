import os
import subprocess

print("-" * 20)
print("Latihan 1: os.system")
os.system("ls")

print("\n" + "-" * 20)
print("Latihan 2 & 3: subprocess.run dengan ls -l")
subprocess.run(["ls", "-l"])

print("\n" + "-" * 20)
print("Latihan 5: uname -a")
command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

print("\n" + "-" * 20)
print("Latihan 6: ps -x")
command = "ps"
commandArgument = "-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])