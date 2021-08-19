# O(nlogk) / O(n)
class Solution:
    def reorganizeString(self, s: str) -> str:
        h = [(-1*n, c) for c, n in Counter(s).items()]
        heapify(h)
        output, last = [], (0, "")
        while h:
            count, char = heappop(h)
            output.append(char)
            if last[0] < 0:
                heappush(h, last)
            last = (count+1, char)
        output_s = "".join(output)
        return output_s if len(s) == len(output_s) else ""  
