import sys

path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()

tree = {}

folder_dic = {}

current_stack = [tree]
current_stack_string = [""]

for line in lines:
    line = line.strip()
    if line[:4]=="$ cd":
        f_name = line[5:]
        fold_name = "/".join(current_stack_string) + "/" + f_name
        if f_name=="..":
            current_stack.pop()
            current_stack_string.pop()
        else:
            if not fold_name in folder_dic:
                folder_dic[fold_name] = -1
            if not fold_name in current_stack[-1]:
                current_stack[-1][fold_name] = {}
            current_stack.append(current_stack[-1][fold_name])
            current_stack_string.append(f_name)
    elif line[:4]!="$ ls":
        if line[:3]!="dir":
            siz, nam = line.split()
            siz = int(siz)
            current_stack[-1][nam] = siz

def iter_f_sizer(current_folder):
    ans = 0
    for key, val in current_folder.items():
        if key in folder_dic:
            if folder_dic[key]==-1:
                # print(key, val)
                folder_dic[key] = iter_f_sizer(val)
            ans += folder_dic[key]
            # print(key, folder_dic[key])
        else:
            ans += val
    return ans
total = iter_f_sizer(tree)

# print(folder_dic)
# print(tree)
tresh = 30000000-(70000000-total)
ans = 0
print(min([x for x in folder_dic.values() if x >= tresh]))
