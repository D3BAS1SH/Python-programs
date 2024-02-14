""" mynumS=str.split(input('Two numbers separated by space : '),' ')
mynumS=[int(x) for x in mynumS]
print(mynumS) """

mynumS=[int(x) for x in str.split(input('Two numbers separated by space : '),' ')]
print(mynumS)