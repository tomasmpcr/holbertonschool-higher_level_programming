#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return
    list_total = []
    las_list = [1]
    for i in range(0, n):
        if i == 0:
            list_total.append(las_list)
        else:
            new_list = []

            for j in range(0, i + 1):
                num1 = 0
                if j > 0:
                    num1 = las_list[j - 1]
                
                num2 = 0
                if j < len(las_list):
                    num2 = las_list[j]

                new_list.append(num1 + num2)
            las_list = new_list
            list_total.append(new_list)
    return(list_total)
