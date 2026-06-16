import subprocess
import sys

COMMON_WORDS = [
    # articles and determiners
    "the", "a", "an", "this", "that", "these", "those", "my", "your", "his", "her", "its", "our", "their",
    # prepositions
    "of", "in", "to", "for", "with", "on", "at", "from", "by", "about", "as", "into", "through", "during",
    # conjunctions
    "and", "but", "or", "nor", "so", "yet", "both", "either", "neither", "although", "because", "since", "while",
    # pronouns
    "i", "you", "he", "she", "it", "we", "they", "me", "him", "us", "them", "who", "what", "which",
    # common verbs
    "be", "is", "are", "was", "were", "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "must", "shall", "can", "get", "got", "make", "know", "think", "take", "see",
    "come", "go", "say", "said", "tell", "told", "use", "find", "give", "want", "look", "seem", "feel",
    # common nouns
    "time", "year", "people", "way", "day", "man", "woman", "child", "world", "life", "hand", "part",
    "place", "case", "week", "company", "system", "program", "question", "work", "government", "number",
    # common adjectives
    "good", "new", "first", "last", "long", "great", "little", "own", "right", "big", "high", "small",
    "large", "next", "early", "young", "important", "public", "private", "real", "best", "free", "able",
    # common adverbs
    "not", "also", "just", "because", "more", "also", "up", "out", "then", "well", "only", "very",
    "even", "back", "there", "down", "still", "here", "now", "how", "where", "when", "why", "never",
]

#compiling the program
cprogram = subprocess.run(["gcc", "main.c", "-o", "main"], capture_output=True, text=True)
if cprogram.returncode != 0:
    print(cprogram.stderr)
    sys.exit(1)

def decryption(txt, shift):
    binary = "main.exe" if sys.platform == "win32" else "./main"
    dec = subprocess.run([binary, "decrypt", str(shift), txt], capture_output=True, text=True)
    return dec.stdout.strip()

#####################################################3333333333

msg = input("Insert message to crack")

best_score = 0

for count in range(27): # im aware theres 26 leters in the alphabet its becaus there might be somebody just sending pure english
    cnt = 0
    msgs = decryption(msg.lower(),count)
    spl = msgs.split()

    for selected in spl:
        if selected in COMMON_WORDS: cnt+=1
    
    if cnt > best_score: best_score = count

ret = decryption(msg,best_score)
print(f"The best score was {best_score} with the message \"{ret}\"")
