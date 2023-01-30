def grabFile():
    i = 0
    for line in file:
        if i > 14:
            bottom.append(line.split())
        elif i > 11:
            top.append(line.split())
        elif i > 8:
            back.append(line.split())
        elif i > 5:
            right.append(line.split())
        elif i > 2:
            left.append(line.split())
        else:
            front.append(line.split())
        i += 1


def u():
    temp = front[0]
    front[0] = right[0]
    right[0] = back[0]
    back[0] = left[0]
    left[0] = temp
    temp = top[0][0]
    top[0][0] = top[2][0]
    top[2][0] = top[2][2]
    top[2][2] = top[0][2]
    top[0][2] = temp
    temp = top[0][1]
    top[0][1] = top[1][0]
    top[1][0] = top[2][1]
    top[2][1] = top[1][2]
    top[1][2] = temp
    total.append('u')


def up():
    temp = front[0]
    front[0] = left[0]
    left[0] = back[0]
    back[0] = right[0]
    right[0] = temp
    temp = top[0][0]
    top[0][0] = top[0][2]
    top[0][2] = top[2][2]
    top[2][2] = top[2][0]
    top[2][0] = temp
    temp = top[0][1]
    top[0][1] = top[1][2]
    top[1][2] = top[2][1]
    top[2][1] = top[1][0]
    top[1][0] = temp
    total.append('u\'')


def r():
    temp = front[0][2]
    front[0][2] = bottom[0][2]
    bottom[0][2] = back[2][0]
    back[2][0] = top[0][2]
    top[0][2] = temp
    temp = front[1][2]
    front[1][2] = bottom[1][2]
    bottom[1][2] = back[1][0]
    back[1][0] = top[1][2]
    top[1][2] = temp
    temp = front[2][2]
    front[2][2] = bottom[2][2]
    bottom[2][2] = back[0][0]
    back[0][0] = top[2][2]
    top[2][2] = temp
    temp = right[0][0]
    right[0][0] = right[2][0]
    right[2][0] = right[2][2]
    right[2][2] = right[0][2]
    right[0][2] = temp
    temp = right[0][1]
    right[0][1] = right[1][0]
    right[1][0] = right[2][1]
    right[2][1] = right[1][2]
    right[1][2] = temp
    total.append('r')


def rp():
    temp = front[0][2]
    front[0][2] = top[0][2]
    top[0][2] = back[2][0]
    back[2][0] = bottom[0][2]
    bottom[0][2] = temp
    temp = front[1][2]
    front[1][2] = top[1][2]
    top[1][2] = back[1][0]
    back[1][0] = bottom[1][2]
    bottom[1][2] = temp
    temp = front[2][2]
    front[2][2] = top[2][2]
    top[2][2] = back[0][0]
    back[0][0] = bottom[2][2]
    bottom[2][2] = temp
    temp = right[0][0]
    right[0][0] = right[0][2]
    right[0][2] = right[2][2]
    right[2][2] = right[2][0]
    right[2][0] = temp
    temp = right[0][1]
    right[0][1] = right[1][2]
    right[1][2] = right[2][1]
    right[2][1] = right[1][0]
    right[1][0] = temp
    total.append('r\'')


def l():
    temp = front[0][0]
    front[0][0] = top[0][0]
    top[0][0] = back[2][2]
    back[2][2] = bottom[0][0]
    bottom[0][0] = temp
    temp = front[1][0]
    front[1][0] = top[1][0]
    top[1][0] = back[1][2]
    back[1][2] = bottom[1][0]
    bottom[1][0] = temp
    temp = front[2][0]
    front[2][0] = top[2][0]
    top[2][0] = back[0][2]
    back[0][2] = bottom[2][0]
    bottom[2][0] = temp
    temp = left[0][0]
    left[0][0] = left[2][0]
    left[2][0] = left[2][2]
    left[2][2] = left[0][2]
    left[0][2] = temp
    temp = left[0][1]
    left[0][1] = left[1][0]
    left[1][0] = left[2][1]
    left[2][1] = left[1][2]
    left[1][2] = temp
    total.append('l')


