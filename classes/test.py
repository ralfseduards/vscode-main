class meth():
    def plus(self):
        pass
    def generate(self, max):
        for i in range(max):
            yield 1

answer_key = "ACBAACBBBC"
answers = "ABCBSACVAW"
score = 0
max_score = len(answer_key)

for num, char in enumerate(answer_key):
    if char == answers[int(num)]:
        score += 1
print(score)
