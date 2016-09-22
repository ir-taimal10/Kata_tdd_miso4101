

class Calculator:
    def buildResponse(self, input):
        answer = []
        if len(input) == 0:
            answer = [0, None, None, None]
        else:
            splitInput = input.split(',')
            answer.append(len(splitInput))
            answer.append(int(min(splitInput)))
            answer.append(int(max(splitInput)))
            answer.append(self.average(splitInput))
        return answer

    def average(self, split_input):
        sum = 0.0
        for i in range(0, len(split_input)):
            sum = sum + int(split_input[i])
        return sum / len(split_input)