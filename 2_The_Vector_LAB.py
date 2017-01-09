f = open('voting_record_dump109.txt','r')
mylist = list(f)


def list_dot(u,v):
    return sum([a*b for (a,b) in zip(u,v)])
    
    
def create_voting_dict(strlist):
    d = dict()
    for s in strlist:
        ss = s.split(' ')
        d[ss[0]] = [int(x) for x in ss[3:]]
    return d


votes = create_voting_dict(mylist)


def policy_compare(sen_a,sen_b,voting_dict):
    return list_dot(voting_dict[sen_a],voting_dict[sen_b])

def addn(v,w):
    return [v[i] + w[i] for i in range(0,len(v))]
sen = 'Akaka'
voting_dict = votes
def most_similar(sen, voting_dict):
    sims = {s:list_dot(voting_dict[s],voting_dict[sen])for s in voting_dict if s != sen }
    max_sim = -999
    most_sim = ''
    for sim in sims:
        if sims[sim] >= max_sim:
            max_sim = sims[sim]
            most_sim = sim
    return most_sim
    

def least_similar(sen, voting_dict):
    sims = {s:list_dot(voting_dict[s],voting_dict[sen])for s in voting_dict if s != sen }
    max_sim = 999
    most_sim = ''
    for sim in sims:
        if sims[sim] <= max_sim:
            max_sim = sims[sim]
            most_sim = sim
    return most_sim
                   
# Task 2.12.5
most_similar('Chafee',votes)
least_similar('Santorum',votes)

def find_average_similarity(sen, sen_set,voting_dict):
    sims = {s:list_dot(voting_dict[s],voting_dict[sen])for s in voting_dict if (s != sen) & (s in sen_set)}
    sim_avg = sum([int(sims[s]) for s in sims]) / len(sims)
    return sim_avg
    
# democrats
democrats = set()
for d in mylist:
    dd = d.split(' ')
    if dd[1] == 'D':
        democrats.add(dd[0])
        
# average similarities to democracts
avg_sims = {sen:find_average_similarity(sen,democrats,votes) for sen in votes}
        
# most similar to democrats
max_sim = -999
most_sim = ''
for sim in avg_sims:
    if avg_sims[sim] >= max_sim:
        max_sim = avg_sims[sim]
        most_sim = sim
        
def find_average_record(sen_set,voting_dict):
    avg_votes=[0 for x in voting_dict[list(voting_dict.keys())[0]]]
    tt = [addn(voting_dict[v],avg_votes) for v in [s for s in voting_dict if s in sen_set]]
    