def my_list(n, n_list):
    new_list = []
    for i in n_list:
        if n_list.count(i) != n:
            n_list.remove(i)
            new_list = n_list
            print(new_list)
        return "failed"


if __name__ == '__main__':
    my_list(2, [1, 2, 3, 2, 1, 1, 2, 3])
