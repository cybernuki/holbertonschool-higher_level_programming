
#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return None
    
    n_set = set (my_list)
    return sum(n_set)