def lp():
    temp = front[0][0]
    front[0][0] = bottom[0][0]
    bottom[0][0] = back[2][2]
    back[2][2] = top[0][0]
    top[0][0] = temp
    temp = front[1][0]
    front[1][0] = bottom[1][0]
    bottom[1][0] = back[1][2]
    back[1][2] = top[1][0]
    top[1][0] = temp
    temp = front[2][0]
    front[2][0] = bottom[2][0]
    bottom[2][0] = back[0][2]
    back[0][2] = top[2][0]
    top[2][0] = temp
    temp = left[0][0]
    left[0][0] = left[0][2]
    left[0][2] = left[2][2]
    left[2][2] = left[2][0]
    left[2][0] = temp
    temp = left[0][1]
    left[0][1] = left[1][2]
    left[1][2] = left[2][1]
    left[2][1] = left[1][0]
    left[1][0] = temp
    total.append('l\'')


def f():
    temp = left[0][2]
    left[0][2] = bottom[0][0]
    bottom[0][0] = right[2][0]
    right[2][0] = top[2][2]
    top[2][2] = temp
    temp = left[1][2]
    left[1][2] = bottom[0][1]
    bottom[0][1] = right[1][0]
    right[1][0] = top[2][1]
    top[2][1] = temp
    temp = left[2][2]
    left[2][2] = bottom[0][2]
    bottom[0][2] = right[0][0]
    right[0][0] = top[2][0]
    top[2][0] = temp
    temp = front[0][0]
    front[0][0] = front[2][0]
    front[2][0] = front[2][2]
    front[2][2] = front[0][2]
    front[0][2] = temp
    temp = front[0][1]
    front[0][1] = front[1][0]
    front[1][0] = front[2][1]
    front[2][1] = front[1][2]
    front[1][2] = temp
    total.append('f')


def fp():
    temp = left[0][2]
    left[0][2] = top[2][2]
    top[2][2] = right[2][0]
    right[2][0] = bottom[0][0]
    bottom[0][0] = temp
    temp = left[1][2]
    left[1][2] = top[2][1]
    top[2][1] = right[1][0]
    right[1][0] = bottom[0][1]
    bottom[0][1] = temp
    temp = left[2][2]
    left[2][2] = top[2][0]
    top[2][0] = right[0][0]
    right[0][0] = bottom[0][2]
    bottom[0][2] = temp
    temp = front[0][0]
    front[0][0] = front[0][2]
    front[0][2] = front[2][2]
    front[2][2] = front[2][0]
    front[2][0] = temp
    temp = front[0][1]
    front[0][1] = front[1][2]
    front[1][2] = front[2][1]
    front[2][1] = front[1][0]
    front[1][0] = temp
    total.append('f\'')


def d():
    temp = front[2]
    front[2] = left[2]
    left[2] = back[2]
    back[2] = right[2]
    right[2] = temp
    temp = bottom[0][0]
    bottom[0][0] = bottom[2][0]
    bottom[2][0] = bottom[2][2]
    bottom[2][2] = bottom[0][2]
    bottom[0][2] = temp
    temp = bottom[0][1]
    bottom[0][1] = bottom[1][0]
    bottom[1][0] = bottom[2][1]
    bottom[2][1] = bottom[1][2]
    bottom[1][2] = temp
    total.append('d')


def dp():
    temp = front[2]
    front[2] = right[2]
    right[2] = back[2]
    back[2] = left[2]
    left[2] = temp
    temp = bottom[0][0]
    bottom[0][0] = bottom[0][2]
    bottom[0][2] = bottom[2][2]
    bottom[2][2] = bottom[2][0]
    bottom[2][0] = temp
    temp = bottom[0][1]
    bottom[0][1] = bottom[1][2]
    bottom[1][2] = bottom[2][1]
    bottom[2][1] = bottom[1][0]
    bottom[1][0] = temp
    total.append('d\'')


def b():
    temp = left[0][0]
    left[0][0] = top[0][2]
    top[0][2] = right[2][2]
    right[2][2] = bottom[2][0]
    bottom[2][0] = temp
    temp = left[1][0]
    left[1][0] = top[0][1]
    top[0][1] = right[1][2]
    right[1][2] = bottom[2][1]
    bottom[2][1] = temp
    temp = left[2][0]
    left[2][0] = top[0][0]
    top[0][0] = right[0][2]
    right[0][2] = bottom[2][2]
    bottom[2][2] = temp
    temp = back[0][0]
    back[0][0] = back[2][0]
    back[2][0] = back[2][2]
    back[2][2] = back[0][2]
    back[0][2] = temp
    temp = back[0][1]
    back[0][1] = back[1][0]
    back[1][0] = back[2][1]
    back[2][1] = back[1][2]
    back[1][2] = temp
    total.append('b')


