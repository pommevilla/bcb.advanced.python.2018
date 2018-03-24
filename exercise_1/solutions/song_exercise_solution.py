'''
    Paul Villanueva
    BCBGSO Advanced Python Workshop
    3/23/2018

    
'''

from line_counter import line_counter 

songs = ['days_go_by.txt', 'friday.txt', 'last_friday_night.txt',
         'monday.txt', 'summer_days.txt', 'sunday.txt', 'ten_days.txt',
         'tuesday.txt', 'sunday_morning.txt']

longest_song = ""
most_lines = 0

for song in songs:
##    print line_counter(song)
    if line_counter(song) > most_lines:
        most_lines = line_counter(song)
        longest_song = song

with open(longest_song) as fin:
    song, artist = [item.strip() for item in fin.readline().strip().split("-")]
    
print "The song that had the most lines was {} by {}.\nIt was {} lines long.".format(
    song, artist, most_lines)
