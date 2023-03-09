import tomatopy

first_year, last_year = 1960, 2023

with open("../data/all_movie_names.txt", "w") as f:
    for year in range(first_year, last_year + 1):
        movie_names = tomatopy.wikipedia.scrape_movie_names(year)
        for movie_name in movie_names:
            f.write(movie_name + "\n")
