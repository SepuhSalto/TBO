def l1Deltanfa(state, x) -> set:
    new_states = set()  
    
    if state == 'A':
        if x == '1':
            new_states.add('B')  
    elif state == 'B':
        if x == '0':
            new_states.add('C')  
    elif state == 'C':
        if x == '0':
            new_states.add('C')  
            new_states.add('D')  
        elif x == '1':
            new_states.add('C')  

    elif state == 'D':
        if x == '1':
            new_states.add('E')  
    elif state == 'E':
        pass  
    
    return new_states if new_states else None  


def l2Deltanfa(state, x) -> set:
    new_states = set()  
    
    if state == 'A':
        if x == '0':
            new_states.add('A')  
            new_states.add('B')  
        elif x == '1':
            new_states.add('A')  
    elif state == 'B':
        if x == '0':
            new_states.add('C')  
    elif state == 'C':
        if x == '0':  
            new_states.add('D')    
    elif state == 'D':
        if x == '1':
            new_states.add('D')  
            new_states.add('E')  
        elif x == '0':
            new_states.add('D')   
    elif state == 'E':
        pass  
    
    return new_states if new_states else None  

def l3Deltanfa(state, x) -> set:
    new_states = set()  
    
    if state == 'A':
        if x == '1':
            new_states.add('C')  
        elif x =='0':
            new_states.add('B')
    elif state == 'B':
        if x == '1':
            new_states.add('B')  
            new_states.add('D')  
        elif x == '0':
            new_states.add('B')   
    elif state == 'C':
        if x == '0':
            new_states.add('C')  
            new_states.add('D')  
        elif x == '1':
            new_states.add('C')  
    elif state == 'D':
        pass 
    return new_states if new_states else None  

def l4Deltanfa(state, x) -> set:
    new_states = set()  
    
    if state == 'A':
        if x == '0':
            new_states.add('B')  
        elif x =='1':
            new_states.add('G')  
    elif state == 'B':
        if x == '1':
            new_states.add('B')
            new_states.add('C')  
        elif x =='0':
            new_states.add('B')  
    elif state == 'C':
        if x == '0':
            new_states.add('D')  
    elif state == 'D':
        if x == '1':
            new_states.add('E')  
    elif state == 'E':
        if x == '0':
            new_states.add('E')
            new_states.add('F')
        elif x == '1':
            new_states.add('E')
    elif state == 'F':
        if x == '0':
            new_states.add('H')
        elif x == '1':
            new_states.add('F') 
    elif state == 'G':
        if x == '1':
            new_states.add('G')    
        elif x == '0':
            new_states.add('H') 
    elif state == 'H':
        if x == '0':
            new_states.add('G')
        elif x == '1':
            new_states.add('F')     
    return new_states if new_states else None  
