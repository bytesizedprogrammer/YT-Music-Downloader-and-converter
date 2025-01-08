import subprocess

array = []

with open('downloadListHere.txt', 'r') as file:
    for line in file:
        if line.strip() not in array: # line.strip() clears out excess whitespace
            array.append(line.strip())
            #print(line.strip())

for url in array:
    subprocess.run(f'yt-dlp -x {url}', shell=True) # to run the yt-dlp command on each url
    

print("Done!")