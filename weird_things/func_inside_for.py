for i in range(10):
    def show():  # Defining a fuction inside a for loop
        print(i*2)

    show()  # It can be called inside the for loop, will print i*2 for each iteration

show()  # It can be called outside the for loop, will print i*2 for the last iteration only
