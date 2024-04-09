def main():
    t_room, t_cond = map(int,input().split())
    mode = input()
    if mode == 'freeze':
        print(min(t_room, t_cond))
    elif mode == 'heat':
        print(max(t_room, t_cond))
    elif mode == 'fan':
        print(t_room)
    else:
        print(t_cond)

if __name__ == '__main__':
    main()