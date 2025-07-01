def find_average(numbers):
    if not numbers:
        return 0.0  
    return sum(numbers) / len(numbers) 

def gardners_equation(velocity):
    alpha = 0.31  # For m/s
    beta = 0.25
    density = alpha * (velocity ** beta)
    return density