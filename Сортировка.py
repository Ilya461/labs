import random
#сортировка слиянием
def selection_sort(lst):
    col_sr = col_perest = 0
    for i in range(len(lst) - 1):
        mn_ind, col_sr = (find_min_ind(lst, i))[0], col_sr + (find_min_ind(lst, i))[1]
        lst[i], lst[mn_ind] = lst[mn_ind], lst[i]
        col_perest += 1
    return ["выбором", col_sr, col_perest, lst]
def find_min_ind(lst, start):
    work_lst = (lst[start:]).copy()
    col_sr = 0
    min_ind = 0
    for i in range(1, len(work_lst)):
        col_sr += 1
        if work_lst[min_ind] > work_lst[i]:
            min_ind = i
    return [min_ind + start, col_sr]
def bubble_sort(lst):
    col_sr = col_perest = 0
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            col_sr += 1
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                col_perest += 1
    return ["пузырьком", col_sr, col_perest, lst]
def vivod(lst):
    lst_s, lst_b = lst.copy(), lst.copy()
    srt_s, srt_b = selection_sort(lst_s), bubble_sort(lst_b)
    print("Сортировка выбором:", *(srt_s[3]))
    print("Сортировка пузырьком:", *(srt_b[3]))
    lst_form = ["Сортировка", "Количество сравнений", "Количество перестановок"]
    otv = [lst_form, srt_s, srt_b]
    print()
    for i in range(3):
        for j in range(3):
            print(str(otv[i][j]).ljust(27), end = "")
        print()    
def main():
    print("Выберите режим работы:")
    print("1 - демонстративный")
    print("2 - интерактивный")
    flag = False
    while not flag:
        mode = input()
        if (mode != "1") and (mode != "2"):
            print("Введите цифру: 1 или 2, обозначающую режим работы:")
        else:
            flag = True
    if mode == "1":
        lst = [random.randint(0, 99) for _ in range(10)]
        print("Массив для сортировки:")
        print(*lst)
        vivod(lst)
    elif mode == "2":
        deistv = 0
        while deistv != "6":
            print("Выберите действие:")
            print("1 - ввести массив")
            print("2 - изменить массив")
            print("3 - сортировка выбором")
            print("4 - сортировка пузырьком")
            print("5 - вывод таблицы сравнения сортировок")
            print("6 - выход")
            deistv = input()
            while (deistv != "1") and (deistv != "2") and (deistv != "3") and (deistv != "4") and (deistv != "5") and (deistv != "6"):
                print("Введите цифру: 1, 2, 3, 4, 5 или 6, обозначающую действие:")
                deistv = input()
                print(deistv)
                print(deistv == "6")
            if deistv == "1":
                print("Введите числа для массива на одной строке, через пробел:")
                lst = input().split()
                #while not pr(lst):
                    
if __name__ == "__main__":
    main()
