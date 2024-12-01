def cooking_end_time(start_time, duration):
    end_time = (start_time + duration) % 24
    return end_time


print(cooking_end_time(15, 10))
print(f"Take the turkey out of the oven at {cooking_end_time(13, 8)} o'clock")
