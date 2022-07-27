def solution(record):
    answer = []
    dic = dict()
    actions = []
    
    for r in record:
        info = r.split()
        action, id = info[0], info[1]
        if action in ["Enter", "Change"]:
            nickname = info[2]
            dic[id] = nickname
        actions.append((action, id))
        
    for info in actions:
        action, id = info[0], info[1]
        if action == 'Enter':
            answer.append(f'{dic[id]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{dic[id]}님이 나갔습니다.')
    
    return answer