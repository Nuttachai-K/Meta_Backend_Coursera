def hanoi(disks,source,temp,destination):
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, temp)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, temp, source, destination)

disks = int(input("Number of Disk : "))

hanoi(disks,'A','B','C')