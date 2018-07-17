def get_living_neighbors(i, j, generation):
    """
    returns living neighbors around the cell
    """
    living_neighbors = 0 # count for living neighbors
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1),
                    (i-1, j+1), (i-1, j-1), (i+1, j+1), (i+1, j-1)] 
    for k, l in neighbors:
        if 0 <= k < len(generation) and 0 <= l < len(generation[0]):
            if generation[k][l] == 1:
                living_neighbors += 1
    return living_neighbors

def get_next_generation(generation):
    """
    compute the next generation
    """
    updates = []
    for i in range(len(generation)):
        for j in range(len(generation[0])):
            living_neighbors = get_living_neighbors(i, j, generation)
            if generation[i][j] == 0:
                if living_neighbors == 3:
                    updates.append((i, j))
            else:
                if living_neighbors < 2 or living_neighbors > 3:
                    updates.append((i, j))

    for i, j in updates:
        generation[i][j] = 0 if generation[i][j] == 1 else 1
    return generation

def input_generation():
    board = []
    row = col = -1
    with open('input.txt') as fobj:
        for line in fobj:
            i, j = map(int, line.split(','))
            board.append((i, j))
            row = max(row, i)
            col = max(col, j)
    generation =[[0 for j in range(col+1)] for i in range(row+1)]
    for i, j in board:
        generation[i][j] = 1
    return generation

def output_generation(new_generation):
    board = []
    for i in range(len(new_generation)):
        for j in range(len(new_generation[0])):
            if new_generation[i][j] == 1:
                board.append((i, j))
    with open('output.txt','w') as fobj:
        for i, j in board:
            fobj.write(str(i) + ',' + str(j) + '\n')
    
def main():
    generation = input_generation()
    new_generation = get_next_generation(generation)
    output_generation(new_generation)

if __name__ == '__main__':
    main()