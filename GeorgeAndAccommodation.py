class Room:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def set_p_q(px, qx):
        p = px
        q = qx


def take_input():
    n = input()
    n = int(n)
    rooms = []
    for i in range(n):
        px, qx = input().split()
        r = Room(int(px), int(qx))
        rooms.append(r)

    return n, rooms


def room_count(n,rooms):
    empty_room=0
    for room in rooms:
        if room.q-room.p>1:
            empty_room+=1

    return empty_room

def main():
    n,rooms=take_input()
    empty_room=room_count(n,rooms)
    print(empty_room)

main()
