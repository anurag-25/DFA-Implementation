# Defining transitions from all the states for all the input characters
# Here states, Q = {1,2,3} corresponding to q1, q2 and q3 in the problem.
# The input characters = {a,b}
def transition (currentState, inputCharacter):

    #Defining transitions from state 1.
    if (currentState == 1):
        if (inputCharacter == 'a'):    
            nextState = 2
            return nextState
        if (inputCharacter == 'b'):    
            nextState = 1
            return nextState  
        
    #Defining transitions from state 2.
    if (currentState == 2):
        if (inputCharacter == 'a'):    
            nextState = 3
            return nextState
        if (inputCharacter == 'b'):    
            nextState = 3
            return nextState  

    #Defining transitions from state 3.
    if (currentState == 3):
        if (inputCharacter == 'a'):    
            nextState = 2
            return nextState
        if (inputCharacter == 'b'):    
            nextState = 1
            return nextState  

#Defining the Initial State and Accept State of DFA.
initialState = 1
acceptState = 2

#Take the input string from user and determine its length.
inputString = input ("Enter String to be processed: ")
length = len (inputString)

# Simulate the DFA on this string using the transitions defined 
# above, starting for initial state (=1).
currentState = initialState
for i in range (length):
    # Take the next character from input string in each iteration
    currentCharacter = inputString[i]
    
    # Updating the currentState using the transition for the 
    # current input character and state.
    currentState = transition (currentState, currentCharacter)

# After the computation is done, check if the state reached finally 
# is the accept state or not. If yes, then ACCEPT. Else reject.
if (currentState == acceptState):
    print (inputString, "is accepted by the DFA.")
else:
    print (inputString, "is rejected by the DFA.")
        