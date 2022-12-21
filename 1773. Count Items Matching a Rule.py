class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
          s = {"type": 0, "color": 1, "name": 2}
          key = s[ruleKey]
          count = 0
          for item in items:
             if item[key] == ruleValue:
                 count += 1
          return count
