from datetime import datetime as dt


def get_results(leader_time, your_time):
    time_format = '%H:%M:%S'
    leader_time_object = dt.strptime(leader_time, time_format)
    your_time_object = dt.strptime(your_time, time_format)

    if your_time_object == leader_time_object:
        return f'Вы пробежали за {your_time} и победили!'
    else:
        difference = your_time_object - leader_time_object
        return (f'Вы пробежали за {your_time} '
                f'с отставанием от лидера на {difference}.')


print(get_results('02:02:02', '02:02:02'))
print(get_results('02:02:02', '03:04:05'))
