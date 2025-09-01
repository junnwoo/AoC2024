class Computer:
    reg_a: int
    reg_b: int
    reg_c: int
    output: list[int]

    def __init__(self, init_a: int = 0, init_b: int = 0, init_c: int = 0):
        self.reg_a = init_a
        self.reg_b = init_b
        self.reg_c = init_c
        self.output = []

    def get_literal(self, literal: int) -> int:
        match literal:
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 3
            case 4:
                return self.reg_a
            case 5:
                return self.reg_b
            case 6:
                return self.reg_c
            case 7:
                return 7
            case _:
                raise ValueError()

    def bxl(self, arg: int):
        n1 = self.reg_b
        n2 = self.get_literal(arg)
        self.reg_b = n1 ^ n2

    def bst(self, arg: int):
        lit = self.get_literal(arg)
        self.reg_b = lit % 8

    def bxc(self):
        b = self.reg_b
        c = self.reg_c
        self.reg_b = b ^ c

    def dv(self, arg: int, out_reg: str):
        num = self.reg_a
        den = 2 ** self.get_literal(arg)
        out = int(num / den)
        match out_reg:
            case "a":
                self.reg_a = out
            case "b":
                self.reg_b = out
            case "c":
                self.reg_c = out
            case _:
                raise ValueError

    def run_program(self, sequence: list[int]):
        finished = False
        curr_inst = 0
        while not finished:
            op = sequence[curr_inst]
            arg = sequence[curr_inst + 1]
            print(f"{op}, {arg}")
            jumped = False

            match op:
                case 0:
                    self.dv(arg, out_reg="a")
                case 1:
                    self.bxl(arg)
                case 2:
                    self.bst(arg)
                case 3:
                    if not self.reg_a == 0:
                        jumped = True
                        curr_inst = self.get_literal(arg)
                case 4:
                    self.bxc()
                case 5:
                    n = self.get_literal(arg)
                    self.output.append(n % 8)
                    print(self.output)
                case 6:
                    self.dv(arg, out_reg="b")
                case 7:
                    self.dv(arg, out_reg="c")
                case _:
                    raise ValueError()

            if not jumped:
                curr_inst += 2
            if curr_inst >= len(sequence) - 1:
                finished = True

    def print_output(self):
        out_string = ""
        for i in self.output:
            out_string += str(i) + ","
        print(out_string[0:-1])


comp = Computer(41644071, 0, 0)
seq = [2, 4, 1, 2, 7, 5, 1, 7, 4, 4, 0, 3, 5, 5, 3, 0]
comp.run_program(seq)
comp.print_output()
