def get_responses(n):
    a = {}
    for i in range(n):
        try:
            line = input("enter a pair of word ").split()
            if len(line) != 2:
                print("word pair must contain exactly two words ")
                return {}
            first = line[0]
            second = line[1]
            a[first] = second
        except Exception as e:
            print(f"Error: {e}")
            return {}
    return a
def process(responses):
    try:
        questions = input("enter your questions ").split()
        result = []
        for j in questions:
            if j in responses:
                result.append(responses[j] + " kachel!")
            else:
                result.append("kachel!")
        return result
    except Exception as e:
        print(f"Error while processing {e}")
        return []
def main():
    try:
        n, m = input("enter the number of word pairs and number of questions ").split()
        n = int(n)
        m = int(m)
        if not (1 <= n <= 1000) or not (1 <= m <= 1000):
            print("n and m must be between 1 and 1000 ")
            return
        az = ax(n)
        if not az:
            return
        result = process(az)
        print(" ".join(result))
    except ValueError as e:
        print(f"Invalid input ")
main()