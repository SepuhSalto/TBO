from hat_delta_dfa import l1Hat

def l1(x) -> bool:
    final_state = l1Hat('q0', x)  
    return True if final_state == 'q10' else False  
