from string import Template


def get_users(filename=None):
    """ Get a file contain username & name
        Return username & name of the person form file name
        Result: {'username': 'name'}
    """
    with open(filename) as f:
        users = {}
        for line in f.readlines():
            username = line.split(':')[0]
            user = line.split(':')[4]
            users[username] = user
    return users

def convert_usage_unit(records):
    # get records convert bytes to propr unit and return 
    # the result records

    result = []
    for user, size_in_byte in records:
        size_in_kb = size_in_byte // 2 ** 10
        size_in_mb = size_in_byte // 2 ** 20
        size_in_gb = size_in_byte // 2 ** 30

        if size_in_gb:
            size = str(size_in_gb) + 'GB' 
        elif size_in_mb:
            size = str(size_in_mb) + 'MB' 
        elif size_in_kb:
            size = str(size_in_kb) + 'KB' 
        else:
            size = str(size_in_byte) + 'Byte'
        
        result.append((user, size))
    return result


def get_usage(filename):
    """ return a dictionary contain {'userid': 'size in gb'}
    """
    with open(filename) as f:
        usage = {}
        for line in f.readlines():
            splited_line = line.split(',')
            userid = splited_line[0].split('=')[-1]
            size_in_byte = int(splited_line[-1].split('=')[-1])
            usage[userid] = size_in_byte
    return usage
          

def sort_usage(records):
    return  sorted(records, key=lambda t: t[1], reverse=True)            
    


def get_output(sort=True):
    """ {username: sizingb} """
    users = get_users('thinlinc.txt')
    usage = get_usage('diskusage.txt')
    records = []
    for username in users:
        if username in usage:
            record = (users[username], usage[username])
            records.append(record)
    if sort:
        sorted_records = sort_usage(records)
        return convert_usage_unit(sorted_records)
    return records


def write_file(filename, content=''):
    with open(filename, 'w') as f:
        f.write(content)


def get_preformatted(user=None, format_type='html', to_file=False):
    records = get_output()
    formats = {
    'html': ['<p>{}) {} {}</p><hr>\n', 
            '<p style="background-color:yellow;">{}) {} {}</p><hr>\n'],
    'txt': ['{:<10d}{:-<30}{:->10}\n',
            '*{:<9d}{:-<30}{:->10}\n'],
    }
    output = ''
    if user is not None:
        for index, record in enumerate(records, start=1):    
            name, size = record
            if user == name:
                output += formats[format_type][1].format(index, name, size)
            else:
                output += formats[format_type][0].format(index, name, size)
    # create output in general, no user preformatted
    else:
        for index, record in enumerate(records, start=1):    
            name, size = record
            output += '<p>{} {} {}GB</p>\n'.format(index, name, size)
    # create a file with content of 'output' with name 'message.txt'
    if to_file:
        filename = 'message.txt'
        write_file(filename, output)
        return filename
    return output


if __name__ == '__main__':
    x = get_preformatted('Moeen.Rajput')
    print(x)