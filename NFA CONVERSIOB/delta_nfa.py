def l1Deltanfa(state, symbol):
    if state == 'q0' and symbol == 'a':
        return {'q1', 'q2'}
    elif state == 'q1' and symbol == 'b':
        return {'q3', 'q4'}
    elif state == 'q2' and symbol == 'b':
        return {'q1'}
    elif state == 'q3' and symbol == 'b':
        return {'q1'}
    elif state == 'q4' and symbol == 'a':
        return {'q5'}
    else:
        return set()  


