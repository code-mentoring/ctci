# Towers of Hanoi.

import argparse

class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def peek(self, x):
        return self.items[-1]

    def empty(self):
        return len(self)==0

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return "{" + ",".join(str(x) for x in self.items) + "}"

    def __repr__(self):
        return str(self)

def solve_hanoi(N):
    towers = [Stack() for _ in range(3)]
    for k in reversed(range(1, N+1)):
        towers[0].push(k)
    print_towers(towers)
    move_disks(towers, N, 0, 2)

def move_disks(towers, n, i, j):
    if n == 1:
        move_disk(towers, i, j)
    else:
        k = 3 - i - j # this is the empty tower
        move_disks(towers, n-1, i, k)
        move_disk(towers, i, j)
        move_disks(towers, n-1, k, j)

def move_disk(towers, i, j):
    disk = towers[i].pop()
    assert towers[j].empty or disk < towers[j].peek()
    towers[j].push(disk)
    print_towers(towers)

def print_towers(towers):
    print(" | ".join(str(tower) for tower in towers))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True)
    args = parser.parse_args()
    assert args.N > 0
    solve_hanoi(args.N)

if __name__ == "__main__":
    main()
