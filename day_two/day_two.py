
__INSTRUCTION_ADD__ = 1
__INSTRUCTION_MULT__ = 2
__INSTRUCTION_EXIT__ = 99

def aggregate_memory(memory, instruction_pointer, agg_func):
    num1_address = memory[instruction_pointer + 1]
    num2_address = memory[instruction_pointer + 2]
    result_address = memory[instruction_pointer + 3]
    
    num1 = memory[num1_address]
    num2 = memory[num2_address]

    memory[result_address] = agg_func(num1, num2)

    return intcode_program(memory, instruction_pointer + 4)

def intcode_program(memory, instruction_pointer = 0):
  instruction = memory[instruction_pointer]

  if instruction == __INSTRUCTION_ADD__:
    return aggregate_memory(memory, instruction_pointer, lambda x,y : x + y)

  elif instruction == __INSTRUCTION_MULT__:
    return aggregate_memory(memory, instruction_pointer, lambda x,y : x * y)

  elif instruction == __INSTRUCTION_EXIT__:
    return memory

  else:
    raise Exception("Unknown instruction")
    
assert intcode_program([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50]
assert intcode_program([1,0,0,0,99]) == [2,0,0,0,99]
assert intcode_program([2,3,0,3,99]) == [2,3,0,6,99]
assert intcode_program([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
assert intcode_program([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

if __name__ == "__main__":
    memory = []
    with open("day_two_input.txt") as file_input:
      string_input = file_input.readline()
      memory = list(map(lambda x : int(x), string_input.split(",")))

    for noun in range(0, 100):
      for verb in range(0, 100):
        temp_memory = list(memory)
        temp_memory[1] = noun
        temp_memory[2] = verb 
        temp_memory = intcode_program(temp_memory)
        if temp_memory[0] == 19690720:
          print("The noun %d and verb %d have generated the output 19690720" % (noun, verb))
          print("The answer is 100 * %d + %d = %d" % (noun, verb, 100 * noun + verb))
          raise SystemExit()

    print("No solution found")
