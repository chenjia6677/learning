import collections


class Graph:
    @staticmethod
    def bfs(graph: dict, initial_vertex: str) -> set:
        """
        宽度优先的搜索（breadth first search，简称bfs)
        :param graph: 邻接列表形式的图
        :param initial_vertex: 起始顶点
        :return: 起始顶点可到达的顶点
        """
        # 起始顶点可到达的顶点
        result = set()
        # 队列数据结构
        queue = collections.deque(initial_vertex)
        while queue:
            # 出队列
            vertex = queue.popleft()
            result.add(vertex)
            for neighbor_vertex in graph.get(vertex, []):
                # 判断该邻居顶点是否已探索
                if neighbor_vertex in queue or neighbor_vertex in result:
                    continue
                # 进队列
                queue.append(neighbor_vertex)
        return result

    @staticmethod
    def bfs_layer_number(graph: dict, initial_vertex: str) -> dict:
        """
        使用宽度优先的搜索策略实现计算最短路径（单元边）
        :param graph: 邻接列表形式的图
        :param initial_vertex: 起始顶点
        :return: 起始顶点可到达的顶点及其所在的层（最短路径）
        """
        # 起始顶点可到达的顶点及其所在的层
        result = {initial_vertex: 0}
        # 队列数据结构
        queue = collections.deque(initial_vertex)
        while queue:
            # 出队列
            vertex = queue.popleft()
            for neighbor_vertex in graph.get(vertex, []):
                # 判断该邻居顶点是否已探索
                if neighbor_vertex in queue or neighbor_vertex in result:
                    continue
                # 进队列
                queue.append(neighbor_vertex)
                # 记录该邻居顶点所在的层
                result[neighbor_vertex] = result[vertex] + 1
        return result

    def bfs_ucc(self, graph: dict) -> dict:
        """
        使用宽度优先的搜索实现计算无向图连通分量（undirected graph connected component，简称ucc)
        :param graph: 邻接列表形式的图
        :return: 连通分量及其顶点
        """
        # 连通分量及其顶点
        result = dict()
        # 连通分量
        count = 0
        # 已探索的顶点
        explored_vertex = set()
        for vertex in graph.keys():
            if vertex in explored_vertex:
                continue
            count += 1
            # 可到达的顶点
            attainable_vertex = self.bfs(graph, vertex)
            result[count] = attainable_vertex
            explored_vertex |= attainable_vertex
        return result

    @staticmethod
    def dfs_iterative(graph: dict, initial_vertex: str) -> set:
        """
        迭代式版本的深度优先的搜索（depth first search，简称dfs)
        :param graph: 邻接列表形式的图
        :param initial_vertex: 起始顶点
        :return: 起始顶点可到达的顶点
        """
        # 起始顶点可到达的顶点
        result = set()
        # 堆栈数据结构
        queue = collections.deque(initial_vertex)
        while queue:
            # 出栈
            vertex = queue.pop()
            result.add(vertex)
            for neighbor_vertex in graph.get(vertex, []):
                # 判断该邻居顶点是否已探索
                if neighbor_vertex in queue or neighbor_vertex in result:
                    continue
                # 进栈
                queue.append(neighbor_vertex)
        return result

    def dfs_recursive(self, graph: dict, initial_vertex: str, explored_vertex: set = None) -> set:
        """
        递归式版本的深度优先的搜索（depth first search，简称dfs)
        :param graph: 邻接列表形式的图
        :param initial_vertex: 起始顶点
        :param explored_vertex: 已探索的顶点
        :return: 起始顶点可到达的顶点
        """
        if explored_vertex is None:
            explored_vertex = set(initial_vertex)
        else:
            explored_vertex.add(initial_vertex)

        for neighbor_vertex in graph.get(initial_vertex, []):
            # 判断该邻居顶点是否已探索
            if neighbor_vertex in explored_vertex:
                continue
            self.dfs_recursive(graph, neighbor_vertex, explored_vertex)
        return explored_vertex


