class Calculator:
    def buildResponse(self, input):
        answer = []
        if len(input) == 0:
            answer = [0]
        else:
            splitInput = input.split(',')
            answer = [len(splitInput)]
        return answer
