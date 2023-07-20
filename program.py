
def geo_log(geo_logs):
    geo_logs_rus = 'Россия'
    geo_logs_new = list(filter(lambda x: geo_logs_rus in list(x.values())[0], geo_logs))
    return geo_logs_new


def uniq_id(ids):
    result = []
    for numbers in ids.values():
        for num in numbers:
            if num not in result:
                result.append(num)
    return result


def max_volume(stats):
    stats_maxs = max(stats, key=stats.get)
    return stats_maxs


