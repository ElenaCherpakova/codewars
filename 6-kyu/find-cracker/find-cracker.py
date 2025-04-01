def find_hack(arr):
    res = []
    score_dic = {'A': 30, 'B': 20, 'C': 10, 'D': 5}
    
    for each_stud in arr:
        total = 0
        stud_name, score, arr_scores = each_stud[0], each_stud[1], each_stud[2]
        
        for grade in arr_scores:
            total += score_dic.get(grade, 0)
            
        if len(arr_scores) >= 5 and all(grade in ['A', 'B'] for grade in arr_scores):
            total += 20   
        if total > 200:
            total = 200
​
        if score > total:
            res.append(stud_name)
​
    return res