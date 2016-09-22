class Calculator:
    def buildResponse(self, input):
        answer = []
        if len(input) == 0:
            answer = [0]
        else:
            answer = [len(input)]
        return answer
