import wget


target = input("Enter target url: ")


file1 = f'{target}/robots.txt'
file2 = f'{target}/sitemap.xml'

d1 = wget.download(file1, '/Users/raedshafei/PycharmProjects/Robotsxml')
d2 = wget.download(file2, '/Users/raedshafei/PycharmProjects/Robotsxml')


