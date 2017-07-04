# Export functions
from reports import *


def export_list(function, filename):
    exportlist = function
    for i in exportlist:
        filename.write(i + ", ")
    filename.write("\n")


def export(filename="gamestat_report.txt"):
    filename = open("gamestat_report.txt", "w")

    filename.write(str(count_games("game_stat.txt")) + "\n")
    filename.write(str(decide("game_stat.txt", 2011)) + "\n") 
    filename.write(str(get_latest("game_stat.txt")) + "\n") 
    filename.write(str(count_by_genre("game_stat.txt", "First-person shooter")) + "\n") 
    filename.write(str(get_line_number_by_title("game_stat.txt", "Half-Life")) + "\n")
    export_list(sort_abc("game_stat.txt"), filename)
    export_list(get_genres("game_stat.txt"), filename)
    filename.write(str(when_was_top_sold_fps("game_stat.txt")) + "\n")     
    filename.close()

export()