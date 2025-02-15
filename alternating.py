def longest_substring(l):
    sum=1
    d={}
    left=0
    right=1
    t=''
    s=''
    while right <= len(l) :
        t+=l[left]
        if int(l[left])%2 != int(l[right-1])%2 and right==len(l):
            t+=l[right-1]
            d[t]=sum
            break
        elif int(l[left])%2 == int(l[right-1])%2 and right==len(l):
            d[t]=sum
            break
        elif int(l[left])%2 != int(l[right])%2:
            sum+=1
            left=right
            right+=1
        elif int(l[left])%2 == int(l[right])%2:
            d[t]=sum
            sum=1
            t=''
            left=right
            right+=1
            continue
    m=max(d.values())
    for k in d.keys():
        if d[k]==m:
            s=k
            break
        else:
            continue
    return s

print(longest_substring("736237766362158694825822899262"))
##print(len('10101010101010101'))
print(longest_substring("844929328912985315632725682153")=="56327256")
print(longest_substring("769697538272129475593767931733")=="27212947")
print(longest_substring("937948289456111258444958189244")=="894561")
print(longest_substring("736237766362158694825822899262")=="636")
print(longest_substring("369715978955362655737322836233")=="369")
print(longest_substring("345724969853525333273796592356")=="496985")
print(longest_substring("548915548581127334254139969136")=="8581")
print(longest_substring("417922164857852157775176959188")=="78521")
print(longest_substring("251346385699223913113161144327")=="638569")
print(longest_substring("483563951878576456268539849244")=="18785")
print(longest_substring("853667717122615664748443484823")=="474")
print(longest_substring("398785511683322662883368457392")=="98785")
print(longest_substring("368293545763611759335443678239")=="76361")
print(longest_substring("775195358448494712934755311372")=="4947")
print(longest_substring("646113733929969155976523363762")=="76523")
print(longest_substring("575337321726324966478369152265")=="478369")
print(longest_substring("754388489999793138912431545258")=="545258")
print(longest_substring("198644286258141856918653955964")=="2581418569")
print(longest_substring("643349187319779695864213682274")=="349")
print(longest_substring("919331281193713636178478295857")=="36361")
print(longest_substring("2846286484444288886666448822244466688822247")=="47")