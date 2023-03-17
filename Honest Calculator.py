memory = float(0)
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
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_= [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

def take_input():
    print(msg_0)
    calc = input()
    x, oper, y = calc.split(" ")
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    return str(x), str(oper), str(y)

def store_to_memory(number):
    global memory
    decision = input(msg_4)
    if decision == "y" and is_one_digit(number) == False:
        memory = number
    elif decision == "n":
        pass
    else:
        msg_index = 10
        while True:
            if input(msg_[msg_index]) == "y":
                if not msg_index < 12:
                    memory = number
                    break
                else:
                    msg_index += 1
                    continue
            else:
                break


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) is True and is_one_digit(v2) is True:
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)
        return msg

def calculator():
    while True:
        x, oper, y = take_input()
        math_oper = ['+', '-', '*', '**', '/', '//', '%']
        if x.isalpha() or y.isalpha():
            print(msg_1)
        elif oper not in math_oper:
            print(msg_2)
        else:
            xx = float(x)
            yy = float(y)
            check(xx, yy, oper)
            if oper == '+':
                result = xx + yy
                print(float(result))
                return result
            elif oper == '-':
                result = xx - yy
                print(float(result))
                return result
            elif oper == '*':
                result = xx * yy
                print(float(result))
                return result
            elif oper == '/' and x or y != 0:
                try:
                    result = xx / yy
                    print(float(result))
                    return result
                except ZeroDivisionError:
                    print(msg_3)
            else:
                return



def main():
        while True:
            result = calculator()
            store_to_memory(result)
            decision = input(msg_5)
            if decision == "y":
                continue
            else:
                break

if __name__ == "__main__":
	main()
