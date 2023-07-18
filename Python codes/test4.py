import timeit

# def sum(n):
#     final = 0 
#     for i in range(n+1):
#         final = final+i

#     print(final)





def sum(n):
    final = n*(n+1)/2
    print(final)

sum(10)


execution_time = timeit.timeit(lambda: sum(2), number=1)
print(execution_time)