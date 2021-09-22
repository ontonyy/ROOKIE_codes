# Algorith to find a mango seller
from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['peggy'] = []
graph['anuj'] = []
graph['thom'] = ['khabib', 'Max']
graph['khabib'] = []
graph['max'] = []
graph['jonny'] = []

def search_in(graph):

    search_queue = deque()
    search_queue += graph['you']
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f'WE find MANGO seller! - {person}')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print("NO mango seller:(")
    return False

def person_is_seller(name):
    return name[0] == 'm' or name[0] == 'M'

if __name__ == '__main__':
    search_in(graph)
