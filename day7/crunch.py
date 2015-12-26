from collections import defaultdict
from ctypes import c_uint16

operators = {
    'AND': lambda x, y: x & y,
    'OR': lambda x, y: x | y,
    'LSHIFT': lambda x, y: x << y,
    'RSHIFT': lambda x, y: x >> y,
    'NOT': lambda x: ~x
}


class LogicGate(object):
    def __init__(self,
                 operands=None,
                 operation=None,
                 receiver=None):
        self.operands = operands
        self.operation = operation
        self.receiver = receiver

    def __str__(self):
        return '(%s) %s %s' % (
            self.operation,
            self.operands,
            self.receiver)


def do_simulation(circuits,
                  values_for_wires):
    while None in values_for_wires.values():
        for circuit in circuits:
            has_all_input = True
            for operand in circuit.operands:
                if operand in values_for_wires and \
                                values_for_wires[operand] is None:
                    has_all_input = False
                    break
            if has_all_input:
                if not circuit.operation:
                    # literal -> wire
                    if circuit.operands[0] in values_for_wires:
                        values_for_wires[circuit.receiver] = values_for_wires[
                            circuit.operands[0]]
                    else:
                        values_for_wires[circuit.receiver] = long(
                                circuit.operands[0]
                        )
                else:
                    func = operators[circuit.operation]
                    if len(circuit.operands) == 1:
                        values_for_wires[circuit.receiver] = func(
                                long(values_for_wires[circuit.operands[0]])
                        )
                    else:
                        op1 = values_for_wires.get(circuit.operands[0])
                        if not op1 and circuit.operands[0] \
                                not in values_for_wires:
                            # check for literals
                            op1 = long(circuit.operands[0])

                        op2 = values_for_wires.get(circuit.operands[1])
                        if not op2 and circuit.operands[1] \
                                not in values_for_wires:
                            # check for literals
                            op2 = long(circuit.operands[1])

                        values_for_wires[circuit.receiver] = func(
                                op1,
                                op2
                        )


def load_circuits(filename,
                  values_for_wires):
    circuits = []
    with open(filename) as f:
        for line in f:
            lvalue, dest = line.strip().split(' -> ')
            lvalue = lvalue.split(' ')
            if len(lvalue) == 1:
                # format: 123 -> dest
                instruction = LogicGate(
                        operands=[lvalue[0]],
                        receiver=dest
                )
            elif len(lvalue) == 2:
                # format: OP op1 -> dest
                instruction = LogicGate(
                        operation=lvalue[0],
                        operands=[lvalue[1]],
                        receiver=dest
                )
            elif len(lvalue) == 3:
                # format: op1 OP op2 -> dest
                instruction = LogicGate(
                        operands=[lvalue[0], lvalue[2]],
                        operation=lvalue[1],
                        receiver=dest
                )
            else:
                assert False, "what?"
            values_for_wires[dest] = None
            circuits.append(instruction)
    return circuits


def main():
    values_for_wires = defaultdict(str)
    circuits = load_circuits('input.txt', values_for_wires)
    do_simulation(circuits, values_for_wires)

    print 'Done:'
    for wire in sorted(values_for_wires.keys()):
        print '%s : %s' % (wire, c_uint16(values_for_wires[wire]))


if __name__ == '__main__':
    main()