class Dijkstra:
    """
    Dijkstra（狄杰斯特拉）最短路径算法，其功能是计算从一个起始顶点到其他所有顶点的最短路径的长度
    """

    @staticmethod
    def _min_element(data: dict):
        """
        找出值最小的元素
        :param data: 值是整数类型的字典
        :return: 最小的值及对应的键
        """
        # 初始化最小的值为无穷大
        min_value = float('inf')
        # 初始化最小的键为None
        min_key = None
        for key, value in data.items():
            if value < min_value:
                min_value = value
                min_key = key
        end_vertex, head_vertex = min_key.split('_')
        return end_vertex, head_vertex, min_value

    @staticmethod
    def _has_edge(processed_vertexes: list, graph: dict) -> bool:
        """
        判断已处理的顶点与尚未处理的顶点之间是否有边
        :param processed_vertexes: 已处理的顶点
        :param graph: 邻接列表形式的图
        :return: 是否有边
        """
        for processed_vertex in processed_vertexes:
            if graph[processed_vertex]:
                return True
        return False

    @staticmethod
    def simple(graph: dict, initial_vertex: str) -> dict:
        """
        Dijkstra（狄杰斯特拉）最短路径算法的简单实现
        :param graph: 邻接列表形式的图，边的长度非负
        :param initial_vertex: 起始顶点
        :return: 起始顶点可到达的顶点及其最短路径
        """
        # 已处理的顶点及其距离起始顶点的最短路径
        processed_vertexes = {initial_vertex: 0}
        # 主循环：已处理的顶点与尚未处理的顶点之间有边
        while Dijkstra._has_edge(processed_vertexes.keys(), graph):
            # 已处理的顶点（尾顶点）与尚未处理的顶点（头顶点）之间的边及头顶点距离起始顶点的路径
            edge = collections.defaultdict(int)
            for end_vertex, shortest_distance in processed_vertexes.items():
                # end_vertex尾顶点 head_vertex头顶点 edge_length边长
                for head_vertex, edge_length in graph.get(end_vertex, {}).items():
                    edge[f'{end_vertex}_{head_vertex}'] = shortest_distance + edge_length
            # 找出得分最低的那条边
            end_vertex, head_vertex, length = Dijkstra._min_element(edge)
            # 将得分最低的那条边的头顶点划入已经处理过的顶点
            processed_vertexes.update({head_vertex: length})
            # 删除得分最低的那条边的头顶点的入射边
            for key, value in graph.items():
                if head_vertex in value:
                    del graph[key][head_vertex]
        return processed_vertexes

    @staticmethod
    def heap(graph: dict, initial_vertex: str) -> dict:
        """
        Dijkstra（狄杰斯特拉）最短路径算法的堆实现
        :param graph: 邻接列表形式的图，边的长度非负
        :param initial_vertex: 起始顶点
        :return: 起始顶点可到达的顶点及其最短路径
        """
        pass


if __name__ == '__main__':
    # 无向图 18页图2.2（a）
    graph1 = {
        's': ['u', 'v'],
        'u': ['v', 'v', 'w'],
        'v': ['s', 'u', 'w'],
        'w': ['u', 'v'],
        'x': ['y'],
        'y': ['x'],
        'z': []
    }
    # 有向图 18页图2.2（b）
    graph2 = {
        's': ['u', 'v'],
        'u': ['v'],
        'v': [],
        'w': ['u', 'v'],
        'x': [],
        'y': ['x'],
        'z': []
    }
    # 无向图 24页图2.5
    graph3 = {
        's': ['a', 'b'],
        'a': ['s', 'c'],
        'b': ['s', 'c', 'd'],
        'c': ['a', 'd', 'b', 'e'],
        'd': ['b', 'c', 'e'],
        'e': ['c', 'd']
    }
    # 无向图 32页图2.12
    graph4 = {
        '1': ['3', '5'],
        '3': ['1', '5'],
        '5': ['1', '3', '7', '9'],
        '7': ['5'],
        '9': ['5'],
        '2': ['4'],
        '4': ['2'],
        '6': ['8', '10'],
        '8': ['6'],
        '10': ['6']
    }
    # 有向图 71页
    graph5 = {
        's': {'v': 1, 'w': 4},
        'v': {'w': 2, 't': 6},
        'w': {'t': 3},
        't': {}
    }
    # 有向图 77页
    graph6 = {
        's': {'v': 1, 't': -2},
        'v': {'t': -5},
        't': {}
    }
    G = Graph()
    # 宽度优先的搜索
    r = G.bfs(graph3, 's')
    print(r)
    # 使用宽度优先的搜索实现计算最短路径（单元边）
    r = G.bfs_layer_number(graph3, 's')
    print(r)
    # 使用宽度优先的搜索实现计算无向图连通分量（undirected graph connected component，简称ucc)
    r = G.bfs_ucc(graph4)
    print(r)
    # 迭代式版本的深度优先的搜索（depth first search，简称dfs)
    r = G.dfs_iterative(graph3, 's')
    print(r)
    # 递归式版本的深度优先的搜索（depth first search，简称dfs)
    r = G.dfs_recursive(graph3, 's')
    print(r)
    # 计算从一个起始顶点到其他所有顶点的最短路径的长度
    r = Dijkstra.simple(graph5, 's')
    print(r)
    # 计算从一个起始顶点到其他所有顶点的最短路径的长度
    r = Dijkstra.simple(graph6, 's')
    print(r)
