def maiorMenor(numbers):
    if len(numbers) == 0:
        return None
    return(min(numbers), max(numbers))