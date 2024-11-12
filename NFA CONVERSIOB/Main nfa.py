from hat_delta_nfa import hat1

def main():
    test_strings = ['ab', 'abb', 'abbb', 'aba', 'abba', 'abbba']
    initial_state = 'q0'
    final_states = {'q3', 'q5'}  # Single set containing 'q3' and 'q5'

    for x in test_strings:
        final_result_states = hat1(initial_state, x)

        print(f"State akhir untuk string '{x}': {final_result_states}")
        print(f"Final State NFA: {final_states}")

        # Check if any of the final result states intersect with the final states
        if final_result_states & final_states:
            print(f"String '{x}' diterima.")
        else:
            print(f"String '{x}' ditolak.")

main()
