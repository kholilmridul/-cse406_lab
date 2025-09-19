def scan_disk(requests, head, direction):
    req = sorted(requests)
    left = [x for x in req if x < head]
    right = [x for x in req if x > head]
    d = direction.strip().lower()
    if d == "left":
        path = left[::-1] + right
    elif d == "right":
        path = right + left[::-1]
    else:
        return None, None
    total = 0
    cur = head
    seq = []
    for x in path:
        total += abs(cur - x)
        seq.append(x)
        cur = x
    return total, seq

if __name__ == "__main__":
    n = int(input("Enter number of requests: ").strip())
    seq = list(map(int, input("Enter request sequence: ").split()))
    head = int(input("Enter initial head position: ").strip())
    direction = input("Enter direction (left/right): ").strip()
    time, order = scan_disk(seq, head, direction)
    if time is not None:
        print("\nSeek Sequence:", [head] + order)
        print("Total Seek Time:", time)
