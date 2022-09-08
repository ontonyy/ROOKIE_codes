import pygame as pg
from random import random
from collections import deque

cols, rows = 25, 15
TILE = 40

start = (0, 0)
queue = deque([start])
visited = {start: None}
goal = start
cur_node = start

goal_click_pos = None


def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


def get_next_nodes(x, y):
    check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows and not grid[y][x] else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]


def get_click_mouse_pos():
    x, y = pg.mouse.get_pos()
    grid_x, grid_y = x // TILE, y // TILE
    click = pg.mouse.get_pressed()
    return click, (grid_x, grid_y)


pg.init()
sc = pg.display.set_mode([cols * TILE, rows * TILE])
clock = pg.time.Clock()
# grid
grid = [[1 if random() < 0.2 else 0 for col in range(cols)] for row in range(rows)]
# dict of adjacency lists
graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if not col:
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)

while True:
    # fill screen
    sc.fill(pg.Color('black'))

    # draw grid
    [[pg.draw.rect(sc, pg.Color('darkorange'), get_rect(x, y), border_radius=TILE // 5)
      for x, col in enumerate(row) if col] for y, row in enumerate(grid)]

    [pg.draw.rect(sc, pg.Color('forestgreen'), get_rect(x, y)) for x, y in visited]
    [pg.draw.rect(sc, pg.Color('darkslategray'), get_rect(x, y)) for x, y in queue]

    # BFS logic
    click = get_click_mouse_pos()
    mouse_pos = click[1]
    goal_click = click[0][0]
    start_click = click[0][2]

    if start_click and goal_click_pos is None:
        start = mouse_pos
        queue = deque([start])
        visited = {start: None}
        goal = start
        cur_node = start

    if goal_click_pos is None:
        pg.draw.rect(sc, pg.Color('red'), get_rect(mouse_pos[0], mouse_pos[1]))

        if goal_click and not grid[mouse_pos[1]][mouse_pos[0]]:
            goal_click_pos = mouse_pos
            if goal_click_pos in visited:
                queue = deque([start])
                visited = {start: None}
                goal = start
                cur_node = start
    else:
        if queue:
            cur_node = queue.popleft()

            if cur_node == goal_click_pos:
                goal = goal_click_pos
                goal_click_pos = None

            next_nodes = graph[cur_node]
            for next_node in next_nodes:
                if next_node not in visited:
                    queue.append(next_node)
                    visited[next_node] = cur_node

    # draw path
    path_head, path_segment = goal, goal
    while path_segment:
        pg.draw.rect(sc, pg.Color('white'), get_rect(*path_segment), TILE, border_radius=TILE // 3)
        path_segment = visited[path_segment]

    pg.draw.rect(sc, pg.Color('blue'), get_rect(*start), border_radius=TILE // 3)
    pg.draw.rect(sc, pg.Color('magenta'), get_rect(*path_head), border_radius=TILE // 3)

    # pygame necessary lines
    [exit() for event in pg.event.get() if event.type == pg.QUIT]
    pg.display.flip()
    clock.tick(30)
