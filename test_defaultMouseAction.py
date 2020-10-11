def line_equation(x1, y1, x2, y2):
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
    msg = ''
    # 2) 좌변 양수로 만들기
    if ay<0:
        ay *= -1
        ax *= -1
        ac *= -1

    # 3) 1, -1과 띄어쓰기 처리
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

line_equation(0, 0, 1, 1)
