def solution(my_string):
    answer = []
    for i in range(1, len(my_string)+1):
        answer.append(my_string[-i:])
        print(answer)
    
    answer.sort()
    return answer