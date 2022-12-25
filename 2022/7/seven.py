## okay so I need to somehow store a file system in such a way that I 
# can then calculate the total sum size of all directories that contain a 
# size under 100,000 themselves – files can end up being counted 
# multiple times this way.
# Okay, current idea, store the files as strings. Basically parse 
# the i line by line storing folder names as string values in 
# a list with the file name at the end, then using join and story
# that final string in the ultimate directory list. Each item in
# will be a file.

# i = open('2022/7/input.txt', 'r').read().splitlines()
# dir = []
# curr = []
# f = {}
# files = {}

# ## creating strings
# for line in i:
#     l = line.split(' ')
#     if l[1] == 'cd':
#         if l[2] == '..':
#             curr.pop()
#         else:
#             curr.append(l[2])
#             f[l[2]] = 0
#     elif l[0] != '$' and l[0] != 'dir':
#         curr.append(l[0])
#         dir.append('_'.join(curr))
#         curr.pop()

# print(dir)

# ## plugging them into a dict - hashing size to set of pathed f
# for filepath in dir:
#     fp = filepath.split('_')
#     name = fp[len(fp)-1]
#     files[name] = set()
#     for index in range(0, len(fp) - 1):
#         files[name].add(fp[index])

# print(f)

# total = 0

# ## add stuff up per folder
# for folder in f.keys():
#     for file in files.keys():
#         if folder in files[file]:
#             f[folder] += int(file)


# print(f)

# ## add it all up lmao
# for f in f.values():
#     if f <= 100000:
#         total += f

# print(total)

## this doesn't work for some reason. I'm not sure why. But recursion 
# is another option.

def r(i, nL, f):
    tally = 0
    while True:
        if len(i[nL].split(' ')) > 2: ## we have a command
            if i[nL].split(' ')[2] == '..': ## exiting a folder
                return [tally, nL, f] 
            else: ## going into a folder
                get = r(i, nL+2, f)
                f.append(get[0])
                tally, nL = tally + get[0], get[1]
        else: ## no command, so, examining files I suppose
            tally += int(i[nL].split(' ')[0]) if i[nL].split(' ')[0] != 'dir' else 0 ## add size if not dir
        if nL < len(i) - 1: ## check not end of input
            nL += 1
        else:
            return [tally, nL, f]
v = r(open('2022/7/input.txt', 'r').read().splitlines(), 0, [])
print(f'ans 1: {sum([item for item in v[2] if item <= 100000])}, ans 2: {min([item for item in v[2] if item >= 30000000 - (70000000 - v[0])])}')


