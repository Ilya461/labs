import random
#сортировка слиянием
def selection_sort(lst):
    col_sr = col_perest = 0
    for i in range(len(lst) - 1):
        mn_ind, col_sr = (find_min_ind(lst, i))[0], col_sr + (find_min_ind(lst, i))[1]
        lst[i], lst[mn_ind] = lst[mn_ind], lst[i]
        col_perest += 1
    return [lst, col_sr, col_perest]
def find_min_ind(lst, start):
    work_lst = (lst[start:]).copy()
    col_sr = 0
    min_ind = 0
    for i in range(1, len(work_lst)):
        col_sr += 1
        if work_lst[min_ind] > work_lst[i]:
            min_ind = i
    return [min_ind + start, col_sr]
#def bubble sort(lst):
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
        print("Список для сортировки:")
        print(*lst)
        print(selection_sort(lst))
if __name__ == "__main__":
    main()