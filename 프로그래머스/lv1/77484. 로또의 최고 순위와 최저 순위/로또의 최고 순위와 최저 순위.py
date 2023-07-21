def solution(lottos, win_nums):
    match_cnt = 0
    zero_cnt = 0
    for lotto in lottos:
        if lotto == 0:
            zero_cnt += 1
        else:
            if lotto in win_nums:
                match_cnt += 1
    
    good = 7 - (match_cnt + zero_cnt)
    bad = 7 - match_cnt
    
    if good == 7:
        good = 6
    if bad == 7:
        bad = 6
    
    return [good, bad]