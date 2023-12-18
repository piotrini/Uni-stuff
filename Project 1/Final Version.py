
def find_submatrices_summing_above_threshhold(matrix, threshhold, submatrix_width = 2, submatrix_height = 2):
    results = []
    for y in range((len(matrix)-submatrix_height+1)):
        for x in range((len(matrix[0])-submatrix_width+1)):
            submatrix = [row[x:x+submatrix_width] for row in array[y:y+submatrix_height]]
            sum = 0
            for row in submatrix:
                for element in row:
                    sum += element
            if(sum >= threshhold):
                results.append(submatrix)
    return results

k = 25
array = [[9,2,3,4,5],[9,7,1,8,6],[1,9,9,0,11]]  

print(find_submatrices_summing_above_threshhold(array, k))