from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        created = {}

        def dfs(node):
            print(node.val)
            if node.val not in created:
                created[node.val] = Node(node.val)
                for nei in node.neighbors:
                    created[node.val].neighbors.append(dfs(nei))

            return created[node.val]

        if not node:
            return node

        return dfs(node)
