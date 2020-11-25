import collections

cpdomains=["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
#["9001 discuss.leetcode.com"]

def subdomainVisits(cpdomains):
    table=collections.defaultdict(int)
    sp_dm=[]
    for domain in cpdomains:
        sp_dm=domain.split(' ')
        sp_dm_1=sp_dm[1].split('.')
        for i in range(len(sp_dm_1)):
            table['.'.join(sp_dm_1[i:])]+=int(sp_dm[0])

    ans=[]
    for val, val2 in table.items():
        ans.append(str(val2)+" "+val)
    return ans


print(subdomainVisits(cpdomains))