def bp():
    temp = left[0][0]
    left[0][0] = bottom[2][0]
    bottom[2][0] = right[2][2]
    right[2][2] = top[0][2]
    top[0][2] = temp
    temp = left[1][0]
    left[1][0] = bottom[2][1]
    bottom[2][1] = right[1][2]
    right[1][2] = top[0][1]
    top[0][1] = temp
    temp = left[2][0]
    left[2][0] = bottom[2][2]
    bottom[2][2] = right[0][2]
    right[0][2] = top[0][0]
    top[0][0] = temp
    temp = back[0][0]
    back[0][0] = back[0][2]
    back[0][2] = back[2][2]
    back[2][2] = back[2][0]
    back[2][0] = temp
    temp = back[0][1]
    back[0][1] = back[1][2]
    back[1][2] = back[2][1]
    back[2][1] = back[1][0]
    back[1][0] = temp
    total.append('b\'')


def whitecenter(colors):

        if front[2][1] == 'w' and bottom[0][1] == colors:
            f()
            f()
            up()
            rp()
            f()
            r()
        elif front[1][2] == colors and right[1][0] == 'w':
            f()
        elif front[1][2] == 'w' and right[1][0] == colors:
            r()
            u()
            f()
            f()
        elif front[0][1] == colors and top[2][1] == 'w':
            f()
            f()
        elif front[0][1] == 'w' and top[2][1] == colors:
            u()
            l()
            fp()
            lp()
        elif front[1][0] == colors and left[1][2] == 'w':
            fp()
        elif front[1][0] == 'w' and left[1][2] == colors:
            lp()
            up()
            l()
            f()
            f()
        elif bottom[1][0] == colors and left[2][1] == 'w':
            lp()
            fp()
            l()
        elif bottom[1][0] == 'w' and left[2][1] == colors:
            l()
            l()
            up()
            f()
            f()
        elif bottom[2][1] == colors and back[2][1] == 'w':
            bp()
            bp()
            u()
            rp()
            f()
            r()
        elif bottom[2][1] == 'w' and back[2][1] == colors:
            b()
            b()
            u()
            u()
            f()
            f()
        elif bottom[1][2] == colors and right[2][1] == 'w':
            r()
            f()
        elif bottom[1][2] == 'w' and right[2][1] == colors:
            r()
            r()
            u()
            f()
            f()
        elif top[1][0] == colors and left[0][1] == 'w':
            l()
            fp()
            lp()
        elif top[1][0] == 'w' and left[0][1] == colors:
            up()
            f()
            f()
        elif top[0][1] == colors and back[0][1] == 'w':
            u()
            rp()
            f()
            r()
        elif top[0][1] == 'w' and back[0][1] == colors:
            u()
            u()
            f()
            f()
        elif top[1][2] == colors and right[0][1] == 'w':
            rp()
            f()
            r()
        elif top[1][2] == 'w' and right[0][1] == colors:
            u()
            f()
            f()
        elif left[1][0] == colors and back[1][2] == 'w':
            l()
            up()
            lp()
            f()
            f()
        elif left[1][0] == 'w' and back[1][2] == colors:
            l()
            l()
            fp()
            l()
            l()
        elif right[1][2] == colors and back[1][0] == 'w':
            rp()
            u()
            r()
            f()
            f()
        elif right[1][2] == 'w' and back[1][0] == colors:
            r()
            r()
            f()
            rp()
            rp()
        total.append('y\'')


def switchtop():
    temp = top[0][0]
    top[0][0] = top[0][2]
    top[0][2] = top[2][2]
    top[2][2] = top[2][0]
    top[2][0] = temp
    temp = top[0][1]
    top[0][1] = top[1][2]
    top[1][2] = top[2][1]
    top[2][1] = top[1][0]
    top[1][0] = temp
    temp = bottom[0][0]
    bottom[0][0] = bottom[2][0]
    bottom[2][0] = bottom[2][2]
    bottom[2][2] = bottom[0][2]
    bottom[0][2] = temp
    temp = bottom[0][1]
    bottom[0][1] = bottom[1][0]
    bottom[1][0] = bottom[2][1]
    bottom[2][1] = bottom[1][2]
    bottom[1][2] = temp

def sexymoves():
        r()
        u()
        rp()
        up()


