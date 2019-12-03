from math import floor

__LAST_FREE_FUEL__ = 9

def calculate_required_fuel(mass):
  required_fuel = floor(mass / 3) - 2 

  if required_fuel >= __LAST_FREE_FUEL__:
    return calculate_required_fuel(required_fuel) + required_fuel
  else:
    return required_fuel

assert calculate_required_fuel(12) == 2, "Required fuel to a module of mass 12 should be 2"
assert calculate_required_fuel(14) == 2, "Required fuel to a module of mass 14 should be 2"
assert calculate_required_fuel(1969) == 966, "Required fuel to a module of mass 1969 should be 966"
assert calculate_required_fuel(100756) == 50346, "Required fuel to a module of mass 100756 should be 50346"

if __name__ == "__main__":
    with open("day_one_input.txt") as file_input:

      sum_of_fuel_requirements = 0
      for mass in file_input.readlines():
        fuel = calculate_required_fuel(int(mass))
        sum_of_fuel_requirements = sum_of_fuel_requirements + fuel
      
      print("The sum of the fuel requirements is %d" % sum_of_fuel_requirements)
