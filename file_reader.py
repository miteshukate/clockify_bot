def get_time_entries():
    entries = []
    with open('entries.txt') as f:
        entries = f.readlines()
    return entries
