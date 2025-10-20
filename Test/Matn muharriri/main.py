def time_to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def seconds_to_time(sec):
    sec = sec % (12 * 3600)
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return h, m, s

def main():
    N = int(input())
    times = []
    
    for _ in range(N):
        time_str = input().strip()
        h, m, s = map(int, time_str.split(':'))
        times.append(time_to_seconds(h, m, s))
    
    times.sort()
    
    min_total_time = float('inf')
    best_time = 0
    
    for i in range(N):
        T = times[i]
        total_time = 0
        
        for j in range(N):
            if times[j] >= T:
                total_time += times[j] - T
            else:
                total_time += (12 * 3600 - T + times[j])
        
        if total_time < min_total_time:
            min_total_time = total_time
            best_time = T
        elif total_time == min_total_time and T < best_time:
            best_time = T
    
    h, m, s = seconds_to_time(best_time)
    print(f"{h}:{m:02d}:{s:02d}")

if __name__ == "__main__":
    main()