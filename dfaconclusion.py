from hat_delta_dfa import l1Hat

def l1(x) -> bool:
    print('A', end = '')
    final_state = l1Hat('A', x)  
    print("\nFinal State:", final_state)  
    return True if final_state == 'F' else False  
