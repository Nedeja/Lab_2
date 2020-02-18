raw_address = input("enter a raw address:")

def check_for_errors(raw_address):
    """
    this function checks if raw address is entered
    in a right way
    >>> check_for_errors(91.124.230.205/30)
    True
    >>> check_for_errors('dhhfh')
    
    """
    raw_address_list = raw_address.split('.')
    if len(raw_address_list)  != 4:
        return None
    for i in raw_address_list:
        if '/' in i:
            ind = i.index('/')
            i = i.replace(i[ind:], '')
            if int(i) > 255:
                return None
    ind = raw_address.index('/')
    if int(raw_address[ind +1:]) > 32:
        return None
    return True
check_for_errors(raw_address)

def get_ip_from_raw_address(raw_address):
    """
    this function returs an IP address without mask
    >>> get_ip_from_raw_address('192.168.1.15/24')
    192.168.1.15
    """
    if check_for_errors(raw_address) != True:
        return None
    else:
        IP = []
        for i in raw_address:
            if i != '/':
                IP += i 
            else:
                break
        IP = ''.join(IP)
        return IP
print(get_ip_from_raw_address(raw_address))

def get_mask_from_raw_address(raw_address):
    """
    this function gets a mask from a raw address
    >>> get_mask_from_raw_address(91.124.230.205/30)
    255.255.255.252
    """
    if check_for_errors(raw_address) != True:
        return None
    else:
        prefix = int(raw_address[-2:])
        mask = [0, 0, 0, 0]

        for i in range(prefix):
            mask[i // 8] += 1 << (7 - i % 8)
        mask_int = []
        for i in mask:
            mask_int.append(str(i))
        return mask
print('.'.join(str(x) for x in get_mask_from_raw_address(raw_address)))

def get_network_address_from_raw_address(raw_address):
    """
    this functionn gets a network address from raw mask
    >>> get_network_address_from_raw_address(91.124.230.205/30)
    91.124.230.204
    """
    if check_for_errors(raw_address) != True:
        return None
    else:
        mask = get_mask_from_raw_address(raw_address)
        IP = get_ip_from_raw_address(raw_address)
        ip= IP.split('.')
        ip_int = []
        for i in ip:
            ip_int.append(int(i))
        network_address = []
        for i in range(4):
            network_address.append(str(ip_int[i] & mask[i]))
        network_address = '.'.join(network_address)
        # print('Network address is:',network_address)
        return network_address
print(get_network_address_from_raw_address(raw_address))

def get_binary_network_address_from_raw_address(raw_address):
    """
    this function returns a binary form of a network address
    >>> get_binary_network_address_from_raw_address(91.124.230.205/30)
    01011011.01111100.11100110.11001100
    """
    if check_for_errors(raw_address) != True:
        return None
    else:
        network_address = get_network_address_from_raw_address(raw_address)
        new_net = network_address.replace('.', ' ')
        new_net = new_net.split(' ')
        net_piece = []
        for i in new_net:
            net_piece.append(bin(int(i)))
        net_ad = []
        for i in net_piece:
            i = i.replace('0b', '')
            if len(i) < 8:
                i = '0' * (8 - len(i)) + i
            net_ad.append(i)
        net_ad_dot = ".".join(net_ad)
        return net_ad_dot
print(get_binary_network_address_from_raw_address(raw_address))

def get_second_usable_ip_address_from_raw_address(raw_address):
    """
    this function get a secondusable IP address from raw address
    >>> get_second_usable_ip_address_from_raw_address(91.124.230.205/30)
    91.124.230.206
    """
    if check_for_errors(raw_address) != True:
        return None
    else:
        network_address = get_network_address_from_raw_address(raw_address)
        network_address = network_address.split('.')
        network_address[3] = str(int(network_address[3]) + 2)
        return network_address
print('.'.join(get_second_usable_ip_address_from_raw_address(raw_address)))

def get_last_usable_ip_address_from_raw_address(raw_address):
    """
    this function gets a last usable IP address from raw address
    >>> get_last_usable_ip_address_from_raw_address(91.124.230.205/30)
    91.124.230.206
    """
    if check_for_errors(raw_address) != True:
        return None
    else:
        IP = get_ip_from_raw_address(raw_address)
        IP = IP.split('.')
        IP_lst = []
        for k in IP:
            IP_lst.append(int(k))
        mask = get_mask_from_raw_address(raw_address)
        binar_mask = []
        for i in mask:
            binar_mask.append(str(bin(i)).replace('0b', ''))
        binar_mask = '.'.join(binar_mask)
        sub_mask = ''
        for j in binar_mask:
            if j == '0':
                sub_mask += '1'
            if j == '1':
                sub_mask += '0'
            if j == '.':
                sub_mask += '.'
        sub_mask= sub_mask.split('.')
        sub_mask_lst= []
        for i in sub_mask:
            sub_mask_lst.append(int('0b' + i, 2))
        # print(sub_mask_lst)
        second_ip_address_st = []
        for i in range(4):
            second_ip_address_st.append(str(IP_lst[i] | sub_mask_lst[i]))
        second_ip_address_st[3] = str(int(second_ip_address_st[3]) - 1)
        return second_ip_address_st
print(".".join(get_last_usable_ip_address_from_raw_address(raw_address)))

def get_total_number_of_ips_from_raw_address(raw_address):
    """
    this function gets a total number of possible ips
    >>> get_total_number_of_ips_from_raw_address(r91.124.230.205/30)
    4
    """
    if check_for_errors(raw_address) != True:
        return None
    else:
        mask = int(raw_address.split('/')[-1])
        total_number = 2 ** (32 - mask)
        return total_number
print(get_total_number_of_ips_from_raw_address(raw_address))

def get_ip_class_from_raw_address(raw_address):
    """
    this function gets an IP class from a raw address
    >>> get_ip_class_from_raw_address(91.124.230.205/30)
    A
    """
    if check_for_errors(raw_address) != True:
        return None
    else:
        first_oct = int(raw_address[0:2])
        if first_oct in range(0, 128):
            return('A')
        if first_oct in range(128, 192):
            return('B')
        if first_oct in range(192, 224):
            return('C')
print(get_ip_class_from_raw_address(raw_address))

def get_ip_address_type_from_raw_address(raw_address):
    """
    this function gets a type of IP address from a raw address
    >>> et_ip_address_type_from_raw_address(91.124.230.205/30)
    Public
    """
    if check_for_errors(raw_address) != True:
        return None
    else:
        IP = get_ip_from_raw_address(raw_address)
        ip = IP.split('.')
        first_oct = int(ip[0])
        second_oct = int(ip[1])
        if first_oct == 10:
            return 'Private'
        if first_oct == 172 and second_oct in range(16, 32):
            return "Private" 
        if first_oct == 192:
            return "Private"
        else:
            return 'Public'
print(get_ip_address_type_from_raw_address(raw_address))
