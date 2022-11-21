class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        n=len(paths)
        return paths[n-1][1]
