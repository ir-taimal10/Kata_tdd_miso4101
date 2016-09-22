class Calculator:
    def buildResponse(self, input):
        answer = []
        if len(input) == 0:
            answer = [0, None]
        else:
            splitInput = input.split(',')
            answer.append(len(splitInput))
            answer.append(int(min(splitInput)))
        return answer