def whitecorners(colorl, colorr):
    if front[0][2] == 'w' and top[2][2] == colorl and right[0][0] == colorr:
        u()
        r()
        up()
        rp()
    elif front[0][2] == colorl and top[2][2] == colorr and right[0][0] == 'w':
        sexymoves()
    elif front[0][2] == colorr and top[2][2] == 'w' and right[0][0] == colorl:
        sexymoves()
        sexymoves()
        sexymoves()
    elif (top[0][0] == 'w' and left[0][0] == colorl and back[0][2] == colorr):
        u()
        u()
        sexymoves()
        sexymoves()
        sexymoves()
    elif (top[0][0] == colorl and left[0][0] == colorr and back[0][2] == 'w'):
        up()
        r()
        up()
        rp()
    elif (top[0][0] == colorr and left[0][0] == 'w' and back[0][2] == colorl):
        u()
        u()
        sexymoves()
    elif (top[0][2] == 'w' and back[0][0] == colorl and right[0][2] == colorr):
        u()
        sexymoves()
        sexymoves()
        sexymoves()
    elif (top[0][2] == colorr and back[0][0] == 'w' and right[0][2] == colorl):
        u()
        sexymoves()
    elif (top[0][2] == colorl and back[0][0] == colorr and right[0][2] == 'w'):
        u()
        u()
        r()
        up()
        rp()
    elif (top[2][0] == 'w' and front[0][0] == colorl and left[0][2] == colorr):
        up()
        sexymoves()
        sexymoves()
        sexymoves()
    elif (top[2][0] == colorl and front[0][0] == colorr and left[0][2] == 'w'):
        r()
        up()
        rp()
    elif (top[2][0] == colorr and front[0][0] == 'w' and left[0][2] == colorl):
        up()
        sexymoves()
    elif (bottom[0][0] == 'w' and left[2][2] == colorl and front[2][0] == colorr):
        lp()
        up()
        l()
        sexymoves()
    elif (bottom[0][0] == colorl and left[2][2] == colorr and front[2][0] == 'w'):
        lp()
        up()
        l()
        sexymoves()
        sexymoves()
        sexymoves()
    elif (bottom[0][0] == colorr and left[2][2] == 'w' and front[2][0] == colorl):
        lp()
        up()
        l()
        u()
        r()
        up()
        rp()
    elif (bottom[0][2] == colorl and front[2][2] == colorr and right[2][0] == 'w'):
        sexymoves()
        sexymoves()
    elif (bottom[0][2] == colorr and front[2][2] == 'w' and right[2][0] == colorl):
        fp()
        up()
        f()
        u()
        u()
        r()
        up()
        rp()
    elif (bottom[2][0] == 'w' and left[2][0] == colorr and back[2][2] == colorl):
        l()
        u()
        lp()
        u()
        u()
        r()
        up()
        rp()
    elif (bottom[2][0] == colorl and left[2][0] == 'w' and back[2][2] == colorr):
        l()
        u()
        lp()
        u()
        sexymoves()
    elif (bottom[2][0] == colorr and left[2][0] == colorl and back[2][2] == 'w'):
        l()
        u()
        lp()
        u()
        sexymoves()
        sexymoves()
        sexymoves()
    elif (bottom[2][2] == 'w' and back[2][0] == colorr and right[2][2] == colorl):
        rp()
        u()
        u()
        r()
        up()
        sexymoves()

    elif (bottom[2][2] == colorl and back[2][0] == 'w' and right[2][2] == colorr):
        rp()
        u()
        r()
        u()
        sexymoves()
    elif (bottom[2][2] == colorr and back[2][0] == colorl and right[2][2] == 'w'):
        rp()
        up()
        r()
        up()
        r()
        up()
        rp()
    total.append('y\'')


def f2lmovel():
    u()
    r()
    up()
    rp()
    up()
    fp()
    u()
    f()


def f2lmover():
    up()
    fp()
    u()
    f()
    u()
    r()
    up()
    rp()


