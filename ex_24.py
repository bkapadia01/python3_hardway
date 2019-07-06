print("let's practice everythign")
print('you\'d need to know \'bout excapes with \\ that do:')
print('\n newliines and \t tabs')

poem = """
\t the lovely world
this is line 
\n\t where there is none
"""

print("--------")
print(poem)
print("-------")

five = 10 - 2 + 3 - 6

print(f"this should be five: {five}")

def secret_formula(started):
    jelly_bean = started * 500
    jars = jelly_bean / 1000
    crates = jars / 100
    return jelly_bean, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("with a starting point of: {}".format(start_point))

print(f"we'd have {beans} beans, {jars} jars and {crates} crates.")

start_point = start_point/100
print("we can also do it this way")
formula = secret_formula(start_point)
print("we'd have {} beans, {}, jars and {} crates)".format(*formula))