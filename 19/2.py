import sys
import re
import tqdm


path = sys.argv[1]
with open(path, 'r') as f:
    lines = f.readlines()


blueprints = []

for l in lines:
    my_re = re.search(r'Blueprint (.*?): Each ore robot costs (.*?) ore. Each clay robot costs (.*?) ore. Each obsidian robot costs (.*?) ore and (.*?) clay. Each geode robot costs (.*?) ore and (.*?) obsidian.', l.strip())
    values = [int(my_re.group(i)) for i in range(1,8)]
    cur_bp = [values[0], [(values[1],0,0,0), (values[2],0,0,0), (values[3], values[4],0,0), (values[5], 0, values[6],0)]]
    blueprints.append(cur_bp)

def pareto_dominates(t, lt):
    lt_purged = [el for el in lt if el!=t]
    if len(lt_purged)==0:
        return True
    return min([max([t[i]-cur_lt[i] for i in range(4)]) for cur_lt in lt_purged]) > 0

def max_geo(bp, steps):
    '''
    state = (ore, clay, obs, geo, ore_r, clay_r, obs_r, geo_r)
    '''
    states = {(1,0,0,0) : [(0,0,0,0)]}
    bound = 0
    for t in tqdm.tqdm(range(steps)):

        total_els = sum([len(el) for key, el in states.items()])
        new_states = {}
        for cur_state_bot, cur_state_el_list in states.items():
            for cur_state_el in cur_state_el_list:
                def add_to_new_states(special_key, special_el):
                    if special_key[1]<=bp[2][1] and special_key[2]<=bp[3][2] and special_key[0]<=(bp[1][0] + bp[2][0] + bp[3][0]): 
                        if not special_key in new_states:
                            new_states[special_key] = set([special_el])
                        elif pareto_dominates(special_el, new_states[special_key]):
                            new_states[special_key].add(special_el)
                        return special_el[3] + (31-t)*special_key[3]
                    return 0

                next_resources = tuple(cur_state_bot[i] + cur_state_el[i] for i in range(4))
                bound = max(bound, add_to_new_states(cur_state_bot, next_resources))

                for it, robot in enumerate(bp):
                    new_resources = tuple(cur_state_el[i] - robot[i] for i in range(4))
                    if min(new_resources)>=0:
                        new_resources = tuple(new_resources[i] + cur_state_bot[i] for i in range(4))
                        new_robots = list(cur_state_bot)
                        new_robots[it] += 1
                        new_robots = tuple(new_robots)
                        bound = max(bound, add_to_new_states(new_robots, new_resources))
        states = {}
        extra_dp_memo = {}
        def get_extra(t_inv, cur_key, obsi):
            if t_inv ==0:
                return 0
            my_key = (t_inv, cur_key, obsi)
            if my_key in extra_dp_memo:
                return extra_dp_memo[my_key]
            else:
                ans = cur_key[1]
                add_0 = get_extra(t_inv-1, (cur_key[0]+1, cur_key[1]), obsi + cur_key[0])
                add_1 = 0
                if obsi>=bp[3][2]:
                    add_1 = get_extra(t_inv-1, (cur_key[0], cur_key[1]+1), obsi-bp[3][2])
                ans += max(add_0, add_1)
                extra_dp_memo[my_key] = ans
                return ans
        for key, el in new_states.items():
            states[key] = set()
            for cur_el in el: 
                if pareto_dominates(cur_el, el):
                    if get_extra(steps - t -1, key[2:], cur_el[2]) + cur_el[3] > bound:
                        states[key].add(cur_el)
        if sum([len(l) for k,l in states.items()])==0:
            return bound
    return max([el[3] for key, el_list in states.items() for el in el_list])

ans = 1
for bp in tqdm.tqdm(blueprints[:3]):
    ans *= max_geo(bp[1], 32)
print(ans)
