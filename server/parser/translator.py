def translate(name, data):

    return {
        "id": name,
        "last_update": 0,
        "keyword1": data[0][0],
        "keyword1_rating": data[0][1]["ratings"],
        "keyword1_freq": data[0][1]["freq"],
        "keyword2": data[1][0],
        "keyword2_rating": data[1][1]["ratings"],
        "keyword2_freq": data[1][1]["freq"],
        "keyword3": data[2][0],
        "keyword3_rating": data[2][1]["ratings"],
        "keyword3_freq": data[2][1]["freq"],
        "keyword4": data[3][0],
        "keyword4_rating": data[3][1]["ratings"],
        "keyword4_freq": data[3][1]["freq"],
        "keyword5": data[4][0],
        "keyword5_rating": data[4][1]["ratings"],
        "keyword5_freq": data[4][1]["freq"],
    }
