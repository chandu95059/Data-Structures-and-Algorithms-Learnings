def graph_color(graph):
    colors={}
    k=sorted(graph,key=lambda x:len(graph[x]),reverse=True)
    l=set()
    for i in k:
        s=set()
        for j in graph[i]:
            if j in colors:
                s.add(colors[j])
        color=1
        while color in s:
            color+=1
        colors[i] = color
        l.add(color)
    print(len(l))
    return colors

l=[[0,1,1,1,1,0,0],[1,0,1,0,0,0,0],[1,1,0,0,1,1,1],[1,0,0,0,1,0,0],[1,0,1,1,0,1,0],[0,0,1,0,1,0,0],[0,0,1,0,0,0,0]]
graph={}
d={0:'Math',1:'Eng',2:'Bio',3:'French',4:'CS',5:'Hist',6:'Psy'}

for i in range(len(l)):
    k=[]
    for j in range(len(l[i])):
        if l[i][j]==1:
            k.append(d[j])
    print(k)
    graph[d[i]] = k
    
# print(graph)
graph_color(graph)