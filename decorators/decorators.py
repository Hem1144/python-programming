def greet():
    def welcome():
        print("Greeting")

    return welcome


somefunc = greet()
somefunc()
