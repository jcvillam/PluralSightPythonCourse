# This is a test
name = "Juan"
print(f"Hello World, I am {name}")

student_names = ["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]

# for name in student_names:
#     print(f"Student name is {name}")

# """ x = 0
# for index in range(5, 10, 2):
#     x += 10
#     print(f"For index {index}, The value of x is {x}") """

for name in student_names:
    if name == "Bort":
        continue
    print(f"Currently testing {name}")


