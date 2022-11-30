def take_input():
    n, t = input().split()
    queue = input()
    return n,t,queue

def str_to_arr(queue):
    new_queue = []
    for i in queue:
        new_queue.append(i)
    return new_queue

def queue_reorder(queue):
    new_queue = []
    i = 0
    while i < len(queue):
        if i != len(queue) - 1 and queue[i] == 'B' and queue[i + 1] == 'G':
            new_queue.append('G')
            new_queue.append('B')
            # print(i)
            i += 2
            # print(i)
        else:
            new_queue.append(queue[i])
            # print(i)
            i += 1
    return new_queue

def loop_and_print(new_queue,n,t):
    for i in range(int(t)):
        new_queue = queue_reorder(new_queue)

    for i in range(int(n)):
        print(new_queue[i], end="")

n,t,queue=take_input()
new_queue=str_to_arr(queue)
loop_and_print(new_queue,n,t)


