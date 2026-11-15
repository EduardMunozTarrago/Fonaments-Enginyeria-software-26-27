def mitjana(lectures):
    if not lectures:
        return None
    return sum(lectures) / len(lectures)
if __name__ == '__main__':
    print(mitjana([20.0, 22.0, 24.0]))
    print(mitjana([]))
