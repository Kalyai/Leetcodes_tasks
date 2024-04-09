def get_day_of_week(day):
    if day[0:2] == 'Mo':
        return 0
    elif day[0:2] == 'Tu':
        return 1
    elif day[0:2] == 'We':
        return 2
    elif day[0:2] == 'Th':
        return 3
    elif day[0:2] == 'Fr':
        return 4
    elif day[0:2] == 'Sa':
        return 5
    return 6

def init_day_of_week(day):
    if day == 0:
        return 'Monday'
    elif day == 1:
        return 'Tuesday'
    elif day == 2:
        return 'Wednesday'
    elif day == 3:
        return 'Thursday'
    elif day == 4:
        return 'Friday'
    elif day == 5:
        return 'Saturday'
    return 'Sunday'

def main(n, year):
    days = list()
    for i in range(n):
        day, month = input().split()
        days.append(int(day) + months[month])

    d_w = input()
    day_of_week = get_day_of_week(d_w)
    for i in range(7):
        weeks[i] = 52
    weeks[day_of_week] += 1

    if (f - 28): weeks[(day_of_week + 1) % 7] += 1

    for d in days:
        weeks[((d + day_of_week) % 7) - 1] -= 1

    ma, mi = -1, 54
    res_ma, res_mi = '', ''
    for i in range(7):
        if weeks[i] > ma:
            ma = weeks[i]
            res_ma = i
        if weeks[i] < mi:
            mi = weeks[i]
            res_mi = i
    res_ma = init_day_of_week(res_ma)
    res_mi = init_day_of_week(res_mi)
    return (f'{res_ma} {res_mi}')

if __name__ == '__main__':
    n = int(input())
    year = int(input())
    weeks = [0] * 7
    f = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
    months = {
        'January': 0,
        'February': 31,
        'March': f + 31,
        'April': f + 31 * 2,
        'May': f + 30 + 31 * 2,
        'June': f + 30 + 31 * 3,
        'July': f + 30 * 2 + 31 * 3,
        'August': f + 30 * 2 + 31 * 4,
        'September': f + 30 * 2 + 31 * 5,
        'October': f + 30 * 3 + 31 * 5,
        'November': f + 30 * 3 + 31 * 6,
        'December': f + 30 * 4 + 31 * 6
    }
    print(main(n, year))
