def top7txt():
        alltext = []
        with open('Top7.txt', 'r') as top7:
            for line in top7.readlines():
                alltext.append(line)

        allminusn = []
        for line in alltext:
            minusn = line.replace("\n", "")
            allminusn.append(minusn)

        scoreonly = allminusn
        n = 10
        while n != 0:
            scoreonly = scoreonly[1: ]
            n -= 1

        nameonly = []
        m = 0
        for m in range(1, 8):
            nameonly = nameonly + [allminusn[m]]
            m += 1

        intscores = []
        i = 0
        scores = 7
        while i != scores:
            intscores.append(int(scoreonly[i]))
            i += 1

        

        def partition(arr, low, high):
            i = (low-1)         # index of smaller element
            pivot = arr[high]     # pivot
          
            for j in range(low, high):
          
                # If current element is smaller than or
                # equal to pivot
                if arr[j] <= pivot:
          
                    # increment index of smaller element
                    i = i+1
                    arr[i], arr[j] = arr[j], arr[i]
          
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return (i+1)
          
        # The main function that implements QuickSort
        # arr[] --> Array to be sorted,
        # low  --> Starting index,
        # high  --> Ending index
          
        # Function to do Quick sort
          
          
        def quickSort(arr, low, high):
            if len(arr) == 1:
                return arr
            if low < high:
          
                # pi is partitioning index, arr[p] is now
                # at right place
                pi = partition(arr, low, high)
          
                # Separately sort elements before
                # partition and after partition
                quickSort(arr, low, pi-1)
                quickSort(arr, pi+1, high)

        def check(score, sclist):
                if sclist == []:
                        return False
                elif score > sclist[0]:
                        return True
                else:
                        return check(score, sclist[1:])


        top7 = (nameonly, intscores) #tuple with names and scores
        names = top7[0] #names list
        scores = top7[1] #scores list
        user_name = 'Bruno'
        user_score = 250
        check = check(user_score, scores)
        if check == True:
                scores.append(user_score) #append the user's score
                n = len(scores) - 1 #variable for quick sort method
                sort = quickSort(scores, 0, n) #sorts the new list
                scores.reverse() #inverts the order of the array
                i = scores.index(user_score) #takes the new score's index
                names.insert(i, user_name) #adds the username in the index of the user score
                names = names[: -1] #finally, deletes the least score and name
                scores = scores[: -1]
        fortxt = ["Top 7 Players by score"] + names + [""] + ["Respective score"] + scores
        return fortxt
