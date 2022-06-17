SELECT S.artist, S.song, S.duration_ms, S.explicit, S.year , S.popularity ,S.danceability,
S.energy,S.key,S.loudness,SS.mode,SS.speechiness,SS.acousticness,SS.instrumentalness ,
SS.liveness,SS.valence,SS.tempo,SS.genre 
into songs_normalize
from songs1 S
INNER JOIN songs2 SS
ON S.song= SS.song 
	