from file2 import func2
data_list = [
    {"name": "John", "age": 25, "city": "New York", "country": "USA"},
    {"name": "Emily", "age": 30, "city": "London", "country": "UK"},
    {"name": "Michael", "age": 40, "city": "Los Angeles", "country": "USA"},
    {"name": "Sophia", "age": 35, "city": "Paris", "country": "France"},
    {"name": "Daniel", "age": 28, "city": "Toronto", "country": "Canada"},
    {"name": "Alicia", "age": 45, "city": "Sydney", "country": "Australia"},
    {"name": "David", "age": 33, "city": "Berlin", "country": "Germany"},
    {"name": "Emma", "age": 27, "city": "Tokyo", "country": "Japan"},
    {"name": "Matthew", "age": 32, "city": "Seoul", "country": "South Korea"},
    {"name": "Olivia", "age": 38, "city": "Moscow", "country": "Russia"},
    {"name": "Alexander", "age": 29, "city": "Beijing", "country": "China"},
    {"name": "Isabella", "age": 31, "city": "Dubai", "country": "UAE"},
    {"name": "James", "age": 36, "city": "Rome", "country": "Italy"},
    {"name": "William", "age": 42, "city": "Mexico City", "country": "Mexico"},
    {"name": "Mia", "age": 26, "city": "São Paulo", "country": "Brazil"},
    {"name": "Benjamin", "age": 39, "city": "Cairo", "country": "Egypt"},
    {"name": "Charlotte", "age": 34, "city": "Mumbai", "country": "India"},
    {"name": "Ethan", "age": 37, "city": "Bangkok", "country": "Thailand"},
    {"name": "Amelia", "age": 41, "city": "Istanbul", "country": "Turkey"},
    {"name": "Liam", "age": 24, "city": "Nairobi", "country": "Kenya"}
]


def func1(data_list):
    received_data = func2(data_list)
    print('=============================================================')
    print(received_data,type(received_data))



if __name__ == '__main__':
    func1(data_list)