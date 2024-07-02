from gendiff import generate_diff

file1 = 'file1.json'
file2 = 'file2.json'

diff = generate_diff(file1, file2)
print(diff)
