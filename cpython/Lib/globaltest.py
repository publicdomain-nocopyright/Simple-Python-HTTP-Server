#_____________________________________
global_array = []

#_____________________________________
def add_argument_to_global_array(func):
    def wrapper(arg):
        global global_array
        global_array.append(arg)
        return func(arg)
    return wrapper

#_____________________________________
@add_argument_to_global_array
def example_function(arg):
    print(f"Function is running with argument: {arg}")

#_____________________________________
example_function("Argument to add when function runs")
example_function("Seeecond")

#_____________________________________
print(global_array)
