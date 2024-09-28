def generate_hashtag(s):
    words = s.strip().split()
    
    if not words:
        return False
    
    hashtag = '#' + ''.join(word.capitalize() for word in words)
    
    if len(hashtag) > 140:
        return False
    
    return hashtag
    