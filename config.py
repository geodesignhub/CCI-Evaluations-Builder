settings = {

    "aoifile": "https://gdh-data.ams3.digitaloceanspaces.com/boundaries/Jekyll-Island.geojson",
    "systems": ["URB", "IND", "FOR", "HYDRO","AG"],
    "outputdirectory": "output",
    "workingdirectory": "working",
    "ccidata": "CCI.zip",
}


processchains = {
    "URB": {
        "red": [190],
        "yellow": [],
        "green": []
    },
    "AG": {
        "red": [81,82],
        "yellow": [],
        "green": []  
    },
    
    "IND": {
        "red": [],
        "yellow": [],
        "green": [] 
    },
    
    "FOR": {
        "red": [],
        "yellow": [],
        "green": [] 
    },
    
    "HYDRO": {
        "red": [],
        "yellow": [],
        "green": [] 
    },
    

}
