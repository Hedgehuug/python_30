"""
Generate a sequence using the function range that
returns the following.
[-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0,
10, 20, 30, 40, 50, 60, 70, 80, 90]
"""

sequence_one = list(range(-100,91,10))
print(sequence_one)

"""
Generate the previous sequence but in this case in
the opposite way.
"""
sequence_reverse = list(range(90,-101,-10))
print(sequence_reverse)


"""
This challenge can be a bit difficult, try to create a
function that returns a sequence of decimal numbers between
2 numbers, incremental only.
Here's a hint, use the while statement
"""
#Hoof this was really hard cause of the rounding, but it's something I've had problems with in the past
#But the solution should adjust the rounding to the number of decimal points in Step
def float_sequence(start,stop,step):
    progress = start
    output = [start]
    round_num = len(str(step).split('.')[1])
    while progress < stop:
        output.append(progress)
        progress = round(progress + step,round_num)
    print(output)


float_sequence(2,15,0.08)


    