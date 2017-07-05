# Export functions
from reports import *


def export_list(function, filename):
    exportlist = function
    counter = 0
    if exportlist == list(exportlist):
        for i in exportlist:
            if i != exportlist[len(exportlist)-1]:
                filename.write(str(i) + ", ")
            else:
                filename.write(str(i))
    else:
        for i in exportlist:
            if counter != len(exportlist):
                filename.write(i + ": " + str(exportlist[i]) + ", ")
                counter += 1
            else:
                filename.write(i + ": " + str(exportlist[i]))
                
    filename.write("\n")


def export(filename="gamestat_reportP2.txt"):
    filename = open("gamestat_reportP2.txt", "w")

    filename.write(get_most_played("game_stat.txt") + "\n")
    filename.write(str(sum_sold("game_stat.txt")) + "\n")
    filename.write(str(get_selling_avg("game_stat.txt")) + "\n")
    filename.write(str(count_longest_title("game_stat.txt")) + "\n")
    filename.write(str(get_date_avg("game_stat.txt")) + "\n")
    export_list(get_game("game_stat.txt", "Half-Life 2"), filename)
    export_list(count_grouped_by_genre("game_stat.txt"), filename)
    export_list(get_date_ordered("game_stat.txt"), filename)

    filename.close()

export()