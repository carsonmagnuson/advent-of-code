local file = io.open("input.txt", "r")

local list1 = {}
local list2 = {}

for line in file:lines() do
    local part1, part2 = line:match("(%S+)%s+(%S+)")
    table.insert(list1, part1)
    table.insert(list2, part2)
end

file:close()

table.sort(list1)
table.sort(list2)
local s = 0
local m = 0
local frequencyMap = {}

for _, item in ipairs(list2) do
  frequencyMap[item] = (frequencyMap[item] or 0) + 1
end


for i,v in ipairs(list1) do
  s = s + math.abs(v - list2[i])
  m = m + (v*(frequencyMap[v] or 0))
end


print(s)
print(m)
