
# Report functions
import math

def import_file(filename):
    datas = []
    thefile = open(filename)
    for line in thefile:
        datas.append(line.split("\t"))
    return datas


def sum_data(filename, data):
    datas = import_file(filename)
    data_sum = 0
    for game in datas:
        data_sum += float(game[data])
    return data_sum


def get_most_played(filename):
    datas = import_file(filename)
    sold_number = 0
    gametitle = None
    for game in datas:
        if float(game[1]) > sold_number:
            sold_number = float(game[1])
            gametitle = game[0]
    return gametitle


def sum_sold(filename):
    return sum_data("game_stat.txt", 1)


def get_selling_avg(filename):
    datas = import_file(filename)
    selling_sum = sum_sold(filename)
    return selling_sum / len(datas)

def count_longest_title(filename):
    datas = import_file(filename)
    title_length = 0
    for game in datas:
        if len(game[0]) > title_length:
            title_length = len(game[0])
    return title_length


def get_date_avg(filename):
    datas = import_file(filename)
    date_sum = sum_data(filename, 2)
    return math.ceil(date_sum / len(datas))


def get_game(filename, title):
    datas = import_file(filename)
    result = " "
    for game in datas:
        if game[0] == title:
            game[1] = int(game[1])
            game[2] = int(game[2])
            game[4] = game[4][:-1]
            return game


def count_grouped_by_genre(filename):
    datas = import_file(filename)    
    genre_dict = {}
    for game in datas:
        if game[3] in genre_dict:
            genre_dict[game[3]] += 1
        else:
            genre_dict.update({game[3]:1})
    return genre_dict


def get_date_ordered(filename):
    datas = import_file(filename)    
    title_list = []
    current_title = None
    while len(title_list) < len(datas):
        year_counter = 0
        for game in datas:
            if game[0] not in title_list:
                if int(game[2]) > year_counter:
                    current_title = game[0]
                    year_counter = int(game[2])
        title_list.append(current_title)
    return title_list
