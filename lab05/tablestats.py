def read_rows(lines):
    headers = None
    rows = []

    for line in lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue

        fields = [field.strip() for field in cleaned_line.split(',')]

        if headers is None:
            headers = fields
            continue

        if len(fields) != len(headers):
            continue

        row_dict = {}
        for i in range(len(headers)):
            row_dict[headers[i]] = fields[i]
        rows.append(row_dict)

    return rows