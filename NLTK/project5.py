def levenshtein(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1,m+1):
        for j in range(1,n+1):
            cost = 0 if s1[i-1]==s2[j-1] else 1
            dp[i][j] = min(dp[i-1][j]+1,      
                           dp[i][j-1]+1,       
                           dp[i-1][j-1]+cost)  
    return dp[m][n]

keyboard_neighbors = {
    'q':'was', 'w':'qase', 'e':'wsdr', 'r':'edft', 't':'rfgy',
    'y':'tghu', 'u':'yhji', 'i':'ujko', 'o':'iklp', 'p':'ol',
    'a':'qwsz', 's':'qwedxz', 'd':'ersfcx', 'f':'drtgvc', 'g':'ftyhbv',
    'h':'gyujnb', 'j':'huikmn', 'k':'jiolm', 'l':'kop', 'z':'asx',
    'x':'zsdc', 'c':'xdfv', 'v':'cfgb', 'b':'vghn', 'n':'bhjm', 'm':'njk'
}

def weighted_levenshtein(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                cost = 0
            elif s2[j-1] in keyboard_neighbors.get(s1[i-1], ''):
                cost = 0.5  
            else:
                cost = 1
            dp[i][j] = min(dp[i-1][j]+1,
                           dp[i][j-1]+1,
                           dp[i-1][j-1]+cost)
    return dp[m][n]

typed_word = "HELLP"

dictionary = ["HELLO", "HELP", "HILL", "HEAP"]

suggestions = sorted(dictionary, key=lambda w: weighted_levenshtein(typed_word.lower(), w.lower()))

print("Suggested correction:", suggestions[0])