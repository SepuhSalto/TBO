def l1Delta(state, x) -> str:
    if state == 'q0':
        return 'q1' if x == 'Y' else 'q0'
    elif state == 'q1':
        return 'q2' if x == 'Y' else 'q0'
    elif state == 'q2':
        return 'q3' if x == 'Y' else 'q0'
    elif state == 'q3':
        return 'q4' if x == 'Y' else 'q0'  
    elif state == 'q4':
        return 'q5' if x == 'Y' else 'q0'
    elif state == 'q5':
        return 'q6' if x == 'Y' else 'q0'
    elif state == 'q6':
        return 'q7' if x == 'Y' else 'q0'
    elif state == 'q7':
        return 'q8' if x == 'Y' else 'q0'
    elif state == 'q8':
        return 'q9' if x == 'Y' else 'q0'
    elif state == 'q9':
        return 'q10' if x == 'Y' else 'q0'
    elif state == 'q10':
        return 'q10' if x == 'Y' else 'q10'
