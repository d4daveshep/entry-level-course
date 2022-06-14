from platform import platform, machine, processor, system, version

# get the underlying OS
print("Platform is", platform())
print(platform(aliased=True, terse=False))
print(platform(False, True))
print("System is", system())
print("OS Version is", version())

# get the machine architecture
print("Machine is", machine())
print("Processor is", processor())

# Get the python version info
from platform import python_implementation, python_version_tuple

print("Python impl is", python_implementation())

for atr in python_version_tuple():
    print(atr, end=".")

