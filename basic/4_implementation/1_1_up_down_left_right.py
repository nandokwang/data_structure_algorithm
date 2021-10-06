# N 입력받기
n = int(input()) # 5
x, y = 1, 1 # 시작좌표는 항상 (1, 1)
plans = input().split() # R R R U D D

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:            # R R R U D D
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):    # ['L', 'R', 'U', 'D']
        if plan == move_types[i]:
            nx = x + dx[i] # temp x 좌표 저장
            ny = y + dy[i] # temp y 좌표 저장
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n: # 갱신된 temp x,y 좌표가 1보다작거나(맵좌상단벗어남) n보다크면(맵우하단벗어남) 
        continue
    # 이동 수행
    x, y = nx, ny # 안벗어나는경우 x,y 좌표업데이트

print(x, y) # 3 4