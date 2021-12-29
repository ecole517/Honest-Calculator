msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
memory = "0"
msgs = [""] * 3
msgs[0] = "Are you sure? It is only one digit! (y / n)"
msgs[1] = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msgs[2] = "Last chance! Do you really want to embarrass yourself? (y / n)"


def is_one_digit(v):
    if -10 < v < 10 and v == round(v):
        return True
    return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if v1 == 1 or v2 == 1 and v3 == "*":
        msg += msg_7
    if v1 == 0 or v2 == 0 and v3 == "*":
        msg += msg_8
    if msg:
        msg = msg_9 + msg
        print(msg)


while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split(" ")
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
    else:
        if oper not in "*/+-":
            print(msg_2)
        else:
            check(x, y, oper)
            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/" and y != 0:
                result = x / y
            else:
                print(msg_3)
                continue
            print(result)
            while True:
                print(msg_4)
                answer = input()
                if answer == "y":
                    if is_one_digit(result):
                        msg_index = 0
                        while msg_index < 3:
                            print(msgs[msg_index])
                            answer = input()
                            if answer == "y":
                                msg_index += 1
                                if msg_index == 3:
                                    break
                            elif answer == "n":
                                msg_index = 4
                                break
                        if msg_index == 3:
                            memory = str(result)
                            break
                        elif msg_index == 4:
                            break
                    else:
                        memory = str(result)
                        break
                elif answer == "n":
                    break

            while True:
                print(msg_5)
                answer = input()
                if answer == "y":
                    break
                elif answer == "n":
                    exit()
