DATA_LIST = [ 
    'Андрей 9',
    'Василий 11',
    'Роман 7',
    'X Æ A-12 45',
    'Иван Петров 3',
    'Андрей 6',
    'Роман 11',
    'Николай Рясков 0',
    'Николай Рясков 0'
    ] # Constant data

class Parse():
    def __init__(self):
        self.parsed_data = {} # Unique dictionary for every object

    def parse_data(self, data): # parsing raw data to {worker: hours} dictionary
        for worker in data:
            split = worker.rsplit(maxsplit=1) # split string at the rightmost space
            split[1] = int(split[1]) # converting hours into integer
            if split[0] in self.parsed_data:
                self.parsed_data[split[0]].append(split[1]) # if worker exists, appending hours to value
            else:
                self.parsed_data[split[0]] = [split[1]] # else creating new key-value pair

    def print_stats(self): # printing statistics of every worker
        for worker, hours in self.parsed_data.items():
            total_hours = sum(hours) # getting sum of hours
            str_hours = ', '.join(str(x) for x in hours) # removing [] from response
            print(f"{worker}: {str_hours}; sum: {total_hours}") # print statistics


some_parser = Parse() # creating new object with unique dictionary
some_parser.parse_data(data=DATA_LIST) # data kwarg for parsing any data with the same format
some_parser.print_stats() # print statistics in console