user_input = int(input("크리스마스 트리의 높이를 설정하세요: "))

for i in range(1, user_input + 1):
    print(' ' * (user_input - i) + '*' * (2 * i - 1))
