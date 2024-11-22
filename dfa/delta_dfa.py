def l1Delta(state, x) -> str:
    if state == 'q0':
        return 'q1' if x == 'Y' else 'q0'
    elif state == 'login':
        return 'q0' if x == 'Y' else 'login'
    elif state == 'q1':
        return 'q2' if x == 'Y' else 'q1'
    elif state == 'q2':
        return 'q3' if x == 'Y' else 'q2'
    elif state == 'q3':
        return 'q4' if x == 'Y' else 'q3'  
    elif state == 'q4':
        return 'q5' if x == 'Y' else 'q5'
    elif state == 'q5':
        return 'q6' if x == 'Y' else 'q5'
    elif state == 'q6':
        return 'q7' if x == 'Y' else 'q6'
    elif state == 'q7':
        return 'q8' if x == 'Y' else 'q7'
    elif state == 'q8':
        return 'q8' if x == 'Y' else 'q8'
