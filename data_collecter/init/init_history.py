from sortedcontainers import SortedList
import os

def check_file_exists(region):
    paths = ["history/unpulled_summoner_ids_" + region + ".txt",
             "history/pulled_summoner_ids_" + region + ".txt",
             "history/unpulled_match_ids_" + region + ".txt",
             "history/upulled_match_ids_" + region + ".txt",
             ]
    for path in paths:
        if not os.path.exists(path):
            curpath = os.path.abspath(os.curdir)
            print("Current path is: %s" % (curpath))
            print("Trying to open: %s" % (os.path.join(curpath, path)))
            open(path, 'w+')


def unpulled_summoner_ids(region):
    check_file_exists(region)
    process_file = open("history/unpulled_summoner_ids_" + region + ".txt", "r")
    unpulled_summoner_ids = SortedList()
    try:
        lines = process_file.readlines()
        for line in lines:
            unpulled_summoner_ids.add(int(line))
    finally:
        process_file.close()
    return unpulled_summoner_ids

def pulled_summoner_ids(region):
    check_file_exists(region)
    process_file = open("history/pulled_summoner_ids_" + region + ".txt", "r")
    pulled_summoner_ids = SortedList()
    try:
        lines = process_file.readlines()
        for line in lines:
            pulled_summoner_ids.add(int(line))
    finally:
        process_file.close()
    return pulled_summoner_ids

def unpulled_match_ids(region):
    check_file_exists(region)
    process_file = open("history/unpulled_match_ids_" + region + ".txt", "r")
    unpulled_match_ids = SortedList()
    try:
        lines = process_file.readlines()
        for line in lines:
            unpulled_match_ids.add(int(line))
    finally:
        process_file.close()
    return unpulled_match_ids

def pulled_match_ids(region):
    check_file_exists(region)
    process_file = open("history/pulled_match_ids_" + region + ".txt", "r")
    pulled_match_ids = SortedList()
    try:
        lines = process_file.readlines()
        for line in lines:
            pulled_match_ids.add(int(line))
    finally:
        process_file.close()
    return pulled_match_ids
