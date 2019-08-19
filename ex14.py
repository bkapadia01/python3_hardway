from sys import argv

script, user_name = argv
prompt = '> '

print(f"hi {user_name}, im the {script} script")
print("i'd like to ask questions")
print(f"do you like {user_name}")
likes = input(prompt)

print(f"wehr do you live {user_name}")
lives = input(prompt)

print("what kind of comp do you have")
computer = input(prompt)

print(f""" 
so you said {likes} about liking {user_name}
you live in {lives}. thats where you are from
and you have a {computer} computer
""")