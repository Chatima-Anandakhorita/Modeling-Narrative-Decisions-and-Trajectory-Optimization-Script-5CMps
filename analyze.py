# analyze_story.py

import heapq
from story_data import GRAPH

def dijkstra_min_trauma(graph, start):
    """
    Finds the path of absolute minimum trauma cost out of a given start state.
    Returns: (total_cost, step_by_step_path_list)
    """
    queue = [(0, start, [])]
    visited = set()
    
    while queue:
        cost, node, path = heapq.heappop(queue)
        
        if node in visited:
            continue
        visited.add(node)
        
        current_path = path + [node]
        
        if not graph[node]["connections"]:
            return cost, current_path
            
        for conn in graph[node]["connections"]:
            if conn["target"] not in visited:
                heapq.heappush(queue, (cost + conn["c"], conn["target"], current_path))

def run_dfs_all_timelines(graph, current, current_path=None, current_cost=0, current_prob=1.0, loop_executed=False):
    """
    Traverses every timeline variation using DFS tracking.
    Safely captures the unique cyclic self-loop exactly once without triggering infinite recursion.
    """
    if current_path is None:
        current_path = []
        
    current_path = current_path + [current]
    
    if not graph[current]["connections"]:
        print(f"🏁 TERMINAL ENDING: {current}")
        print(f"   ↳ Timeline Path: {' -> '.join(current_path)}")
        print(f"   ↳ Cumulative Trauma Debt: {current_cost}")
        print(f"   ↳ Global Probability Matrix: {current_prob:.4f} ({current_prob * 100:.1f}%)\n")
        return

    for conn in graph[current]["connections"]:
        target = conn["target"]
        
        if target == current:
            if current == "Depressed_Adult_Life" and not loop_executed:
                run_dfs_all_timelines(
                    graph, target, current_path, 
                    current_cost + conn["c"], current_prob * conn["p"], 
                    loop_executed=True
                )
            else:
                continue
        else:
            run_dfs_all_timelines(
                graph, target, current_path, 
                current_cost + conn["c"], current_prob * conn["p"], 
                loop_executed
            )

if __name__ == "__main__":
    print("=" * 75)
    print("   DFS NARRATIVE SPECTRUM ANALYSIS: ALL BRANCHING LIFE TRACKS")
    print("=" * 75 + "\n")
    run_dfs_all_timelines(GRAPH, "Primary_School_Graduation")

    print("=" * 75)
    print("   DIJKSTRA SYSTEM OPTIMAL EVALUATION (MINIMUM EMOTIONAL RESISTANCE)")
    print("=" * 75)
    
    total_trauma, optimal_route = dijkstra_min_trauma(GRAPH, "Primary_School_Graduation")
    print(f"\n🟢 Mathematically Optimal Survival Strategy Path:")
    print(f"   ↳ Route: {' -> '.join(optimal_route)}")
    print(f"   ↳ Minimum Achievable Trauma Score: {total_trauma}\n")