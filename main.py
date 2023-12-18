import wget


target = input("Enter target url: ")


file1 = f'{target}/robots.txt'
file2 = f'{target}/sitemap.xml'

d1 = wget.download(file1, 'path to save')
d2 = wget.download(file2, 'path to save')


