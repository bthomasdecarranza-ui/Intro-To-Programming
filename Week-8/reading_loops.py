# Question 1
# GUESS: It will print "Hello" 4 times
# ACTUAL RESULT:
# Hello
# Hello
# Hello
# Hello
# EXPLANATION:
# range(4) goes from 0 to 3 (4 total iterations), so the loop runs 4 times.

for i in range(4):
    print("Hello")


# Question 2
# GUESS: It will print 3
# ACTUAL RESULT:
# 3
# EXPLANATION:
# count starts at 0. The loop runs while count < 3.
# Each loop adds 1, so count becomes 1 → 2 → 3, then stops.

count = 0
while count < 3:
    count = count + 1

print(count)


# Question 3
# GUESS: It will print "Pass"
# ACTUAL RESULT:
# Pass
# EXPLANATION:
# Even though 85 > 80, Python checks conditions in order.
# Since 85 > 70 is True, it prints "Pass" and skips the rest.

score = 85
if score > 70:
    print("Pass")
elif score > 80:
    print("Great")
else:
    print("Fail")


# Question 4
# GUESS: Infinite loop (prints numbers forever)
# ACTUAL RESULT:
# 5
# 6
# 7
# ... (continues forever)
# EXPLANATION:
# x starts at 5 and increases (x += 1), so it will always be > 0.
# The condition never becomes False → infinite loop.

x = 5
while x > 0:
    print(x)
    x += 1


# Question 5
# GUESS:
# 0 0
# 0 1
# 1 0
# 1 1
# ACTUAL RESULT:
# 0 0
# 0 1
# 1 0
# 1 1
# EXPLANATION:
# Nested loops: for each value of i (0,1), j runs (0,1).
# So it prints all combinations of i and j.

for i in range(2):
    for j in range(2):
        print(i, j)

        