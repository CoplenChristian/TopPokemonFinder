import json, requests
import heapq
import operator

def execute(id, gen):
    index = id
    maxStat = 0
    statsList = []
    nameList = []
    if gen == 0:
        gen_nums = 890
        min_num = 1
    if gen == 1:
        gen_nums = 151
        min_num = 1
    if gen == 2:
        gen_nums =251
        min_num = 152
    if gen == 3:
        gen_nums =386
        min_num = 252
    if gen == 4:
        gen_nums = 493
        min_num = 387
    if gen == 5:
        gen_nums = 649
        min_num = 494
    if gen == 6:
        gen_nums = 721
        min_num = 650
    if gen == 7:
        gen_nums = 807
        min_num = 722
    if gen == 8:
        gen_nums = 890
        min_num = 810
    for i in range(min_num, gen_nums):
        try:
            response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(i))
            info = json.loads(response.content)
            stat = info['stats'][id]['base_stat']
            name = info['name']
        except:
            pass
        statsList.append(stat)
        nameList.append(name)
        
    return(sorted(zip(statsList, nameList), reverse=True)[:6])