def f2l(colorl,colorr):
    if front[1][2] == colorr and right[1][0] == colorl:
        r()
        up()
        rp()
        u()
        fp()
        u()
        u()
        f()
        u()
        u()
        fp()
        u()
        f()
    elif front[1][0] == colorl and left[1][2] == colorr:
        f()
        up()
        fp()
        up()
        lp()
        u()
        l()
        u()
        f2lmovel()
    elif front[1][0] == colorr and left[1][2] == colorl:
        f()
        up()
        fp()
        up()
        lp()
        u()
        l()
        f2lmover()
    elif left[1][0] == colorr and back[1][2] == colorl:
        l()
        up()
        lp()
        up()
        bp()
        u()
        b()
        up()
        f2lmover()
    elif left[1][0] == colorl and back[1][2] == colorr:
        l()
        up()
        lp()
        up()
        bp()
        u()
        b()
        f2lmovel()
    elif right[1][2] == colorl and back[1][0] == colorr:
        rp()
        u()
        r()
        u()
        b()
        up()
        bp()
        f2lmovel()
    elif right[1][2] == colorr and back[1][0] == colorl:
        rp()
        u()
        r()
        u()
        b()
        up()
        bp()
        up()
        f2lmover()
    elif front[0][1] == colorl and top[2][1] == colorr:
        f2lmovel()
    elif front[0][1] == colorr and top[2][1] == colorl:
        up()
        f2lmover()
    elif left[0][1] == colorl and top[1][0] == colorr:
        up()
        f2lmovel()
    elif left[0][1] == colorr and top[1][0] == colorl:
        u()
        u()
        f2lmover()
    elif back[0][1] == colorl and top[0][1] == colorr:
        u()
        u()
        f2lmovel()
    elif back[0][1] == colorr and top[0][1] == colorl:
        u()
        f2lmover()
    elif right[0][1] == colorl and top[1][2] == colorr:
        u()
        f2lmovel()
    elif right[0][1] == colorr and top[1][2] == colorl:
        f2lmover()
    total.append('y\'')


def yellowcross():
    if top[0][1] != 'y' and top[1][0] != 'y' and top[1][2] != 'y' and top[2][1] != 'y':
        f()
        sexymoves()
        fp()
        u()
        u()
        f()
        sexymoves()
        sexymoves()
        fp()
    elif top[0][1] == 'y' and top[1][0] == 'y' and top[1][2] != 'y' and top[2][1] != 'y':
        f()
        sexymoves()
        sexymoves()
        fp()
    elif top[0][1] != 'y' and top[1][0] == 'y' and top[1][2] != 'y' and top[2][1] == 'y':
        u()
        f()
        sexymoves()
        sexymoves()
        fp()
    elif top[0][1] != 'y' and top[1][0] != 'y' and top[1][2] == 'y' and top[2][1] == 'y':
        u()
        u()
        f()
        sexymoves()
        sexymoves()
        fp()
    elif top[0][1] == 'y' and top[1][0] != 'y' and top[1][2] == 'y' and top[2][1] != 'y':
        up()
        f()
        sexymoves()
        sexymoves()
        fp()
    elif top[0][1] != 'y' and top[1][0] == 'y' and top[1][2] == 'y' and top[2][1] != 'y':
        f()
        sexymoves()
        fp()
    elif top[0][1] == 'y' and top[1][0] != 'y' and top[1][2] != 'y' and top[2][1] == 'y':
        u()
        f()
        sexymoves()
        fp()
    total.append('yes')


