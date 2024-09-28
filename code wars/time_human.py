def to_read (sec):
    sec = sec
    h = 0
    m = 0
    if sec - 3600 >0:
        while sec - 3600 > 0:
            h += 1
            sec = sec - 3600
    elif sec - 60 > 0:
        while sec - 60 > 0:
            m += 1
            sec = sec - 60
    return f"{h}:{m}:{sec}"
    
print(to_read(359999))