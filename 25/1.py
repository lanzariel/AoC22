import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

SNAFU = [l.strip() for l in lines]

def to_base_5(num):
    high_five = 1
    cur_pow = 0
    while high_five<=num:
        high_five *= 5
        cur_pow +=1
    ans = []
    cur_num = 0
    while cur_pow>-1:
        if high_five>num:
            high_five = high_five//5
            cur_pow-=1
            ans.append(str(cur_num))
            cur_num = 0
        else:
            cur_num += 1
            num -= high_five
    return "".join(ans[1:])

def to_base_10(num_s):
    high_five = 1
    ans = 0
    for digit in num_s[::-1]:
        ans += high_five*int(digit)
        high_five*=5
    return ans

converter = {'0': '=', '1': '-', '2': '0', '3': '1', '4': '2' }
converter_inv = {el : int(key) for key,el in converter.items()}

def to_SNAFU(num):
    adder = to_base_10("2"*20)
    b5 = to_base_5(num+adder)
    semi_ans = [converter[i] for i in b5]
    semi_ans = semi_ans[::-1]
    while semi_ans and semi_ans[-1]=='0':
        semi_ans.pop()
    if len(semi_ans)==0:
        return '0'
    return ''.join(semi_ans[::-1])

def to_base_10_from_SNAFU(num_s):
    high_five = 1
    ans = 0
    for digit in num_s[::-1]:
        ans += (converter_inv[digit]-2)*high_five
        high_five *= 5
    return ans

# for i in range(40):
#     print(i, to_base_5(i), to_base_10(to_base_5(i)), to_SNAFU(i), to_base_10_from_SNAFU(to_SNAFU(i)))


print(to_SNAFU(sum([to_base_10_from_SNAFU(i) for i in SNAFU])))
