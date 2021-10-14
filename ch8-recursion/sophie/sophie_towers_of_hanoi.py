# In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide
# onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom
# (Le., each disk sits on top of an even larger one). You have the following constraints:
#
# Only one disk can be moved at a time.
# A disk is slid off the top of one tower onto another tower.
# A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using stacks.

# Using stacks (FILO), list structure, .append to add, .pop to remove

def main():
    num_of_disks = 3

    tower_1 = []
    tower_2 = []
    tower_3 = []

    # creating starting condition
    for i in range(num_of_disks, 0, -1):
        tower_1.append(i)


    disk = tower_1.pop()
    tower_3.append(disk)

    disk = tower_1.pop()
    tower_2.append(disk)

    disk = tower_3.pop()
    tower_2.append(disk)



    print("t1: ", tower_1)
    print("t2: ", tower_2)
    print("t3: ", tower_3)


if __name__ == "__main__":
    main()