def yellowcorners():
    if top[0][0] != 'y' and top[0][2] != 'y' and top[2][0] != 'y' and top[2][2] != 'y':
        if left[0][2] == 'y' and front[0][2] == 'y':
            crossfirst()
        elif back[0][2] == 'y' and left[0][2] == 'y':
            up()
            crossfirst()
        elif right[0][2] == 'y' and back[0][2] == 'y':
            u()
            u()
            crossfirst()
        elif front[0][2] == 'y' and right[0][2] == 'y':
            u()
            crossfirst()
        elif left[0][0] == 'y' and left[0][2] == 'y':
            u()
            crosssecond()
        elif front[0][0] == 'y' and front[0][2] == 'y':
            crosssecond()
    elif top[0][0] == 'y' and top[0][2] != 'y' and top[2][0] != 'y' and top[2][2] != 'y':
        if left[0][2] == 'y':
            up()
            fishone()
        else:
            u()
            fishtwo()
    elif top[0][0] != 'y' and top[0][2] == 'y' and top[2][0] != 'y' and top[2][2] != 'y':
        if back[0][2] == 'y':
            u()
            u()
            fishone()
        else:
            fishtwo()
    elif top[0][0] != 'y' and top[0][2] != 'y' and top[2][0] == 'y' and top[2][2] != 'y':
        if front[0][2] == 'y':
            fishone()
        else:
            u()
            u()
            fishtwo()
    elif top[0][0] != 'y' and top[0][2] != 'y' and top[2][0] != 'y' and top[2][2] == 'y':
        if right[0][2] == 'y':
            u()
            fishone()
        else:
            up()
            fishtwo()
    elif top[0][0] == 'y' and top[0][2] == 'y' and top[2][0] != 'y' and top[2][2] != 'y':
        if front[0][0] == 'y':
            spaceone()
        else:
            u()
            spacetwo()
    elif top[0][0] != 'y' and top[0][2] == 'y' and top[2][0] != 'y' and top[2][2] == 'y':
        if left[0][0] == 'y':
            up()
            spaceone()
        else:
            spacetwo()
    elif top[0][0] != 'y' and top[0][2] != 'y' and top[2][0] == 'y' and top[2][2] == 'y':
        if back[0][0] == 'y':
            u()
            u()
            spaceone()
        else:
            up()
            spacetwo()
    elif top[0][0] == 'y' and top[0][2] != 'y' and top[2][0] == 'y' and top[2][2] != 'y':
        if right[0][0] == 'y':
            u()
            spaceone()
        else:
            u()
            u()
            spacetwo()
    elif top[0][0] == 'y' and top[0][2] != 'y' and top[2][0] != 'y' and top[2][2] == 'y':
        if front[0][0] == 'y':
            u()
            doublefish()
        else:
            up()
            doublefish()
    elif top[0][0] != 'y' and top[0][2] == 'y' and top[2][0] == 'y' and top[2][2] != 'y':
        if front[0][2] == 'y':
            doublefish()
        else:
            u()
            u()
            doublefish()
    total.append('yes')


def crossfirst():
    r()
    u()
    u()
    r()
    r()
    up()
    r()
    r()
    up()
    r()
    r()
    u()
    u()
    r()


def crosssecond():
    r()
    u()
    u()
    rp()
    up()
    r()
    u()
    rp()
    up()
    r()
    up()
    rp()


def fishone():
    r()
    u()
    rp()
    u()
    r()
    u()
    u()
    rp()


def fishtwo():
    r()
    u()
    u()
    rp()
    up()
    r()
    up()
    rp()


def spaceone():
    r()
    r()
    d()
    rp()
    u()
    u()
    r()
    dp()
    rp()
    u()
    u()
    rp()


def spacetwo():
    l()
    f()
    rp()
    fp()
    lp()
    f()
    r()
    fp()


def doublefish():
    fp()
    l()
    f()
    rp()
    fp()
    lp()
    f()
    r()


def permcorners():
    if back[0][0] != back[0][2] and right[0][0] != right[0][2] and front[0][0] != front[0][2] and left[0][0] != left[0][2]:
        headlights()
        u()
        headlights()
    elif left[0][0] == left[0][2] and right[0][0] != right[0][2]:
        u()
        headlights()
    elif back[0][0] == back[0][2] and front[0][0] != front[0][2]:
        headlights()
    elif right[0][0] == right[0][2] and left[0][0] != left[0][2]:
        up()
        headlights()
    elif front[0][0] == front[0][2] and back[0][0] != back[0][2]:
        u()
        u()
        headlights()
    total.append('yes')


def headlights():
    rp()
    f()
    rp()
    b()
    b()
    r()
    fp()
    rp()
    b()
    b()
    r()
    r()


def permedges():
    if front[0][0] != front[0][1] and left[0][0] != left[0][1] and back[0][0] != back[0][1] and right[0][0] != right[0][1]:
        if front[0][1] == back[0][0]:
            r()
            r()
            l()
            l()
            d()
            r()
            r()
            l()
            l()
            u()
            u()
            r()
            r()
            l()
            l()
            d()
            r()
            r()
            l()
            l()
        elif front[0][1] == right[0][0]:
            r()
            r()
            l()
            l()
            d()
            r()
            r()
            l()
            l()
            u()
            l()
            rp()
            f()
            f()
            r()
            r()
            l()
            l()
            b()
            b()
            l()
            rp()
        else:
            u()
            r()
            r()
            l()
            l()
            d()
            r()
            r()
            l()
            l()
            u()
            l()
            rp()
            f()
            f()
            r()
            r()
            l()
            l()
            b()
            b()
            l()
            rp()
    elif front[0][0] != front[0][1] and left[0][0] != left[0][1] and back[0][0] == back[0][1] and right[0][0] != right[0][1]:
        uses()
    elif front[0][0] != front[0][1] and left[0][0] == left[0][1] and back[0][0] != back[0][1] and right[0][0] != right[0][1]:
        u()
        uses()
    elif front[0][0] == front[0][1] and left[0][0] != left[0][1] and back[0][0] != back[0][1] and right[0][0] != right[0][1]:
        u()
        u()
        uses()
    elif front[0][0] != front[0][1] and left[0][0] != left[0][1] and back[0][0] != back[0][1] and right[0][0] == right[0][1]:
        up()
        uses()


