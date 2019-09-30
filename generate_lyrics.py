import os.path
import lyricsgenius
import numpy as np

max_songs = 25
n_words = 30
artist_input = "drake"


def markov_chain_2(lyrics):
    pairs = make_pairs(lyrics)

    word_dictionary = {}

    for word1, word2 in pairs:
        if word1 in word_dictionary.keys():
            word_dictionary[word1].append(word2)
        else:
            word_dictionary[word1] = [word2]

    first_word = np.random.choice(lyrics)
    while first_word.islower():
        first_word = np.random.choice(lyrics)

    chain = [first_word]

    for i in range(n_words):
        chain.append(np.random.choice(word_dictionary[chain[-1]]))
    return ' '.join(chain)


def make_pairs(lyrics):
    for i in range(len(lyrics)-1):
        yield (lyrics[i], lyrics[i+1])


def get_lyrics():
    song_lyrics = []
    artist_lyric_file = ("lyrics/%s-lyrics.txt" % artist_input)
    if not os.path.exists(artist_lyric_file):
        f = open(artist_lyric_file, "w+")
        genius = lyricsgenius.Genius('Au6hiQBwt7FXTU-lk7-la_pB-3DdHDiHdVj493zh-0GqHZ54tWDZwvNIpWRstzwg')
        artist = genius.search_artist(artist_input, max_songs=max_songs)
        songs = artist.songs
        for song in songs:
            song_lyrics.append(song.lyrics)
        f.write("".join(song_lyrics))
    f = open(artist_lyric_file, "r").read()
    lyrics = f.split()
    return lyrics


print(markov_chain_2(get_lyrics()))
