from hat_delta_nfa import l1Hatnfa, l2Hatnfa, l3Hatnfa, l4Hatnfa

def l1nfa(x) -> bool:
    print('A', end='') 
    final_states = l1Hatnfa({'A'}, x)  
    print("\nFinal States:", final_states)  
    return True if 'E' in final_states else False  

def l2nfa(x) -> bool:
    print('A', end='') 
    final_states = l2Hatnfa({'A'}, x)  
    print("\nFinal States:", final_states)  
    return True if 'E' in final_states else False

def l3nfa(x) -> bool:
    print('A', end='') 
    final_states = l3Hatnfa({'A'}, x)  
    print("\nFinal States:", final_states)  
    return True if 'D' in final_states else False

def l4nfa(x) -> bool:
    print('A', end='') 
    final_states = l4Hatnfa({'A'}, x)  
    print("\nFinal States:", final_states)  
    return True if 'F' in final_states else False
