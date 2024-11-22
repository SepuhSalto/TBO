from delta_dfa import l1Delta
def l1Hat(state,x) -> str:
    if x == '':
        return state
    else:
        state = l1Delta(l1Hat(state, x[0:-1]), x[-1])
        return state
