def greet():
    def welcome():
        print("Greeting")

    return welcome


func = greet()
func()
