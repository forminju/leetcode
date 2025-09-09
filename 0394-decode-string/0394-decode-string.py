class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
        for ch in s:
            if ch != ']':
                ans.append(ch)
            else:
                # 1) 대괄호 안의 문자열 꺼내기
                curr_str = ""
                while ans and ans[-1] != '[':
                    curr_str = ans.pop() + curr_str
                ans.pop()  # '[' 제거

                # 2) 반복 횟수(숫자) 꺼내기 (여러 자리수 고려)
                curr_num = ""
                while ans and ans[-1].isdigit():
                    curr_num = ans.pop() + curr_num

                # 3) 반복한 문자열을 스택에 다시 push
                repeated = int(curr_num) * curr_str
                ans.append(repeated)

        return "".join(ans)
