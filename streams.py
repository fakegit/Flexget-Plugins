from plugins.BaseApi import BaseApi, SearchResultEntry
from plugins.HDAreaApi import HDAreaApi
from plugins.HDWorldApi import HDWorldApi
from plugins.MovieBlogApi import MovieBlogApi
from plugins.SerienjunkiesApi import SerienjunkiesApi

CONFIG = {"hoster":["shareonline"],"language":"german"}
COUNT_PAGES = 3
RSS_FOLDER = "/config/rss/"

#HDArea
hdAreaApi = HDAreaApi( CONFIG )
movies = hdAreaApi.feed(["top-rls","movies","neues"],COUNT_PAGES,{"only_movies":True})
series = hdAreaApi.feed(["Serien"],COUNT_PAGES,{"only_series":True,"feed_query_category":"c"})

hdAreaApi.generate_rss(movies, RSS_FOLDER + "HDArea-Movies.xml")
hdAreaApi.generate_rss(series, RSS_FOLDER + "HDArea-Series.xml")



#HDWorld
hdWorldApi = HDWorldApi( CONFIG )
movies = hdWorldApi.feed(["top-releases","neuerscheinungen","x265-filme"],COUNT_PAGES,{"only_movies":True})
series = hdWorldApi.feed(["serien"],COUNT_PAGES,{"only_series":True})

hdWorldApi.generate_rss(movies, RSS_FOLDER + "HDWorld-Movies.xml")
hdWorldApi.generate_rss(series, RSS_FOLDER + "HDWorld-Series.xml")


#MovieBlog
movieBlogApi = MovieBlogApi( CONFIG )
movies = movieBlogApi.feed(["top-releases","neuerscheinungen"],COUNT_PAGES,{"only_movies":True})
series = movieBlogApi.feed(["serien"],COUNT_PAGES,{"only_series":True})

movieBlogApi.generate_rss(movies, RSS_FOLDER + "MovieBlog-Movies.xml")
movieBlogApi.generate_rss(series, RSS_FOLDER + "MovieBlog-Series.xml")


#Serienjunkies
serienjunkiesApi = SerienjunkiesApi( CONFIG )

episodes = serienjunkiesApi.feed("episoden")
serienjunkiesApi.generate_rss(episodes,{"file_count":10,"entry_count":200,"filename": RSS_FOLDER + "rss_feed_"})





