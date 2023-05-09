def matMultiplication(mat1, mat2):
    res = list(list())

    if len(mat1[0]) == len(mat2):
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat1[0])):
                    res[i][j] += mat1[i][k] * mat2[k][j]
    else:
        print("Incompatable dimmensions...")
    
    return res

def transpose(m):
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return rez

res = matMultiplication([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(res)