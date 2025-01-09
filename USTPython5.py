def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * pow(base, exponent - 1)
    
base_number = int(input("Enter the base: "))
exponent_number = int(input("Enter the exponent: "))
result = power(base_number, exponent_number)
print(f"The Answer is {result}")


def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)

disks = int(input("Enter the number of disks"))
source = input("Enter the source: ")
destination = input("Enter the destination: ")
auxiliary = input("Enter the auxiliary: ")
result = tower_of_hanoi(disks, source, destination, auxiliary)
print(result)