def read_file(filename):
    reports = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            levels = line.split(' ')
            levels = [int(level) for level in levels]
            reports.append(levels)
    
    return reports

def is_safe(report):
    count_asc = 0
    count_desc = 0
    for i in range(len(report)):
        if (i + 1) < len(report):
            if report[i] < report[i+1]:
                count_asc += 1
            elif report[i] > report[i+1]:
                count_desc += 1
            abs_diff = abs(report[i+1] - report[i])
            if 1 <= abs_diff <= 3:
                continue
            else:
                return False
        if i == len(report) - 1:
            if count_asc == 0 or count_desc == 0:
                return True
            else:
                return False

if __name__ == '__main__':
    reports = read_file('input.txt')
    safe_report = 0
    for report in reports:
        if is_safe(report):
            safe_report += 1
            continue
        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)
            if is_safe(new_report):
                print('report: ', report)
                safe_report += 1
                break
    print("Part1: ", safe_report)


                