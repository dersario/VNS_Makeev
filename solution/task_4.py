def pipeline(stages: list[int], details: list[int]) -> list[int]:
    d = {}
    full_time = sum(stages)
    max_time = max(stages)
    sorted_details = sorted(details)
    first_detail = min(details) + full_time
    for j in details:
        d[j] = sorted_details.index(j)
    print(d)
pipeline([5, 1, 10, 4],[3, 0, 4, 20])