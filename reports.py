
# Report functions


def import_file(filename):
    datas = []
    thefile = open(filename)
    for line in thefile:
        datas.append(line.split("\t"))
    return datas


def count_games(filename):
    datas = import_file(filename)
    return len(datas)


def decide(filename, year):
    datas = import_file(filename)
    for game in datas:
        if int(game[2]) == year:
            return True
    return False


def get_latest(filename):
    year = 0
    gamename = ""
    datas = import_file(filename)
    for game in datas:
        if int(game[2]) > year:
            year = int(game[2])
            gamename = game[0]
    return gamename


def count_by_genre(filename, genre):
    genrecounter = 0
    datas = import_file(filename)
    for game in datas:
        if game[3] == genre:
            genrecounter += 1
    return genrecounter


def get_line_number_by_title(filename, title):
    linecounter = 0
    datas = import_file(filename)
    for game in datas:
        linecounter += 1
        if game[0] == title:
            return linecounter


def sort_abc(filename):
    datas = import_file(filename)
    titles = []
    for game in datas:
        titles.append(game[0])
    return sorted(titles)


def get_genres(filename):
    datas = import_file(filename)
    genres = []
    for game in datas:
        genres.append(game[3])
    return sorted(set(genres), key=str.lower)


def when_was_top_sold_fps(filename):
    datas = import_file(filename)
    soldcounter = 0
    release_year = 0
    for game in datas:
        if game[3] == "First-person shooter":
            if float(game[1]) > soldcounter:
                soldcounter = float(game[1])
                release_year = game[2]
    return int(release_year)