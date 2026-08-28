class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # hot -> *ot, h*t, ho*
        # {*ot: [hot, dot, tot]}
        # bfs

        if endWord not in wordList:
            return 0

        # default dictionary - when we insert a new value for the first time the default will have empty list 
        neighbors = collections.defaultdict(list)

        # append the begin word since it is not part of the word list initially
        wordList.append(beginWord)


        # check ign patterns for each word
        for word in wordList:
            # all words are of same lenght - given
            for j in range(len(word)):
                # for each character of a word, replace char with a wild card character *
                pattern = word[:j] + "*" + word[j+1:]
                # in our neighbours list all the words that fall into this pattern, append it to their corresponding list in dictionary
                neighbors[pattern].append(word)
                # this word is a part of this pattern

        # bfs algorithm
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1 

        while q:
            for i in range(len(q)):
                # pop a word and check if its the endWord
                word=q.popleft()
                if word==endWord:
                    return res
                # if not then take the neighbours of this word and add them to the queue
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiword in neighbors[pattern]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)


            # increament as we go from each layer by layer
            res +=1
        return 0


