def maximize_it(list1, k):
    r = []
    for i in list1:
        a = sum(x*x for x in i)%k
        r.append(a)
    print(max(r))




# maximize_it([[2,5,4],[3,7,8,9],[5,5,7,8,9,10]], 1000)
maximize_it([[67828645,425092764, 242723908, 669696211, 501122842, 438815206],[625649397, 295060482, 262686951, 815352670], [100876777, 196900030, 523615865]], 998)