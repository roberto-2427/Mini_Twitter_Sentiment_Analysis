import csv

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    for char in punctuation_chars:
        s = s.replace(char, "")
    return s

def get_pos(tweet_text):
    count = 0
    words = strip_punctuation(tweet_text).lower().split()
    for word in words:
        if word in positive_words:
            count += 1
    return count

def get_neg(tweet_text):
    count = 0
    words = strip_punctuation(tweet_text).lower().split()
    for word in words:
        if word in negative_words:
            count += 1
    return count

# Wortlisten laden
positive_words = []
with open("kurs_projekt/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("kurs_projekt/negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# Twitter Daten verarbeiten und Ergebnisse schreiben
with open("kurs_projekt/project_twitter_data.csv", "r") as input_file:
    reader = csv.reader(input_file)
    next(reader) # Header überspringen
    
    with open("kurs_projekt/resulting_data.csv", "w", newline='') as output_file:
        writer = csv.writer(output_file)
        #Header schreiben 
        header = ["Number of Retweets", "Number of Replies", "Positive Score", "Negative Score", "Net Score"]
        writer.writerow(header)
        
        #Jede Zeile der Twitter-Daten durchgehen
        for row in reader:
            # Daten extrahieren
            tweet_text = row[0]
            retweets = row[1]
            replies = row[2]
            
            # Scores berechnen
            pos_score = get_pos(tweet_text)
            neg_score = get_neg(tweet_text)
            net_score = pos_score - neg_score
            
         # Zeile in die neue CSV schreiben
            row_to_write = [retweets, replies, pos_score, neg_score, net_score]
            writer.writerow(row_to_write)

print("Die Datei 'resulting_data.csv' wurde erfolgreich erstellt!")