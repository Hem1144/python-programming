# name = "Hemlal"


# def greeting(name):
#     color = "blue"
#     print(color)
#     print(name)


# greeting("Hemlal Dulal")
# print(color)  # * can not access due to local scope


# def another():
#     greeting("Dulal")


# another()


#! function insdie another function

name = "Hemlal"
count = 1


def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Dulal")


another()
