# settings
UI = {
    "theme": "light",  # dark, light
    "colors": "green",  # green, blue, dark-blue
    "size": "700x400",
    "title": "Turing Machine (by Roman Gluschenko)",
}

TAPE = {
    "input": "10101010",
    "sign": "_",
    "position": 10,

    "rules": [
        "q0,0 -> q1,1,R",
        "q0,1 -> q1,0,R",
        "q1,0 -> q0,1,R",
        "q1,1 -> q0,0,R",
        "q0,_ -> q1,_,L",
    ],
}