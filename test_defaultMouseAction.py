from math import gcd

# 모든 계수 정수
def line_equation1(x1, y1, x2, y2):
    #insert code here
    # 1) 수직 수평선과 무수히많은 직선 처리
    if x1==x2 and y1==y2:
        print('모든 ('+str(x1)+', '+str(y1)+')을 지나는 직선')
        return
    if x1==x2:
        print('x = '+str(x1))
        return
    if y1==y2:
        print('y = '+str(y1))
        return
    
    ay = x1-x2
    ax = y1-y2
    ac = (x1-x2)*y1 - (y1-y2)*x1

    # 2) 최대공약수로 나누기
    temp = gcd(ay, ax)
    temp = gcd(temp, ac)
    ax //= temp
    ay //= temp
    ac //= temp
    msg = ''

    # 3) 좌변 양수로 만들기
    if ay<0:
        ay *= -1
        ax *= -1
        ac *= -1
    
    # 4) 1, -1과 띄어쓰기 처리
    if ay == 1:
        msg += 'y = '
    else :
        msg += str(ay)+'y = '

    if ax == 1:
        msg += 'x '
    elif ax == -1:
        msg += '-x '
    else :
        msg += str(ax)+'x '

    if ac>0:
        msg += '+ '+str(ac)
    elif ac<0:
        msg += '- '+str(-ac)
    print(msg)

# 좌변 계수 1 (y = ...)
def line_equation2(x1, y1, x2, y2):
    #insert code here
    # 1) 수직 수평선과 무수히많은 직선 처리
    if x1==x2 and y1==y2:
        print('모든 ('+str(x1)+', '+str(y1)+')을 지나는 직선')
        return
    if x1==x2:
        print('x = '+str(x1))
        return
    if y1==y2:
        print('y = '+str(y1))
        return
    
    # 2) 분수형태 계수 y = (axn/axd)x + (acn/acd), 분모 양수
    axn = y1-y2
    axd = x1-x2
    acn = x1*y2 - x2*y1
    acd = x1-x2
    msg = ''
    
    if axd < 0 :        
        axn *= -1
        axd *= -1
    if acd < 0 :
        acn *= -1
        acd *= -1

    # 3) 최대공약수로 나누기
    gx = gcd(axn, axd)
    gc = gcd(acn, acd)
    
    axn //= gx
    axd //= gx
    acn //= gc
    acd //= gc

    msg += 'y = '
    
    
    # 4) x항 
    # 4-1)정수, 유리수 경우나누기
    msgx = ''
    if axd == 1:
        # 4-2) 1인 경우 미표시
        if axn == 1:
            msgx += 'x '
        elif axn == -1:
            msgx += '-x '
        else:
            msgx += str(axn)+'x '
    else :
        msgx += '('+str(axn)+'/'+str(axd)+')x '

   # 5) 상수항
   # 5-1) 양수 음수 나누기
    msgc = ''
    if acn != 0:
        if acn > 0:
            msgc += '+ '
        elif acn < 0:
            msgc += '- '
        # 5-2)정수, 유리수 나누기
        if acd == 1:
            msgc += str(acn)
        else:
            msgc += str(acn)+'/'+str(acd)
    msg += msgx + msgc
    print(msg)

ex = [[0, 0, 0, 0], [2, 3, 5, 3], [2, 4, 2, 6], [0, 0, 1, 1], [2, 4, -7, 10], [0, 5, 24, 75], [2, -1, -12, 9], [2, -1, 16, -11], [0, 1, 6, 3]]
for i in range (9):
    print(ex[i])
    line_equation1(ex[i][0], ex[i][1], ex[i][2], ex[i][3])
    line_equation2(ex[i][0], ex[i][1], ex[i][2], ex[i][3])
    print(" ")
