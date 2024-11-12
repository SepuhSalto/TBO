from collections import defaultdict

def identify_dfa_states(nfa_states, nfa_transitions, input_symbols):
    dfa_transitions = {}
    dfa_states = {frozenset(nfa_states)}
    unprocessed_states = [frozenset(nfa_states)]
    
    while unprocessed_states:
        current_dfa_state = unprocessed_states.pop()
        dfa_transitions[current_dfa_state] = {}

        for symbol in input_symbols:
            next_dfa_state = set()
            for nfa_state in current_dfa_state:
                next_dfa_state.update(nfa_transitions[nfa_state].get(symbol, set()))
            
            next_dfa_state = frozenset(next_dfa_state)
            dfa_transitions[current_dfa_state][symbol] = next_dfa_state

            if next_dfa_state not in dfa_states:
                dfa_states.add(next_dfa_state)
                unprocessed_states.append(next_dfa_state)

    return dfa_states, dfa_transitions

def identify_dfa_final_states(dfa_states, nfa_final_states):
    dfa_final_states = set()
    for dfa_state in dfa_states:
        if dfa_state & nfa_final_states:
            dfa_final_states.add(dfa_state)
    return dfa_final_states

def convert_nfa_to_dfa_transitions(nfa_start_state, nfa_final_states, nfa_transitions, input_symbols):
    dfa_states, dfa_transitions = identify_dfa_states([nfa_start_state], nfa_transitions, input_symbols)
    dfa_final_states = identify_dfa_final_states(dfa_states, nfa_final_states)
    return dfa_states, dfa_transitions, dfa_final_states

def delta_dfa(dfa_transitions, current_state, symbol):
    return dfa_transitions.get(current_state, {}).get(symbol, frozenset())

def hat_delta_dfa(dfa_transitions, start_state, input_string):
    current_state = start_state
    for symbol in input_string:
        print(f"Transition δ({current_state}, {symbol}) -> {dfa_transitions[current_state].get(symbol)}")
        current_state = delta_dfa(dfa_transitions, current_state, symbol)
    return current_state

def main_dfa():

    nfa_transitions = defaultdict(lambda: defaultdict(set))
    nfa_transitions['q0']['a'] = {'q1', 'q2'}
    nfa_transitions['q1']['b'] = {'q3', 'q4'}
    nfa_transitions['q2']['b'] = {'q1'}
    nfa_transitions['q3']['b'] = {'q1'}
    nfa_transitions['q4']['a'] = {'q5'}

    nfa_start_state = 'q0'
    nfa_final_states = {'q3', 'q5'}
    input_symbols = {'a', 'b'}

    dfa_states, dfa_transitions, dfa_final_states = convert_nfa_to_dfa_transitions(nfa_start_state, nfa_final_states, nfa_transitions, input_symbols)

    print(f"DFA States: {dfa_states}")
    print(f"DFA Final States: {dfa_final_states}")

    test_strings = ["ab", "abb", "abbb", "aba", "abba", "abbba"]
    for test_string in test_strings:
        print(f"\nChecking string: {test_string}")
        final_dfa_state = hat_delta_dfa(dfa_transitions, frozenset([nfa_start_state]), test_string)

        if final_dfa_state in dfa_final_states:
            print(f"String '{test_string}' Diterima oleh DFA.")
        else:
            print(f"String '{test_string}' Ditolak Oleh DFA.")

main_dfa()
