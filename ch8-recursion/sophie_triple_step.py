# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

def main():

    count_ways = 0

    def get_total_steps_from_user():
        return input("Enter number of steps: ")

    # Assumption: The total number of hops must = the total number of stairs
    def update_count(count):
        if count == 0:
            nonlocal count_ways
            count_ways += 1
        elif count < 0:
            return
        else:
            calc_possibilities(count)

    def hop_1(steps_left):
        steps_left -= 1
        update_count(steps_left)

    def hop_2(steps_left):
        steps_left -= 2
        update_count(steps_left)

    def hop_3(steps_left):
        steps_left -= 3
        update_count(steps_left)

    def calc_possibilities(total_steps):
        if total_steps > 0:
            hop_1(total_steps)
            hop_2(total_steps)
            hop_3(total_steps)

    try:
        user_input = get_total_steps_from_user()
        int_total_steps = int(user_input)
        if int_total_steps > 0:
            calc_possibilities(int_total_steps)
            print(count_ways)
        else:
            print("Enter positive integer.")
            main()

    except ValueError:
        print("Enter integer.")
        main()


if __name__ == "__main__":
    main()
