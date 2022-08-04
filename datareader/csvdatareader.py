import os
import csv
import ast


class TrackCSVReader:

    def __init__(self, albums_csv_file: str, tracks_csv_file: str):
        # TODO
        self.__albums_csv_file = None
        self.__tracks_csv_file = None

        self.__dataset_of_tracks = []
        # Set of unique artists
        self.__dataset_of_artists = set()
        # Set of unique albums
        self.__dataset_of_albums = set()
        # Set of unique genres
        self.__dataset_of_genres = set()

    @property
    def dataset_of_tracks(self) -> list:
        return self.__dataset_of_tracks

    @property
    def dataset_of_albums(self) -> set:
        return self.__dataset_of_albums

    @property
    def dataset_of_artists(self) -> set:
        return self.__dataset_of_artists

    @property
    def dataset_of_genres(self) -> set:
        return self.__dataset_of_genres

    def read_csv_files(self):
        # TODO
        pass
