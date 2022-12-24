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
    # print(bp)
    states = {(1,0,0,0) : [(0,0,0,0)]}
    bound = 0
    for t in range(steps):

        print(t, len(states), sum([len(el) for key, el in states.items()]), bound)

        max_list_len = max([len(el) for key, el in states.items()])
        els = [el for key,el in states.items() if len(el)==max_list_len]
        els[0].sort()
        new_states = {}
        for cur_state_bot, cur_state_el_list in states.items():
            for cur_state_el in cur_state_el_list:
                def add_to_new_states(special_key, special_el):
                    if not special_key in new_states:
                        new_states[special_key] = [special_el]
                    elif pareto_dominates(special_el, new_states[special_key]):
                        new_states[special_key].append(special_el)
                    return special_el[3] + (23-t)*special_key[3]

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
        for key, el in new_states.items():
            if key[1]<=bp[2][1] and key[2]<=bp[3][2] and key[0]<=(bp[1][0] + bp[2][0] + bp[3][0]): 
                states[key] = []
                for cur_el in el: 
                    if pareto_dominates(cur_el, el):
                        if cur_el[3] + (23-t)*(24-t)*max(key[3],1)//2 >= bound:
                            states[key].append(cur_el)
                states[key] = list(set(states[key]))
    return max([el[3] for key, el_list in states.items() for el in el_list])

ans = 0
for bp in tqdm.tqdm(blueprints):
    ans += bp[0]*max_geo(bp[1], 24)

print(ans)

