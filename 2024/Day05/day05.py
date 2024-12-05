file = open('input.txt', 'r')
text = file.read().strip()


def clean_text(text):
    split_text = text.split('\n\n')
    rules = [[int(x) for x in line.split('|')] for line in split_text[0].splitlines()]
    updates = [[int(x) for x in line.split(',')] for line in split_text[1].splitlines()]
    return rules, updates


def part1(rules, page_numbers):
    # map each element to the set of page numbers that must come after it
    rules_dict = {}
    for left, right in rules:
        if left not in rules_dict:
            rules_dict[left] = {right}  # create a set
        else:
            rules_dict[left].add(right)  # add to the set

    total = 0
    for update in updates:
        valid = True
        for i in range(len(update) - 1):
            current = update[i]
            afters = update[i + 1 :]
            # make sure that set of pages that come after the current page is a subset of the current page's rules
            if current not in rules_dict or not (set(afters) <= rules_dict[current]):
                valid = False
                break
        if valid:
            total += update[len(update) // 2]
    return total


def part2(rules, page_numbers):
    # map each element to the set of page numbers that must come after it
    # also map each element to the set of page numbers that must come before it
    rules_dict_after = {}
    rules_dict_before = {}
    for left, right in rules:
        if left not in rules_dict_after:
            rules_dict_after[left] = {right}  # create a set
        else:
            rules_dict_after[left].add(right)  # add to the set
        if right not in rules_dict_before:
            rules_dict_before[right] = {left}  # create a set
        else:
            rules_dict_before[right].add(left)

    # get the list of incorrectly ordered updates
    incorrect_updates = []
    for update in updates:
        for i in range(len(update) - 1):
            current = update[i]
            afters = update[i + 1 :]
            # check if set of pages that come after the current page is a subset of the current page's rules
            if current not in rules_dict_after or not (set(afters) <= rules_dict_after[current]):
                incorrect_updates.append(update)
                break

    total = 0
    for update in incorrect_updates:
        # iterate through page numbers until we find the middle page
        # the middle page will be the one with an equal number of pages in its before rules and after rules
        for i in update:
            before = 0
            after = 0
            for j in update:
                if i == j:
                    continue
                if i in rules_dict_after and j in rules_dict_after[i]:
                    after += 1
                if i in rules_dict_before and j in rules_dict_before[i]:
                    before += 1
            if before == after:
                total += i
                break
    return total


rules, updates = clean_text(text)
print('Solution 1:', part1(rules, updates))
print('Solution 2:', part2(rules, updates))
