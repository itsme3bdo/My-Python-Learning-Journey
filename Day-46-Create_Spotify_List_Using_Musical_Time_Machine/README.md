Spotify Musical Time Machine
My Project to Create Playlists from the Past

It's a fun and practical application that lets me travel back in time to any date and automatically generate a Spotify playlist of the top 100 songs from that day. I built this to practice a combination of skills, from web scraping to API integration, to create a fully functional and creative tool.

How It Works 

Web Scraping: I used the requests library to fetch the HTML content of the Billboard Hot 100 chart for a specific date and then used Beautiful Soup to parse the raw data and find the top 100 song titles.

Spotify API Integration: After getting the song titles, I used the spotipy library to connect to the Spotify API. This allowed me to search for each song and get its unique URI.

Authentication and Playlists: I learned how to handle API authentication securely using the dotenv library for environment variables. Once authenticated, I used the API to create a new, personalized playlist and add all the songs I found to it.
