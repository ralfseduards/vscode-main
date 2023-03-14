# seti ir nice prieks data storing jo dators uz glabaa par setu info : kas ir ieksaa setaa
# listam ir jaapaarbauda visi characters bet setam viss jau ir zinaams

# bet taapeec sets nav ordered un nevar arii vinu slicot
"""
a = {1,2,3,4,5,6}

print(1 in a)

a.add("viens")
a.remove(6)
print(a)
"""


#setieam var izmantot matemaatiskaas funkcijas:

# | apvienojums(abu setu locekli kopaa)
# & skeelums(tie elementi kas kopiigi)
#  a - b (kopas a elementi kas nav b)
# ^ elementi kuri nav kopiigi

a = {1,3,5,7,9}
b = {2,4,6,8,0}

print(a|b)#vajadzeetu buut 1,2,3,4,5,6,7,8,9,0
print(a&b)# tuksa kopa (set())
print(a-b)# 1,3,5,7,9
print(a^b)# taa kaa pirmajaa

skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}

print(list(skills&job_skills)[0])


print(type({1,2,3,4,5}))