def uses():
    if right[0][1] == front[0][0]:
        permleft()
    else:
        permright()


def permleft():
    lp()
    u()
    lp()
    up()
    lp()
    up()
    lp()
    u()
    l()
    u()
    l()
    l()


def permright():
    r()
    up()
    r()
    u()
    r()
    u()
    r()
    up()
    rp()
    up()
    r()
    r()


def lasttwist():
    while front[0][0] != front[1][1]:
        u()


def inputs(side):
    for i in range(0, 3):
        print(f"{side}{(3*i) + 1}")
        x = input()
        print(f"{side}{(3*i) + 2}")
        y = input()
        print(f"{side}{(3*i) + 3}")
        z = input()
        temp = x + ' ' + y + ' ' + z + '\n'
        opfile.write(temp)
        

print("There are two ways to input your Rubik's Cube, one is by a file and one will be through the terminal. ")
print("In order to input to a file, you must open a text file and input the colors of the pieces in order.")
print("To do this, start with the red center facing you, the white center facing down.")
print("From here start input the colors from top left to bottom right just like reading a book")
print("Each color should be seperated by a space and each row should be ended with a new line.")
print("Once you have inputed the front face, rotate the rubik's cube so that the blue center is facing you and white center is facing down.")
print("Repeat the input process. Then rotate so that the green center is facing you and white center is down.")
print("Repeat the input process. Then rotate so that the orange center is facing you and white center is down.")
print("Repeat the input process. Then rotate so that the yellow center is facing you and red center is down.")
print("Repeat the input process. Then rotate so that the white center is facing you and orange center is down.")
print("This is also how you should input via the terminal.")
print("Would you like to use a correctly formatted file or input on screen? (1 or 2)")
option = int(input())
if option == 1:
    print("Input file name")
    name = input()
    file = open(name, 'r')
else:
    opfile = open("Input.txt", 'w')
    inputs('front')
    inputs('left')
    inputs('right')
    inputs('back')
    inputs('top')
    inputs('bottom')
    opfile.close()
    yes = 0
    file = open("Input.txt", 'r')
total = []
sides = []
front = []
left = []
right = []
back = []
top = []
bottom = []
grabFile()
file.close()
sides.append(front)
sides.append(left)
sides.append(right)
sides.append(back)
sides.append(top)
sides.append(bottom)
color = 'r'
whitecenter(color)
temp = front
front = left
left = back
back = right
right = temp
switchtop()
color = 'b'
whitecenter('b')
temp = front
front = left
left = back
back = right
right = temp
switchtop()
color = 'o'
whitecenter('o')
temp = front
front = left
left = back
back = right
right = temp
switchtop()
color = 'g'
whitecenter('g')
switchtop()
temp = front
front = left
left = back
back = right
right = temp

whitecorners('r', 'g')
temp = front
front = left
left = back
back = right
right = temp
switchtop()
whitecorners('b', 'r')
temp = front
front = left
left = back
back = right
right = temp
switchtop()
whitecorners('o', 'b')
temp = front
front = left
left = back
back = right
right = temp
switchtop()
whitecorners('g', 'o')
temp = front
front = left
left = back
back = right
right = temp
switchtop()

f2l('r', 'g')
temp = front
front = left
left = back
back = right
right = temp
switchtop()
f2l('b', 'r')
temp = front
front = left
left = back
back = right
right = temp
switchtop()
f2l('o', 'b')
temp = front
front = left
left = back
back = right
right = temp
switchtop()
f2l('g', 'o')
temp = front
front = left
left = back
back = right
right = temp
switchtop()
yellowcross()
yellowcorners()
permcorners()
permedges()
lasttwist()
temp = total
color = 32
print("Here is your solution.")

for i in range(0,len(total)):
    if total[i] == 'y\'':
        print(total[i])
    elif total[i] == 'yes':
        print('')
    else:
        print(total[i], end=' ')



