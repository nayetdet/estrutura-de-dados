def has_more_vogals(x: str, vogal_count: int = 0, consoant_count: int = 0) -> bool:
    if not x:
        return vogal_count > consoant_count

    first_letter = x[0]
    if first_letter.lower() in "aeiou": vogal_count += 1
    elif first_letter.isalpha(): consoant_count += 1
    return has_more_vogals(x[1:], vogal_count, consoant_count)
