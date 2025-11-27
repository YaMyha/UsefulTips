from asyncio import Future

my_future = Future() # create future

print(f'Is my_future done? {my_future.done()}') # get false

my_future.set_result(42) # set value to future

print(f'Is my_future done? {my_future.done()}') # yes
print(f'What is the result of my_future? {my_future.result()}')

# Is my_future done? False
# Is my_future done? True
# What is the result of my_future? 42