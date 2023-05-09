coefficients = input("Coeficientii: ").split(' ')
state = input("Starea: ").split(' ')

coefficients = [int(c) for c in coefficients]
state = [int(s) for s in state]
initial_state = state.copy()

def LFSR(coefficients, state):
    period = 2**len(state) - 1
    output = []
    for i in range(period):
        bit = 0
        for j in range(len(coefficients)):
            bit ^= coefficients[j] & state[j]
            
        output.append(state.pop())
        state.insert(0, bit)
        if state == initial_state:
            break

    return output, i+1

output, period = LFSR(coefficients, state)

print("Output: ", output)
print("Perioada: ", period)