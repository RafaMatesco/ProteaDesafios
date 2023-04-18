group1 = ('Coca-cola', "Pepsico")
group2 = ('Nestlé', 'Unilever')
group3 = ('Mars', 'P&G')

pollutionIndex = 0.0
m = 0

while True:
    increase = float(input('Type the amount of pollution index increase: '))
    pollutionIndex += increase
    print(pollutionIndex)
    if pollutionIndex >= 0.3 and pollutionIndex < 0.45:
        print('warning of increase in pollution index (group 1):')
        m += 1
        for v in group1:
            print(v)
    elif (pollutionIndex >= 0.45) and  pollutionIndex < 0.55:
        m += 1
        print('warning of increase in pollution index (group 1, group 2):')
        for v1 in group1:
            print(v1)
        for v1 in group2:
            print(v1)
    elif (pollutionIndex >= 0.55):
        print('warning of increase in pollution index (group 1, group 2, group 3):')
        for v1 in group1:
            print(v1)
        for v1 in group2:
            print(v1)
        for v1 in group3:
            print(v1)
        break