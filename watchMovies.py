def twoMoviesInFlight(moviesLenght, flightLenght):
    
    # it will save movies and it will give us fast lookup for second movie
    seenMovies = set()

    for firstMovie in moviesLenght:
        # we calculate second movie lenght
        secondMovieLength = flightLenght - firstMovie
        # now we look in seenMovies set for second Movie
        if secondMovieLength in seenMovies:
            # if movie found we return True and function will terminate
            return True

        # if not found such movie we add that to List to avoid n^2 lookup
        seenMovies.add(firstMovie)
    
    # if we did'nt find any pair we return false
    return False