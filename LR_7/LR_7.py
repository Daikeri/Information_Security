from typing import Literal
from functools import reduce


def task_one():
    class Matrix:
        @classmethod
        def create(cls, size_n, size_m, arr_value):
            prom = [['-' for j in range(size_m + 1)] for i in range(size_n + 1)]

            prom[0][0] = '  '

            for el in range(1, size_n + 1):
                prom[el][0] = 'S' + str(el)

            for el in range(1, size_m + 1):
                prom[0][el] = 'O' + str(el)

            for i in range(size_n):
                for j in range(size_m):
                    if arr_value[i][j] != '-':
                        prom[i + 1][j + 1] = arr_value[i][j]
            return prom

    class HRU:
        def __init__(self, base_path):
            file_info = open(base_path, 'r+')
            prom_one = file_info.readline()
            n, m = list(map(lambda x: int(x), prom_one.split()))
            prom_two = file_info.readlines()
            arr_str = list(map(lambda string: string.split(), prom_two))

            self.__matrix = Matrix.create(n, m, arr_str)

        def create_subj(self):
            self.__matrix.append(['-' for i in range(len(self.__matrix[0]))])

            index = len(self.__matrix) - 1
            self.__matrix[index][0] = 'S' + str(index)

        def create_obj(self):
            for lst in self.__matrix:
                lst.append('-')

            index = len(self.__matrix[0]) - 1
            self.__matrix[0][index] = 'O' + str(index)

        def destroy_subj(self, index):
            self.__matrix.pop(index)

        def destroy_obj(self, index):
            for el in self.__matrix:
                el.pop(index)

        def enter_relation(self, i, j, relation):
            if self.__matrix[i][j] == '-':
                self.__matrix[i][j] = relation
            else:
                self.__matrix[i][j] += relation

        def destroy_relation(self, i, j, relation):
            delete = self.__matrix[i][j].find(relation)
            print(self.__matrix[i][j][delete])
            self.__matrix[i][j] = self.__matrix[i][j].replace(self.__matrix[i][j][delete], '')

        def get_info(self):
            for i in self.__matrix:
                for j in i:
                    print(j, end=' ')
                print()
            print()

        def interpreter(self, inp_path, out_path):
            def base_operation(inp):
                size = len(inp)

                if size == 1:
                    if inp[0] == 'O+':
                        self.create_obj()
                    else:
                        self.create_subj()
                if size == 2:
                    if inp[0] == 'O-':
                        self.destroy_obj(int(inp[1]))
                    else:
                        self.destroy_subj(int(inp[1]))
                if size == 3:
                    if inp[0] in ['r+', 'w+', 'o+', 'x+']:
                        self.enter_relation(int(inp[1]), int(inp[2]), inp[0][0])
                    else:
                        self.destroy_relation(int(inp[1]), int(inp[2]), inp[0][0])

            def condition_operation(inp):
                ind_i = int(inp[1])
                ind_j = int(inp[2])
                relation = inp[0]
                action = inp[4:]

                if self.__matrix[ind_i][ind_j] == relation:
                    base_operation(action)

            file_info = open(inp_path, 'r')
            prom = file_info.readlines()
            arr_str = list(map(lambda z: z.split(), prom))
            for el in arr_str:
                if len(el) > 3:
                    condition_operation(el)
                else:
                    base_operation(el)

            file_info.close()
            file_info = open(out_path, 'w')

            for el in range(len(self.__matrix[0])):
                file_info.write(self.__matrix[0][el] + ' ')
            file_info.write('\n')

            for arr in self.__matrix[1:]:
                for el in arr:
                    file_info.write(el + '  ')
                file_info.write('\n')

            file_info.close()

    test_one = HRU('C:\Python_Project\Info_Secure\Text_File\Base_Matrix')
    test_one.interpreter(inp_path='C:\Python_Project\Info_Secure\Text_File\Input',
                         out_path='C:\Python_Project\Info_Secure\Text_File\Result')


def task_two():
    class Matrix:
        @classmethod
        def create(cls, size_n, size_m, arr_value):
            prom = [['-' for j in range(size_m + 1)] for i in range(size_n + 1)]

            prom[0][0] = ' '

            for el in range(1, size_n + 1):
                prom[el][0] = 'S' + str(el)

            for el in range(1, size_m + 1):
                prom[0][el] = 'O' + str(el)

            for i in range(size_n):
                for j in range(size_m):
                    if arr_value[i][j] != '-':
                        prom[i + 1][j + 1] = arr_value[i][j]
            return prom

    class HRU:
        def __init__(self, base_path):
            file_info = open(base_path, 'r+')
            prom_one = file_info.readline()
            n, m = list(map(lambda x: int(x), prom_one.split()))
            prom_two = file_info.readlines()
            arr_str = list(map(lambda string: string.split(), prom_two))

            self.matrix = Matrix.create(n, m, arr_str)

        def point_a(self):
            result = []

            for el in range(1, len(self.matrix[0])):
                flag = True
                for lst in range(1, len(self.matrix)):
                    if self.matrix[lst][el] in ['r', 'w', 'rw', 'wr']:
                        flag = False
                if flag:
                    result.append(self.matrix[0][el])
            print(result)

        def point_b(self):
            result = []
            for lst in range(1, len(self.matrix)):
                flag = True
                for el in range(1, len(self.matrix[0])):
                    if self.matrix[lst][el] in ['r', 'w', 'rw', 'wr']:
                        flag = False
                if flag:
                    result.append(self.matrix[lst][0])
            print(result)

        def point_c(self):
            result = []
            for lst in range(1, len(self.matrix)):
                flag = True
                for el in range(1, len(self.matrix[0])):
                    if self.matrix[lst][el] not in ['rw', 'wr']:
                        flag = False
                if flag:
                    result.append(self.matrix[lst][0])
            print(result)

        def point_d(self):
            result = []
            for el in range(1, len(self.matrix[0])):
                acc = []
                for lst in range(1, len(self.matrix)):
                    if self.matrix[lst][el] in ['r', 'wr', 'rw']:
                        acc.append(self.matrix[lst][0])
                if len(acc) == (len(self.matrix) - 1):
                    result.append(acc)
                    result.append(self.matrix[0][el])
            print(f'res:{result}')

        def point_e(self):
            result = []
            for lst in range(1, len(self.matrix)):
                acc_full = 0
                acc_read = 0
                for el in range(1, len(self.matrix[0])):
                    if self.matrix[lst][el] in ['rw', 'wr']:
                        acc_full += 1
                    elif self.matrix[lst][el] == 'r':
                        acc_read += 1

                if acc_full <= 1 and acc_read == 0:
                    result.append(self.matrix[lst][0])
            print(result)

        def get_info(self):
            for el in range(len(self.matrix[0])):
                print(self.matrix[0][el] + ' ', end='')
            print()

            for arr in self.matrix[1:]:
                for el in arr:
                    print(el + '  ', end='')
                print()


    test_one = HRU('C:\Python_Project\Info_Secure\Text_File\\access_matr')
    test_one.point_a()
    test_one.point_b()
    test_one.point_c()
    test_one.point_d()
    test_one.point_e()

task_two()