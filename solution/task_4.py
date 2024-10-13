def pipeline(stages: list[int], details: list[int]) -> list[int]:
    full_time = sum(stages)
    max_time = max(stages)
    sorted_details = sorted(details)
    first_detail = min(details)
    for i in range(len(details)):
        details[i] = sorted_details.index(details[i])*max_time+full_time+first_detail
