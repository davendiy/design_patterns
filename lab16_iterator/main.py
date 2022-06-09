#!/usr/bin/env python3
# -*-encoding: utf-8-*-

# created: 08.06.22
# Excusa. Quod scripsi, scripsi.

# by d.zashkonyi

from src import StaffList, Employee

def main():
    staff = StaffList([Employee(f"Employee {i}") for i in range(10)])
    for member in staff:
        print(member.get_name())


if __name__ == "__main__":
    main()
