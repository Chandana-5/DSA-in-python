def permutationEquation(p):
    # Write your code 
    result=[]
    for i in range(1,len(p)+1):
        y=p.index(i)+1
        z=p.index(y)+1 
        result.append(z)
    return result
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
