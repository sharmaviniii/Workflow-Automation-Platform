from typing import List, Dict

from fastapi import FastAPI  # type: ignore[import]
from fastapi.middleware.cors import CORSMiddleware  # type: ignore[import]
from pydantic import BaseModel  # type: ignore[import]

class NodePayload(BaseModel):
    id: str
    type: str

class EdgePayload(BaseModel):
    source: str
    target: str

class PipelinePayload(BaseModel):
    nodes: List[NodePayload]
    edges: List[EdgePayload]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

def is_dag(nodes: List[NodePayload], edges: List[EdgePayload]) -> bool:
    graph: Dict[str, List[str]] = {node.id: [] for node in nodes}
    for edge in edges:
        if edge.source not in graph:
            graph[edge.source] = []
        graph[edge.source].append(edge.target)

    visited: Dict[str, bool] = {}
    on_stack: Dict[str, bool] = {}

    def dfs(node_id: str) -> bool:
        visited[node_id] = True
        on_stack[node_id] = True

        for neighbor in graph.get(node_id, []):
            if not visited.get(neighbor, False):
                if dfs(neighbor):
                    return True
            elif on_stack.get(neighbor, False):
                return True

        on_stack[node_id] = False
        return False

    for node in graph:
        if not visited.get(node, False):
            if dfs(node):
                return False

    return True

@app.post('/pipelines/parse')
def parse_pipeline(payload: PipelinePayload):
    node_count = len(payload.nodes)
    edge_count = len(payload.edges)
    dag_valid = is_dag(payload.nodes, payload.edges)

    return {
        'num_nodes': node_count,
        'num_edges': edge_count,
        'is_dag': dag_valid,
    }
