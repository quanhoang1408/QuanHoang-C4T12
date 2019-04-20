phim = [
    {
        "film" :"the amazing spiderman" ,
        "year" : 2014,
        "actors" : "Bruce Wills,John Travolta"
    },
    {
        "film": "the shawshank",
        "year": 1994,
        "actors": "Tim Robbins, Bob Gunton"
    },
    {
        "film": "captain marvel",
        "year":2019,
        "actors" : "Brie Larson, Samuel Jackson"
    }
]
a= phim[0]
a["nationality"] ="america"

for i in phim :
    for k,v in i.items():
        print(k,"-",v)