player_list = ["bob", "joe", "dave"]
def round_robin(player_list):
    for i in range(len(player_list)):
        for n in range (len(player_list)):
            print(player_list[i], "vs. ", player_list[n])

if __name__ == "__main__":
    round_robin(player_list)