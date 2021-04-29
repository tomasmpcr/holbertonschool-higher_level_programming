#!/usr/bin/python3
if __name__ == "__main__":
    x = dir("hidden_4.pyc")
    x.sort()
    for i in range(0, len(x)):
        if x[i][:2] != "__":
            print("{}".format(x[i]))
