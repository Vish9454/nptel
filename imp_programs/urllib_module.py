import urllib.request

with urllib.request.urlopen("https://vish9454.github.io/resume/") as f:
    print(f.read().decode('utf-8'))


print("Beginning to Download")
url='https://vish9454.github.io/resume/'
urllib.request.urlretrieve(url,'Download_by_urlretrive')
print("Downloading Finished")

