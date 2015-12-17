def tsne_viz(X,filename,S=2000,s=50,method='exact'):
    ''' T-SNE image embeding visualization'''
    ''' python version of the code provided by karpathy (http://cs.stanford.edu/people/karpathy/cnnembed/)'''
    G = np.zeros((S,S,3))
    
    # Normalize data between 0 and 1
    min_max_scaler = preprocessing.MinMaxScaler() 
    X_scaled = min_max_scaler.fit_transform(X_2d)

    
    if method=='exact':
        for i in range(len(filename)):
            if (i%1000==0):
                print "Iter",i,"from",Ntake

            a = np.ceil(X_scaled[i,0]* (S-s))
            b = np.ceil(X_scaled[i,1]* (S-s))

            a = a-np.mod(a,s)
            b = b-np.mod(b,s)
            if G[a,b,1] != 0:
                continue #% spot already filled
            image = caffe.io.load_image('/home/deep/dades/500px/' + filename[i])
            image = caffe.io.resize_image(image,(s,s))
            G[a:a+s, b:b+s, :] = image;
    
    if method=='squared':
        xnum = S/s
        ynum = S/s

        used = np.zeros((N))
        qq = np.ceil(S/s)
        abes = np.zeros((qq**2,2))

        i=0
        for a in range(0,S,s):
            for b in range(0,S,s):
                abes[i,0] = a 
                abes[i,1] = b
                i=i+1

        for i in range(len(abes)):
            if (i%1000==0):
                print "Iter",i,"from",len(abes)
            a = abes[i,0]
            b = abes[i,1]    
            xf = (a-1)/S
            yf = (b-1)/S
            dd =np.sum(np.power((X[:,:] - (xf,yf)),2),1)
            dd[used==1]=np.inf
            di = dd.argmin() #find nearest image

            used[di] = True #mark as done

            image = caffe.io.load_image('/home/deep/dades/500px/' + filename[di])
            image = caffe.io.resize_image(image,(s,s))
            G[a:a+s, b:b+s, :] = image;

    return G
