from functools import reduce


class Discharged_Matrix:
    def __init__(self, size_n, size_m, source_arr):
        self.n = size_n + 1
        self.m = size_m + 1

        self.lst_non_stand = ['plug']
        self.lst_column = ['plug']
        self.lst_value = ['plug']

        for lst in range(len(source_arr)):
            acc_non_stand = 0
            for el in range(len(source_arr[0])):
                if source_arr[lst][el] != '-':
                    acc_non_stand += 1
                    self.lst_column.append(el + 1)
                    self.lst_value.append(source_arr[lst][el])
            self.lst_non_stand.append(acc_non_stand)

    def enter_relation(self, i, j, relation):
        el_in_row = reduce(lambda acc, x: acc + x, self.lst_non_stand[1:i], 0)
        start_index = el_in_row + 1
        set_index = self.lst_column[start_index: start_index + self.lst_non_stand[i]]

        if j not in set_index:
            prom_index = list(map(lambda x: int(x), self.lst_column[start_index: start_index + self.lst_non_stand[i]]))
            prom_index.append(j)

            prom_val = self.lst_value[start_index: start_index + self.lst_non_stand[i]]
            prom_val.append(relation)

            save_all = [(prom_index[index], prom_val[index]) for index in range(len(prom_index))]

            prom_index.sort()

            void_arr = ['-' for i in prom_index]

            for ind in range(len(void_arr)):
                h = prom_index.index(save_all[ind][0])
                void_arr[h] = save_all[ind][1]

            self.lst_column = self.lst_column[0: start_index] + prom_index + self.lst_column[start_index + self.lst_non_stand[i]:]
            self.lst_value = self.lst_value[0: start_index] + void_arr + self.lst_value[start_index + self.lst_non_stand[i]:]

            self.lst_non_stand[i] += 1
        else:
            set_value = self.lst_value[start_index: start_index + self.lst_non_stand[i]]
            index = set_index.index(j)
            value = set_value[index]

            if value == 'r' or 'w':
                self.lst_value[start_index] += relation

    def remove_relation(self, i, j, relation):
        el_in_row = reduce(lambda acc, x: acc + x, self.lst_non_stand[1:i], 0)
        start_index = el_in_row + 1
        set_index = self.lst_column[start_index: start_index + self.lst_non_stand[i]]

        if j in set_index:
            set_value = self.lst_value[start_index: start_index + self.lst_non_stand[i]]
            index = set_index.index(j)
            value = set_value[index]
            if len(value) == 2:
                delete = value.find(relation)
                ind = value[delete]
                set_value[index] = set_value[index].replace(ind, '')
                self.lst_value = self.lst_value[0: start_index] + set_value

            else:
                set_index.remove(j)
                set_value.remove(value)
                self.lst_column = self.lst_column[0: start_index] + set_index
                self.lst_value = self.lst_value[0: start_index] + set_value

            self.lst_non_stand[i] -= 1

    def append_subject(self):
        self.lst_non_stand += [0]
        self.n += 1

    def destroy_subject(self, index):
        el_in_row = reduce(lambda acc, x: acc + x, self.lst_non_stand[1:index], 0)
        start_index = el_in_row + 1

        self.lst_column = self.lst_column[0:start_index] + self.lst_column[start_index + self.lst_non_stand[index]:]
        self.lst_value = self.lst_value[0:start_index] + self.lst_value[start_index + self.lst_non_stand[index]:]

        self.lst_non_stand.pop(index)
        self.n -= 1

    def percent_occupancy(self):
        full_matrix = (self.n - 1) * (self.m - 1)
        non_stand = reduce(lambda acc, x: acc + x, self.lst_non_stand[1:], 0)
        percent = non_stand / full_matrix * 100

        print(full_matrix, non_stand, percent)
        print()

    def object_access(self, index):
        acc_lst = ['Object ' + str(index) + ':']

        for row in range(1, len(self.lst_non_stand)):
            el_in_row = reduce(lambda acc, x: acc + x, self.lst_non_stand[1:row], 0)
            start_index = el_in_row + 1
            set_index = self.lst_column[start_index: start_index + self.lst_non_stand[row]]
            if index in set_index:
                acc_lst.append(row)
        print(acc_lst)

    def get_info(self):
        print(f'non stand: {self.lst_non_stand}\ncolumn: {self.lst_column}\nvalue:  {self.lst_value}\n')

    def decompose(self):
        for lst in range(1, self.n):
            el_in_row = reduce(lambda acc, x: acc + x, self.lst_non_stand[1:lst], 0)
            set_index = self.lst_column[el_in_row + 1: el_in_row + self.lst_non_stand[lst] + 1]
            set_value = self.lst_value[el_in_row + 1: el_in_row + self.lst_non_stand[lst] + 1]
            for el in range(1, self.m):
                if el not in set_index:
                    print('-', end=' ')
                else:
                    index = set_index.index(el)
                    value = set_value[index]
                    print(value, end=' ')
            print()
        print()


def test():
    def get_matrix():
        file_info = open('C:\Python_Project\Info_Secure\Text_File\\discharged_matr')
        prom_one = file_info.readline()
        n, m = list(map(lambda x: int(x), prom_one.split()))
        prom_two = file_info.readlines()
        arr_str = [prom_two[lst].split() for lst in range(n)]
        return n, m, arr_str

    n, m, matr = get_matrix()
    test_matr = Discharged_Matrix(n, m, matr)

    for i in range(1, 4):
        test_matr.enter_relation(1, i, 'r')

    for i in range(4, 8):
        test_matr.enter_relation(1, i, 'w')

    for i in range(2, 5):
        test_matr.enter_relation(i, 1, 'r')

    test_matr.remove_relation(3, 6, 'q')
    test_matr.enter_relation(4, 7, 'q')
    test_matr.enter_relation(4, 1, 'se')
    test_matr.remove_relation(4, 1, 'e')
    test_matr.append_subject()

    for i in range(1, 8):
        test_matr.enter_relation(5, i, 'rw')
    test_matr.object_access(1)
    test_matr.object_access(3)
    test_matr.object_access(4)
    test_matr.decompose()
    test_matr.percent_occupancy()
    test_matr.destroy_subject(4)
    test_matr.destroy_subject(1)
    test_matr.destroy_subject(3)
    test_matr.decompose()
    test_matr.percent_occupancy()
    test_matr.object_access(3)


test()


def task_two():
    pass
