from delta_nfa import l1Deltanfa, l2Deltanfa, l3Deltanfa, l4Deltanfa

def l1Hatnfa(states, x) -> set:
    for symbol in x: 
        new_states = set()  
        for state in states:  
            delta_states = l1Deltanfa(state, symbol)  
            if delta_states is not None:
                new_states = new_states.union(delta_states)  
        states = new_states 
        print("-->", states, end='')  
    return states


def l2Hatnfa(states, x) -> set:
    for symbol in x: 
        new_states = set()  
        for state in states:  
            delta_states = l2Deltanfa(state, symbol)  
            if delta_states is not None:
                new_states = new_states.union(delta_states)  
        states = new_states 
        print("-->", states, end='')  
    return states

def l3Hatnfa(states, x) -> set:
    for symbol in x: 
        new_states = set()  
        for state in states:  
            delta_states = l3Deltanfa(state, symbol)  
            if delta_states is not None:
                new_states = new_states.union(delta_states)  
        states = new_states 
        print("-->", states, end='')  
    return states

def l4Hatnfa(states, x) -> set:
    for symbol in x: 
        new_states = set()  
        for state in states:  
            delta_states = l4Deltanfa(state, symbol)  
            if delta_states is not None:
                new_states = new_states.union(delta_states)  
        states = new_states 
        print("-->", states, end='')  
    return states
