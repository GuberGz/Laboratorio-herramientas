import requests

def average(values):
    total = 0
    for value in values:
        total += value
    return total / len(values)

numbers = [4, 8, 15, 16, 23, 42]
response = requests.get("https://api.github.com")

print(response.status_code)
print(average(numbers))