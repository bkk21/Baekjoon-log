def solution(my_string):
    answer = ''.join([x for x in my_string if x not in ['a', 'e','i', 'o', 'u']])
    return answer