score = 0

op_order = ["A", "B", "C"]
me_order = ["X", "Y", "Z"]
with open("day02_input.txt") as f:
    for line in f:
        op, me = line.strip().split()
        ind_op = op_order.index(op)
        ind_me = me_order.index(me)
        if ind_me == 1:
            score += ind_op + 1 + 3
        elif ind_me == 2:
            shape_map = {
                0: 1 + 1,
                1: 2 + 1,
                2: 0 + 1,
            }
            score += shape_map[ind_op] + 6
        else:
            shape_map = {
                0: 2 + 1,
                1: 0 + 1,
                2: 1 + 1,
            }
            score += shape_map[ind_op] + 0

print(score)
