score = 0

op_order = ["A", "B", "C"]
me_order = ["X", "Y", "Z"]
with open("day02_input.txt") as f:
    for line in f:
        op, me = line.strip().split()
        ind_op = op_order.index(op)
        ind_me = me_order.index(me)
        if ind_me == ind_op:
            score += ind_me + 1 + 3
        elif any(
            [
                ind_me == 1 and ind_op == 0,
                ind_me == 2 and ind_op == 1,
                ind_me == 0 and ind_op == 2,
            ]
        ):
            score += ind_me + 1 + 6
        else:
            score += ind_me + 1 + 0

print(score)
