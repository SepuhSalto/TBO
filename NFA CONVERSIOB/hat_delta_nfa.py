from delta_nfa import l1Deltanfa

def hat1(initial_state, input_string):
    current_states = {initial_state}
    trace_steps = [f"δ̂ ({initial_state}, ε) = {{{initial_state}}}."]

    for i, symbol in enumerate(input_string, 1):
        next_states = set()
        transitions = [f"δ({state}, {symbol}) = {l1Deltanfa(state, symbol)}" for state in current_states if l1Deltanfa(state, symbol)]
        
        if not transitions:
            trace_steps.append(f"δ̂ ({current_states}, {input_string[:i]}) = ∅ (no valid transition).")
            break
        
        next_states.update(*[l1Deltanfa(state, symbol) for state in current_states if l1Deltanfa(state, symbol)])
        trace_steps.append(f"δ̂ ({current_states}, {input_string[:i]}) = {' ∪ '.join(transitions)} = {next_states}.")
        current_states = next_states 

    for step in trace_steps:
        print(step)

    return current_states


