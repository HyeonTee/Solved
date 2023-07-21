from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(int) # 장르별 플레이 횟수
    play_dict = defaultdict(list) # 장르 내 노래 별 플레이 횟수, 고유번호
    
    for i in range(len(genres)):
        genre_dict[genres[i]] += plays[i]
        play_dict[genres[i]].append([plays[i], i])
    
    # genre_dict의 value 값을 기준으로 내림차순 정렬
    genre_dict = sorted(genre_dict, key = genre_dict.get, reverse = True)
    
    # play_dict에서 플레이 횟수는 내림차순, 고유번호는 오름차순 정렬
    for genre in play_dict:
        play_dict[genre].sort(key = lambda x: (-x[0], x[1]))
    
    # 재생 많이 된 장르 부터
    for genre in genre_dict:
        try: # 2개 이상이면 2개를 append
            for i in range(2):
                answer.append(play_dict[genre][i][1])
        except: # 없으면(indexError) 다음 장르로
            continue

    return answer